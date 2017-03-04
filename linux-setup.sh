#!/usr/bin/env bash

echo "Installing Tor\n"
apt-get install tor

echo "\nEnsuring pip is up to date\n"
sudo -H pip install --upgrade pip

echo "\nInstalling stem\n"
sudo -H pip install stem

echo "\nInstalling pycurl\n"
sudo -H pip install pycurl
