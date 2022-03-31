# Use Case

There's useful background in the [README](../README.md)

Lazydoro only has one use case. I refer to the primary actor as 'The Writer' - a person who wants to write some 
text or some code.

The assumption is that the system can tell if the writer is at work simply by detecting if they 
are at their desk.



## Use Case - Writer completes a pomodoro cycle

Primary Actor:          The writer
Trigger:                The writer wants to do some writing
Main Success Scenario:
1. Lazydoro indicates that it is ready to start a pomodoro
2. The writer arrives at their desk
3. Lazydoro shows that it has seen the writer
4. Lazydoro notifies the writer every five minutes
5. Lazydoro notifies the writer when the pomodoro time is over
6. The writer leaves their desk for a break
7. Lazydoro shows the passage of each minute of the break
8. Lazydoro notifies the writer when the break is over
Extensions:
4a The writer leaves early:
    1 Lazydoro ends the current pomodoro and starts a new pomodoro if the user returns.
5a. The writer continues working in break time:
    1 Lazydoro notifies the user that the break is overdue
    2 When the writer leaves Lazydoro proceeds to step 5
6a. The writer arrives before the break is over:
    1 Lazydoro starts a new pomodoro



