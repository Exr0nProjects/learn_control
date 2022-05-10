import gym
from time import monotonic
env = gym.make('CartPole-v1')

FRAMERATE = 30

def simulate(env):
    tot_score = 0
    prev_frame_timestamp = monotonic()

    env.reset()
    while True:
        env.render()
        if monotonic() - prev_frame_timestamp < 1/FRAMERATE: continue
        prev_frame_timestamp = monotonic()

        action = 0 # 0 or 1

        state, score, done, _ = env.step(action) # take a random action
        tot_score += score

        if done:
            input(f'Simulation ended. Total score: {tot_score}')
            break

for i in range(20):
    simulate(env)
env.close()

