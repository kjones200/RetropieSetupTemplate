#!/bin/bash

import os
from shutil import move

if os.path.exists('/Users/kenneth/projects/RetropieSetupTemplate/root/boot/config.txt.bak'):
    move('/Users/kenneth/projects/RetropieSetupTemplate/root/boot/config.txt.bak',
         '/Users/kenneth/projects/RetropieSetupTemplate/root/boot/config.txt')

if os.path.exists('/Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all/retroarch.cfg.bak'):
    move('/Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all/retroarch.cfg.bak',
         '/Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all/retroarch.cfg')
