#!/bin/bash



mv -v /Users/kenneth/projects/RetropieSetupTemplate/root/boot/config.txt.bak /Users/kenneth/projects/RetropieSetupTemplate/root/boot/config.txt

mv -v /Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all/retroarch.cfg.bak /Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all/retroarch.cfg

rm -v /Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all/autostart*
rm -v /Users/kenneth/projects/RetropieSetupTemplate/root/opt/retropie/configs/all/runcommand*
rm -v /Users/kenneth/projects/RetropieSetupTemplate/root/home/pi/NESPi/script*
