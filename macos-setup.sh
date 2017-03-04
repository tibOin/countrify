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
    brew install tor
    echoVert "Tor is now installed"
  fi
}

function checkBrew {
  echoOrange "Verifying Homebrew installation..."
  if hash brew 2>/dev/null; then
    echoVert "Homebrew is installed!"
    checkTor
  else
    echoOrange "Installing Homebrew"
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    echoVert "Homebrew is now installed."
    checkTor
  fi
}

echo "This script needs to be executed as root : executing sudo -v"
sudo -v

checkBrew

echoOrange "Ensuring pip is up-to-date"
sudo -H pip install --upgrade pip
echoVert "Done."

echoOrange "Installing Stem..."
sudo -H pip install stem
echoVert "Done."

echoOrange "Installing PycURL..."
sudo -H pip install pycurl
echoVert "Done."
echoJaune "PycURL installation might prompt an error but is still usable"

echoVert "You can now use : $(tput setaf 14)python countrify.py [desired country]$(tput sgr0)"
echoVert "Try $(tput setaf 14)python countrify.py $(tput setaf 10)to display help message"
