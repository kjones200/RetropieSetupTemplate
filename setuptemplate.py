#!/usr/bin/env python

from subprocess import call

########################################################################################################################
# CONFIGURATION SECTION                                                                                                #
########################################################################################################################

# This is the working directory for setup script
WORKING_DIR = '/home/pi/'

# Username and repository name.  This will used to generate a URL for downloading the repository
REPO_USERNAME = "git_username"
REPO_NAME = "reponame"

# List of files requiring modification.  List is comprised of dictionary containing the filename
# location, search tet, and the modification to apply.  For example ('file.txt', '/home/pi/')
MOD_LIST = [
    {'filename': 'config.txt', 'location': '/boot/', 'search': 'enable_uart=0', 'modification': 'enable_uart=1'},

]

# List of file that need to be copied/replaced.  List is comprised of tuples containing the filename
# and location.  For example ('file.txt', '/home/pi/')
COPY_LIST = [
    ('autostart.sh', '/opt/retropie/configs/all/'),

]

########################################################################################################################
# EXECUTION SECTION                                                                                                    #
########################################################################################################################

# Change to the working director before doing anything
call('cd ' + WORKING_DIR)

# Update dependency list and download necessary dependencies.  Uses the -y option for no prompts
call('sudo apt-get update && sudo apt-get -y install python-dev python-pip python-gpiozero')

# Downloads necessary python modules dependencies.  Use 'yes' for installation without prompts.
call('yes | sudo pip install psutil pyserial')

# Download the repository
call('git clone https://github.com/%s/%s.git' % (REPO_USERNAME, REPO_NAME))
call('cd %s' % REPO_NAME)  # move into repo directory
