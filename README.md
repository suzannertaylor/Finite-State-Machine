# Finite State Automata
The automata will give you the remainder when dividing a number by 3. This is a python 3 application

## Requirements
Python 3.x

## Run
On the command line type

 python statemachine.py

 ## Example

Example 1

for input string 110
```
the machine will go as follows.
Initial state = S0, Input = 1, result state = S1
Current state = S1, Input = 1, result state = S0
Current state = S0, Input = 0, result state = S0
```

Output for state S0 = 0

Example 2

for input string 1010
```
the machine will go as follows.
Initial state = S0, Input = 1, result state = S1
Current state = S1, Input = 0, result state = S2
Current state = S2, Input = 1, result state = S2
Current state = S2, Input = 0, result state = S1
```
Output for state S1 = 1