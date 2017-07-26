# This file is part of CAT-SOOP
# Copyright (c) 2011-2017 Adam Hartz <hartz@mit.edu>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import time
import atexit
import ctypes
import signal
import subprocess

import rethinkdb as r

os.setpgrp()

scripts_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.abspath(os.path.join(scripts_dir, '..'))

if base_dir not in sys.path:
    sys.path.append(base_dir)

import catsoop.base_context as base_context

procs = (
    (scripts_dir, ['node', 'checker_reporter.js',
                   str(base_context.cs_websocket_server_port)], 0.1, 'Reporter'),
    (scripts_dir, ['python3', 'checker.py'], 0.1, 'Checker'),
    (base_dir, ['uwsgi', '--http', ':%s' % base_context.cs_wsgi_server_port,
                '--wsgi-file', 'wsgi.py',
                '--touch-reload', 'wsgi.py'], 0.1, 'WSGI Server'),
)

running = []

libc = ctypes.CDLL("libc.so.6")
def set_pdeathsig(sig = signal.SIGTERM):
    def callable():
        return libc.prctl(1, sig)
    return callable

# Start RethinkDB First

print('Starting RethinkDB Server')
running.append(subprocess.Popen(['rethinkdb'], cwd=scripts_dir,
                                preexec_fn=set_pdeathsig(signal.SIGTERM)))

# And give it some time
time.sleep(5)

# Now make sure the database is set up

c = r.connect()
try:
    r.db_create('catsoop').run(c)
except:
    pass
c.close()

c = r.connect(db='catsoop')

tables = r.table_list().run(c)
if 'logs' not in tables:
    r.table_create('logs').run(c)
    r.table('logs').index_create('log', [r.row['username'], r.row['path'], r.row['logname']]).run(c)
    r.table('logs').index_wait('log').run(c)

if 'checker' not in tables:
    r.table_create('checker').run(c)
    r.table('checker').index_create('progress').run(c)
    r.table('checker').index_wait('progress').run(c)
    r.table('checker').index_create('log', [r.row['username'], r.row['path']]).run(c)
    r.table('checker').index_wait('log').run(c)

c.close()

# Finally, start the workers.

for (wd, cmd, slp, name) in procs:
    print('Starting', name)
    running.append(subprocess.Popen(cmd, cwd=wd,
                                    preexec_fn=set_pdeathsig(signal.SIGTERM)))
    time.sleep(slp)

while True:
    time.sleep(10)
