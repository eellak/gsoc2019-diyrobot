#!/bin/bash
#Instructions from https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md
sudo apt install dnsmasq hostapd
sudo echo "interface wlan0" >> /etc/dhcpcd.conf
sudo echo "static ip_address=192.168.4.1/24" >> /etc/dhcpcd.conf
sudo echo "nohook wpa_supplicant" >> /etc/dhcpcd.conf
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo touch /etc/dnsmasq.conf
sudo echo "interface=wlan0" >> /etc/dnsmasq.conf
sudo echo "wlan0" >> /etc/dnsmasq.conf
sudo echo "dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h">>/etc/dnsmasq.conf
sudo systemctl reload dnsmasq
sudo mv hostapd.conf /etc/hostapd/
sudo sed -i 's/#DAEMON_CONF/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/g' /etc/default/hostapd
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf 
sudo iptables -t nat -A  POSTROUTING -o eth0 -j MASQUERADE
sudo sed -i 's/exit 0/iptables-restore < \/etc\/iptables.ipv4.nat/g' /etc/rc.local
sudo echo "exit 0" >> /etc/rc.local
sudo reboot 

