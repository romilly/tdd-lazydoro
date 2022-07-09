# OO version of the NeoPixel code

import array, time
from machine import Pin
import rp2

BLACK = (0, 0, 0)
RED = (255, 0, 0)

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


class NeoPixel:
    def __init__(self, pin=16, count=8, brightness = 0.2):
        self.pin = pin
        self.count = count
        self.brightness = brightness
        self.pixels = array.array("I", [0 for _ in range(self.count)])
        self.sm = rp2.StateMachine(0,
                                   ws2812,
                                   freq=8_000_000,
                                   sideset_base=Pin(self.pin))
        self.sm.active(1)

    def set(self, i, color):
        self.pixels[i] = (color[1] << 16) + (color[0] << 8) + color[2]

    def show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self.count)])
        for i, c in enumerate(self.pixels):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g << 16) + (r << 8) + b
        self.sm.put(dimmer_ar, 8)
        time.sleep_ms(10)

    def clear(self):
        for i in range(self.count):
            self.set(BLACK)





