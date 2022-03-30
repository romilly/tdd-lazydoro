# Lazydoro Mk II

**NB** This project works but is under active development.
_Expect the code to change over the next few days!_

Lazydoro is a small device that helps writers and programmers to practice the Pomodoro technique.

![Lazydoro Mk II hardware](docs/img/lazydoro.jpg)

If you're writing text or code, you probably work at a desk. Lazydoro can see if you're at your desk.

When you sit down it assumes you're starting a Pomorodo. It will show you how time is passing and will remind you 
to tak a break when the pomodoro is complete.

Lazydoro assumes that you will get up from your desk when taking a break.
It will start timing the break when you leave your desk, and it will alert you when the break time is over.

When you've completed a pomodoro/break cycle, Lazydoro will be ready for you st start again.

I documented this behaviour more formally in [a use case](docs/use-case.md).

The current version of Lazydoro Mk II is driven by a Raspberry Pi Zero. Other models of Pi could be used instead.

The additional hardware  is described [here](docs/hardware.md)

## Installing the software

I will package Lazydoro when it's stable. Until then

1. Clone this repository on the Raspberry Pi.
2. Install the required software:
```shell
curl https://get.pimoroni.com/blinkt | bash 
pip3 install adafruit-circuitpython-vl53l0x
pip3 install PyHamcrest # needed for testing

```

## Running the software

```shell
cd <project root>/src
python3 run.py
```

You can stop it by typing `crtl-C`.


