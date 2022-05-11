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
P, I, D = 0.09, 0.0013, 0.80
# P, I, D = 0.09, -0.0012, 0.13
# P, I, D = 0.05, -0.0017, 0.13
# P, I, D = 0.048, -0.003, 0

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

        sp = 0
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
# scores = [simulate(env, render=False) for _ in tqdm(range(1000), leave=False)]
print(f'{P} {I} {D}         average score: {sum(scores)/len(scores):.2f}, standard dev {np.std(scores):.2f}')
env.close()

