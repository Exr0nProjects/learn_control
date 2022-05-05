import gym
env = gym.make('CartPole-v1')
env.reset()

tot_score = 0
while True:
    env.render()

    action = 0 # 0 or 1

    state, score, done, _ = env.step(action) # take a random action
    tot_score += score

    if done:
        input(f'Simulation ended. Total score: {tot_score}')
        break
env.close()

