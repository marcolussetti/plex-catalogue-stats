#!/usr/bin/env bash
# pip install pyinstaller

rm *.pyc

# Linux binary
if [ "$1" == "linux" ]; then
    pyinstaller plex-stats.py --onefile --noconfirm

# Windows binary
elif [ "$1" == "windows" ]; then
    pyinstaller plex-stats.py --onefile --noconfirm --console --version "1.0" 

# Mac binary
elif [ "$1" == "macos" ]; then
    pyinstaller plex-stats.py --onefile --noconfirm --target-architecture "arm64"

fi