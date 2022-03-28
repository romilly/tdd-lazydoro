# Project journal for tdd-lazydoro

I'm going to have another shot at creating an Object-Oriented, tested implementation of lazydoro using a Python 
interpretation of the GOOS approach.

Here's how it works:

When the lazydoro is waiting and no-one arrives the display is clear. (WAITING)
When the lazydoro is waiting or a break has elapsed and someone arrives the lazydoro will show a blue led and then an extra blue led for each 
three minutes (event WORKING_TICK) until the pomododo is over. (WORKING)
If someone leaves before the pomodoro is over, the display will clear and the lazydoro will wait until someone 
arrives. (WAITING)
If someone stays until the 25 minutes is up, the pomodoro will show all red leds until the person leaves to start their 
break. (BREAK_DUE)
If someone leaves after the time is up, the timer will display a green led and then an extra green led for every 
minute. (event = BREAK_TICK, start = ON_BREAK)
When the break has reached 5 minutes the display will show yellow leds. (BREAK_OVER)



    





