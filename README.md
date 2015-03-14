# cubietruck-button

This python script wakes up a given local computer via wake on lan, when a button is pressed.

## Configure GPIO pin ##

The sunxi-tools ``bin2fex`` and ``fex2bin`` must be installed for this.

	$ bin2fex /boot/cubietruck.bin > /path/to/script.fex

Edit the GPIO config in the generated fex file. Add/Edit the following lines in the GPIO section:

	gpio_num = 3
	gpio_pin_3 = port:PG00<0><1><default><default>

For the meaing of the pin values, see http://linux-sunxi.org/Fex_Guide

Save and write the edited fex back to the bin file

	$ fex2bin /path/to/script.fex > /boot/cubietruck.bin

These settings are applied after reboot.

## Static wireless configuration ##

The file ``/etc/network/interfaces`` must look as follows:

	auto wlan0
		allow-hotplug wlan0
		iface wlan0 inet static
			address 192.168.0.60
			netmask 255.255.255.0
			gateway 192.168.0.1
		wpa-ssid SSID_NAME
		wpa-psk xxxxxxxxxxx

	auto lo
		iface lo inet loopback

After editing, restart the network service:

	$ sudo service networking restart


## Autostart ##

To start the python script at boot:

	$ sudo crontab -e

Add line: ``@reboot python /path/to/button.py &``

and save crontab
