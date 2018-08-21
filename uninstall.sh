#!/bin/sh
if [ -f "/opt/wordgen/wordgen.py" ]; then
sudo rm -rf /opt/wordgen
sudo rm -rf /usr/bin/wordgen
echo uninstallation completed
else
echo programm is not installed please install it from install.sh file
fi
