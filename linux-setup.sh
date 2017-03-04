#!/usr/bin/env bash

function echoOrange {
  echo "$(tput setaf 214)$1$(tput sgr0)"
}

function echoVert {
  echo "$(tput setaf 10)$1$(tput sgr0)"
}

function echoRouge {
  echo "$(tput setaf 9)$1$(tput sgr0)"
}

function echoJaune {
  echo "$(tput setaf 11)$1$(tput sgr0)"
}

function checkTor {
  echoOrange "Verifying Tor installation..."
  if hash tor 2>/dev/null; then
    echoVert "Tor is installed!"
  else
    echoOrange "Installing Tor..."
    apt-get install tor
    echoVert "Tor is now installed"
  fi
}

checkTor

echoOrange "Ensuring pip is up to date"
sudo -H pip install --upgrade pip
echoVert "Done."

echoOrange "Installing stem"
sudo -H pip install stem
echoVert "Done."

echoOrange "Installing pycurl"
sudo -H pip install pycurl
echoVert "Done."

echoVert "You can now use : $(tput setaf 14)python countrify.py [desired country]$(tput sgr0)"
echoVert "Try $(tput setaf 14)python countrify.py $(tput setaf 10)to display help message"
