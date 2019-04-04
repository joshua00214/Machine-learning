import tensorflow as tf
import gym
import gym_maze
env = gym.make("Maze-v0")
'''
env.reset()
for _ in range(0, 10):
    env.render()
    
    env.step(env.action_space.sample())
#import maze
'''
#env = gym.make("CartPole-v0")
env.reset()
for i_episode in range(10):
    obs = env.reset()
    for t in range(25):
        env.render()
        print(obs)
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        if done:
            print("finished after {} time".format(t+1))
            break


#env = gym.make("CartPole-v0")
#print(env.action_space)

# discrete(2) 
# the discrete space gives a fixed range of pos numbers, so actions from this are either 0 or 1

#  print(env.observation_space)

# box(4, )
# box space gives a n-th dimension box, in this case a 4th diminsinanol box.
# any valid value with be an array of 4 numbers.
#print(env.observation_space.high) #[4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38] highest values allowed in the box
#print(env.observation_space.low) # [-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38] lowest values allowed in the box

#space = gym.spaces.Discrete(8) #values 0 - 7 possible to create new spaces
#for _ in range(0, 100):
    #print(space.sample()) #.sample creates a value from the space


# steps return observation, reward, done, and info



#THE REGISTRY

#print(gym.envs.registry.all()) # gives a list of all possible env I can use.

#when adding new envirments to the registry, register() them and use it with gym.make
#gym.register("gym_foo:foo-v0")
#mine = gym.make("gym-soccer")
