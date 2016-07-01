# This file is part of CAT-SOOP
# Copyright (c) 2011-2016 Adam Hartz <hartz@mit.edu>

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see
# <https://www.gnu.org/licenses/agpl-3.0-standalone.html>.

import traceback

from . import loader
from . import dispatch
from . import base_context

def html_format(string):
    """
    Returns an HTML-escaped version of the input string, suitable for
    insertion into a <pre> tag
    """
    for x, y in (('&', '&amp;'), ('<', '&lt;'), ('>', '&gt;'), ('\t', '    '),
                 (' ', '&nbsp;')):
        string = string.replace(x, y)
    return string


def clear_info(context, text):
    """
    Clear sensitive information from a string
    """
    text = text.replace(
        context.get('cs_fs_root', base_context.cs_fs_root), '<CATSOOP ROOT>')
    text = text.replace(
        context.get('cs_data_root', base_context.cs_data_root), '<DATA ROOT>')
    for i, j in context.get('cs_extra_clear', []):
        text = text.replace(i, j)
    return text


def error_message_content(context):
    """
    Returns an HTML-ready string containing an error message.
    """
    return html_format(clear_info(context, traceback.format_exc()))


def do_error_message(context, msg=None):
    """
    Display an error message
    """
    new = dict(context)
    loader.load_global_data(new)
    if 'cs_user_info' not in new:
        new['cs_user_info'] = {}
        new['cs_username'] = None
    if 'cs_handler' in new:
        del new['cs_handler']
    m = msg if msg is not None else error_message_content(context)
    new['cs_content'] = '<textarea rows=20 cols=110>ERROR:\n%s</textarea>' % m
    e = ': <font color="red">ERROR</font>'
    new['cs_header'] = new.get('cs_header', '') + e
    new['cs_content_header'] = 'An Error Occurred:'
    s, h, o = dispatch.display_page(new)
    return ('500', 'Internal Server Error'), h, o

