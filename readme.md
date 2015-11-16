# Serial Button Manager

Have you ever wanted to use a physical button to control the state of something on a computer?  Have you ever noticed that empty DB9 serial port connector on the back of said computer, and thought about putting something in that?  In the unlikely event that both of the above are true, this is the project for you.

## Installation

Install from pip

```
pip install serial-button-manager
```

## Use

Just run `serial-button-manager` with two arguments: the path to the `/dev/` device for the serial port you're using, and the name of a SystemV/Upstart service you'd like to control.

If you were using the device `/dev/ttyS0` and the service `networking`, you could run:

```
serial-button-manager /dev/ttyS0 networking
```

## Making a Button

![](http://coddingtonbear-public.s3.amazonaws.com/github/serial-button-manager/DB9-Switch.png)

Serial connectors include a "Carrier Detection" feature that you can trigger by bridging pins #1 and #4 on a DB9 serial connector.  Your goal: to solder a toggle switch to a DB9 connector in such a way that when the switch is closed, those two pins are bridged, and when the switch is open, those two pins are not bridged.

In my case, the end results were as follows:

![](http://coddingtonbear-public.s3.amazonaws.com/github/serial-button-manager/IMG_2841.JPG)
![](http://coddingtonbear-public.s3.amazonaws.com/github/serial-button-manager/IMG_2843.JPG)

In the connector I made, I used a long standard stereo cable and stereo connectors to make it possible for me to mount the switch far away from the serial port, and although the above picture does not show it, these were later encased in some [instamorph](https://www.instamorph.com/) to prevent damage or shorting.
