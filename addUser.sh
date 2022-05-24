#!/bin/bash
sudo useradd -m "$1" -p "$2" -s "/bin/bash"
if [ ! -d "/home/$1" ]; then
        sudo mkdir -p /home/$1
        sudo chown -R $1:$1 /home/$1
fi
command=$(echo sudo su $1 -c "\"mkdir -p /home/$1/.ssh && touch /home/$1/.ssh/authorized_keys && chmod 600 /home/$1/.ssh/authorized_keys && chmod 700 /home/$1/.ssh && echo user created\"")
/bin/bash -l -c "$command"
# sudo usermod -aG sudo $1
# sudo echo "${1} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
