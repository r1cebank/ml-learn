#!/bin/bash

function install {
    echo installing "$1"
    shift
    apt-get -y install "$@" >/dev/null 2>&1
}


function pip_install {
    echo installing "$1"
    shift
    pip install "$@" >/dev/null 2>&1
}


echo "updating package information"
apt-get -y update >/dev/null 2>&1


# Install build tools
install 'build dependencies' build-essential git curl vim libcairo2-dev libatlas-base-dev libav-tools nfs-common portmap python-dev python-pip

pip_install  'upgrade pip' --upgrade pip
pip_install 'python libraries' -r /vagrant/requirements.txt