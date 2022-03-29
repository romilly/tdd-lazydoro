from tdd_lazydoro.adapters import OutputAdapter
from tdd_lazydoro.hw_ui import BlinktDisplay
from tdd_lazydoro.pomodoro import Pomodoro
from time import sleep

ui = BlinktDisplay()
pomodoro = Pomodoro(ui)
output_adapter = OutputAdapter(ui)
pomodoro.add_observer(output_adapter)
for i in range(25):
    pomodoro.minute_has_passed()
    sleep(1)