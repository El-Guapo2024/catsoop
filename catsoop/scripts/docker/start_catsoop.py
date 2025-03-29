#!/usr/bin/env python3

# This file is part of CAT-SOOP
# Copyright (c) 2011-2019 by The CAT-SOOP Developers <catsoop-dev@mit.edu>
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
import logging
import catsoop
import catsoop.wsgi
import waitress

# Set up logging
LOGGER = logging.getLogger("cs")
logging.basicConfig(level=logging.INFO)

# Docker-specific paths and configuration
DOCKER_DATA_DIR = os.environ.get('CATSOOP_DATA_DIR', '/app/data')
DOCKER_CONFIG_DIR = os.environ.get('CATSOOP_CONFIG_DIR', '/root/.config/catsoop')
DOCKER_HOST = os.environ.get('CATSOOP_HOST', '0.0.0.0')
DOCKER_PORT = int(os.environ.get('CATSOOP_PORT', 7667))

cs_logo = r"""
\
/    /\__/\\
\__=(  o_O )=
(__________)
 |_ |_ |_ |_

  CAT-SOOP Docker Edition
"""

def setup_directories():
    """Set up necessary directories for CAT-SOOP in Docker environment"""
    # Create data directory
    os.makedirs(DOCKER_DATA_DIR, exist_ok=True)
    
    # Create checker database directories
    checker_db_loc = os.path.join(DOCKER_DATA_DIR, "_logs", "_checker")
    os.makedirs(checker_db_loc, exist_ok=True)
    for subdir in ("queued", "running", "results", "staging"):
        os.makedirs(os.path.join(checker_db_loc, subdir), exist_ok=True)
    
    # Create config directory
    os.makedirs(DOCKER_CONFIG_DIR, exist_ok=True)

def setup_configuration():
    """Set up CAT-SOOP configuration for Docker environment"""
    config_loc = os.environ.get('CATSOOP_CONFIG', 
                               os.path.join(DOCKER_CONFIG_DIR, 'config.py'))
    
    if not os.path.isfile(config_loc):
        LOGGER.error(f"Config file not found at {config_loc}")
        sys.exit(1)
    
    LOGGER.info(f"Using configuration from {config_loc}")
    os.environ["CATSOOP_CONFIG"] = config_loc

def setup_encryption():
    """Set up encryption for CAT-SOOP in Docker environment"""
    encryption_key = os.environ.get('CATSOOP_ENCRYPTION_KEY')
    if encryption_key:
        os.environ["CATSOOP_PASSPHRASE"] = encryption_key
        LOGGER.info("Encryption key set from environment variable")

def main():
    """Main function to start CAT-SOOP in Docker environment"""
    import catsoop.base_context as base_context
    import catsoop.loader as loader

    # Set up directories
    setup_directories()
    
    # Set up configuration
    setup_configuration()
    
    # Set up encryption
    setup_encryption()

    # Create WSGI app
    app = catsoop.wsgi.application

    # Start the server
    LOGGER.info(f"Starting CAT-SOOP server on {DOCKER_HOST}:{DOCKER_PORT}")
    waitress.serve(app, host=DOCKER_HOST, port=DOCKER_PORT)

def startup_catsoop():
    """Entry point for CAT-SOOP in Docker environment"""
    print(cs_logo)
    LOGGER.info(f"Starting CAT-SOOP in Docker environment")
    LOGGER.info(f"Data directory: {DOCKER_DATA_DIR}")
    LOGGER.info(f"Config directory: {DOCKER_CONFIG_DIR}")
    
    main()

if __name__ == "__main__":
    startup_catsoop() 