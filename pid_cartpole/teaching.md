# an idea for using cartpole as a way to teach programming

start with an empty file. create a series of prompts and "hints" (but better WC so people don't feel guilty using them) to go through implementing a PID controller for cartpole and allowing user input 

don't look up code samples that directly implement one of the steps. this is a common challenge, but real robotics ones wont be. looking up and copying code without understanding what it does and how you might write it yourself doesn't help you learn as much. Feel free to look up code samples that are different from the exact problem though! (eg. stack overflow often has code samples that show how to use a library/function)

types of hints: 
- relevant information gained by experience (eg. gym uses pygame as a backend, so that's where we need to capture keystrokes from)
- big picture (this is the conceptual path to achieving the goal)
- high level steps (eg. install python from python.org. )
- relevant documentation (link to documentation or stack overflow so they don't have to go digging)
- solution code snippet / specific steps 

possible levels:
- get the code onto your computer
- get cartpole running
- create a PID loop
- (optional) create a function that simulates a controller many times to get an objective score metric
- tune the PID loop
- (optional) add user input 
    - let the user play the game themselves, see https://github.com/openai/gym/blob/master/gym/utils/play.py
    - add PID to the user input, so that the user controls the cart position and the PID loop ensures the stick stays balanced

