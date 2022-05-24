#!/bin/bash
sudo useradd -m "$1" -p "$2" -s "/bin/bash"
if [ ! -d "/home/$1" ]; then
        sudo mkdir -p /home/$1
        sudo chown -R $1:$1 /home/$1
fi
# sudo usermod -aG sudo $1
# sudo echo "${1} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
