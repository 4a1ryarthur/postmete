#!/bin/bash

# Install PyQt5
sudo apt-get update
sudo apt-get install -y python3-pyqt5

# Delete the installer script file
rm "$0"
