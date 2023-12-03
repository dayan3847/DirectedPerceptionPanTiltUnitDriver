Check if the device is connected:

```sh
lsusb | grep serial
```

Example:

``` 
Bus 001 Device 014: ID 1a86:7523 QinHeng Electronics CH340 serial converter
```

Change the permissions of the device:

```sh
sudo chown 1000:1000 /dev/ttyUSB0 
```

Check if the permissions are changed:

```sh
ll /dev/ttyUSB0 
```
