# Directed Perception `PAN TILT UNIT` Driver

<img alt="PAN TILT UNIT" src="./img/ptu_d46.png" width="400"/>

## Setup

Check if the device is connected:

```sh
lsusb | grep serial
```

Example:

``` 
Bus 001 Device 014: ID xxx:xxxx QinHeng Electronics CH340 serial converter
```

Change the permissions of the device:

```sh
sudo chown 1000:1000 /dev/ttyUSB0 
```

Check if the permissions are changed:

```sh
ll /dev/ttyUSB0 
```
