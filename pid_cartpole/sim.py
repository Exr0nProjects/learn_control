import gym
from time import monotonic
from math import pi
import numpy as np
from tqdm import tqdm
env = gym.make('CartPole-v1')
# TODO: why not working? \/
env.x_threshold = 100
env.theta_threshold_radians = pi

FRAMERATE = 30
sp, P, I, D = 0, 0.09, 0.0013, 0.80
sp, P, I, D = 0.1, 0.09, 0.0343, 0.80

inturrupt = False

def generate_until_inturrupt():
    num = 0
    while True:
        num += 1
        yield num
        if inturrupt: return

class CartPoleAnimated:
    def __init__(self, env, render=True):
        self.env = env
        self.should_render = render
        self.reset()

    def reset(self):
        global interrupt
        inturrupt = False
        self.state = self.env.reset()
        self.tot_score = 0
        self.accumulated_error = 0
        self.prev_error = 0

    def step(self, frame_n):
        if self.should_render: self.draw()

        pos, vel, angle, a_vel = self.state

        sp = 0      # set point
        pv = angle  # percieved (sensor) value
        error = sp - pv

        signal = P * error + I * self.accumulated_error + D * (error - self.prev_error)

        self.accumulated_error += error
        self.prev_error = error

        action = int(signal < 0)

        # running the environment
        self.state, score, done, _ = env.step(action) # take a random action
        self.tot_score += score
        # TODO: what do i do with done? global interrupt var?
        # TODO: what to return for the render thingy?


    def draw(self):
        self.env.render()

def simulate(env, render=True):
    tot_score = 0
    prev_frame_timestamp = monotonic()

    accumulated_error = 0
    prev_error = 0

    state = env.reset()
    while True:
        if render: env.render()
        if render and monotonic() - prev_frame_timestamp < 1/FRAMERATE: continue
        prev_frame_timestamp = monotonic()



        # the algorithm
        pos, vel, angle, a_vel = state

        pv = angle
        error = sp - pv

        signal = P * error + I * accumulated_error + D * (error - prev_error)

        accumulated_error += error
        prev_error = error

        action = int(signal < 0) # 0 or 1
        if render: print(state, signal, action)



        # running the environment
        state, score, done, _ = env.step(action) # take a random action
        tot_score += score

        if done:
            if render: input(f'Simulation ended. Total score: {tot_score}')
            break
    return tot_score

simulate(env)
scores = [simulate(env, render=False) for _ in tqdm(range(1000), leave=False)]
print(f'sp: {sp}, {P} {I} {D}         average score: {sum(scores)/len(scores):.2f}, standard dev {np.std(scores):.2f}')
env.close()

