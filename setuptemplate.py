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

# List of files requiring modification.  List is comprised of dictionary containing the filename
# location, search tet, and the modification to apply.  For example ('file.txt', '/home/pi/')
MOD_LIST = [
    {'filename': 'config.txt', 'location': '/boot/', 'search': 'enable_uart=0', 'modification': 'enable_uart=1'},

]

# List of file that need to be copied/replaced.  List is comprised of tuples containing the filename
# and location.  For example ('file.txt', '/home/pi/')
# NOTE: If file is listed here, it should be included in the repository
COPY_LIST = [
    ('autostart.sh', '/opt/retropie/configs/all/'),

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
    #    exit(code)
    
    # Download the repository
    # Check for repo and delete it to prevent errors when downloading due to repo already existing
    if os.path.exists(os.path.join(os.getcwd(), REPO_NAME)):
        shutil.rmtree(os.path.join(os.getcwd(), REPO_NAME), ignore_errors=True)
    
    run_process(['git', 'clone https://github.com/%s/%s.git' % (REPO_USERNAME, REPO_NAME)])
    os.chdir(REPO_NAME) # move into repo directory
    
    # Modify retroarch.cfg
    
    # Modify config.txt


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

def find_modifiy(filename, search, mod):
    


if __name__ == '__main__':
    main()
