#!/usr/bin/env python

"""
Simply setup script to automate the process of setting up a retropie with various electronics kits.

Copyright (C) 2017 Kenneth A Jones II kenneth@nvnctechnology.com

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

Visit: https://www.facebook.com/groups/miniNESbuilders/
"""

import os
import sys
import subprocess
import logging
import shutil

########################################################################################################################
# CONFIGURATION SECTION                                                                                                #
########################################################################################################################

logging.basicConfig(filename="install.log",
                    filemode='w',
                    format='[%(levelname)-8s] %(message)s',
                    level=logging.DEBUG)

# This is the working directory for setup script
WORKING_DIR = '/Users/kenneth/projects/RetropieSetupTemplate/root/home/pi/'

# Username and repository name.  This will used to generate a URL for downloading the repository
REPO_USERNAME = "kjones200"
REPO_NAME = "testrepo"

# List of files requiring modifications.  List is comprised of dictionary containing the filename
# location, search tet, and the modification to apply.  For example ('file.txt', '/home/pi/')
MOD_LIST = [
    {'name'    : 'config.txt',
     'location': '/Users/kenneth/projects/RetropieSetupTemplate/root/boot',
     'mods'    : {'enable_uart': 'enable_uart=1'}
     },
    {'name'    : 'retroarch.cfg',
     'location': '/Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all',
     'mods'    : {'network_cmd_enable': 'network_cmd_enable = true',
                  'network_cmd_port'  : 'network_cmd_port = 55355'}
     },

]

# List of files that need to be copied/replaced.  List is comprised of dictionary containing the filename
# and location.  For example {'file.txt': '/home/pi/'}
# NOTE: If file is listed here, it should be included in the repository
COPY_LIST = [
    {'autostart.sh': '/opt/retropie/configs/all/'},
    {'runcommand-onstart.sh': '/opt/retropie/configs/all/'},
    {'runcommand-onend.sh': '/opt/retropie/configs/all/'},
    {'script.py': '/Users/kenneth/projects/RetropieSetupTemplate/root/home/pi/NESPi'},
]


########################################################################################################################
# EXECUTION SECTION                                                                                                    #
########################################################################################################################

def main():
    # Change to the working director before doing anything
    os.chdir(WORKING_DIR)
    
    # Update dependency list and download necessary dependencies.  Uses the -y option for no prompts
    # out,err = run_process(['sudo apt-get update'])
    # out, err = run_process (['sudo apt-get -y install python-dev python-pip python-gpiozero'])
    
    # Downloads necessary python modules dependencies.  Use 'yes' for installation without prompts.
    # code = run_process(['yes |', 'pip install psutil pyserial'])
    # if code != 0:
    #    sys.exit(code)
    
    # Download the repository
    # Check for repo and delete it to prevent errors when downloading due to repo already existing
    if os.path.exists(os.path.join(os.getcwd(), REPO_NAME)):
        shutil.rmtree(os.path.join(os.getcwd(), REPO_NAME), ignore_errors=True)
    
    run_process(['git', 'clone https://github.com/%s/%s.git' % (REPO_USERNAME, REPO_NAME)])
    os.chdir(REPO_NAME)  # move into repo directory
    
    # Perform modifications to files defined in
    for f in MOD_LIST:
        mod_file(f)


def run_process(cmd):
    p = subprocess.Popen(' '.join(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while p.poll() is None:
        l = p.stdout.readline()  # This blocks until it receives a newline.
        if l != "":
            print l
    # When the subprocess terminates there might be unconsumed output
    # that still needs to be processed.
    out = p.stdout.read()
    err = p.stderr.read()
    if p.returncode != 0:
        logging.error(err)
    return p.returncode


def copy_files(file):
    pass


def mod_file(file):
    src_path = os.path.join(file['location'], file['name'])
    dest_path = os.path.join(file['location'], 'temp_' + file['name'])
    
    try:
        # Check if file exists
        if not os.path.exists(src_path):
            logging.warning('File does not exist, nothing to modify')
            return  # File doesn't exist, nothing to modify
        
        # Write the contents of source file to a temporary file, while making modifications.  This done so that the
        # source file doesn't have to be read nto memory
        with open(src_path, 'r') as in_file, open(dest_path, 'w') as out_file:
            for line in in_file:
                for target, replacement in file['mods'].iteritems():
                    if target in line:
                        line = replacement + '\n'
                out_file.write(line)
        
        # Backup old source file by adding .bak extension, then rename temp file with source files name
        os.rename(src_path, src_path + '.bak')
        os.rename(dest_path, src_path)
    
    except:
        logging.error('Modifing file ' + src_path + ' failed')
        sys.exit(1)


if __name__ == '__main__':
    main()
