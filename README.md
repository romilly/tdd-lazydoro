# Lazydoro Mk V

Lazydoro is a small device that helps writers and programmers to practice the
[Pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique).

![Lazydoro Mk V hardware](docs/img/lazydoro.jpg)

If you're writing text or code, you probably work at a desk. Lazydoro can see if you're at your desk.

When you sit down it assumes you're starting a Pomorodo. It will show you how
time is passing and will remind you 
to tak a break when the pomodoro is complete.

Lazydoro assumes that you will get up from your desk when taking a break.
It will start timing the break when you leave your desk, and it will buzz 
to alert you when the break time is over.

When you've completed a pomodoro/break cycle, Lazydoro will be ready for
you to start again.

I documented this behaviour more formally in [a use case](docs/use-case.md).

The current version of Lazydoro Mk 5 is driven by a Raspberry Pi Zero or a 
Raspberry Pi Pico. Other models could be used instead.

The additional hardware for the Pi is described [here](docs/hardware.md).

Docs for the Pico hardware are coming soon.

### Installing the software on a Pi

I will package Lazydoro when it's stable. Until then, once you have built the hardware,

1. Clone this repository on the Raspberry Pi.
2. Install the required software:
```shell
curl https://get.pimoroni.com/blinkt | bash 
pip3 install adafruit-circuitpython-vl53l0x
pip3 install PyHamcrest # needed for testing

```

### Running the software in the Pi

```shell
cd <project root>/src
python3 run.py
```

You can stop it by typing `crtl-C`.


### 

## Future plans

I'm now using this project, and will start blogging about the implementation.

As of today (2 April 2022) automated test coverage is at 97%.
That's a high figure for an embedded Python application!





