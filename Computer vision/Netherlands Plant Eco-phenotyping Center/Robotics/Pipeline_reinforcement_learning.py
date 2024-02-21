import time
import gymnasium as gym
from stable_baselines3 import PPO
from ot2_gym_wrapper import OT2Env
import numpy as np
import pandas as pd

# Importing the coordinates
coordinates = pd.read_csv("Final_pipeline_coordinates.csv")

# Turning the coordinates into a numpy array
coordinates.columns = ['id', 'x', 'y', 'z']

# Convert DataFrame to a list of tuples
coordinates_list = list(coordinates.itertuples(index=False, name=None))

terminated = False
truncated = False

env = OT2Env(render=True, max_steps=1000)
model = PPO.load(r"C:\Users\daraz\Documents\GitHub\2023-24b-fai2-adsai-DanielElek223838\3. Reinforcement Learning\model.zip", env=env)
obs, info = env.reset()

# Starting the timer
start = time.time()

# Creating a variable to store the error
overall_error = 0

for i, coordinate in enumerate(coordinates_list):
      
    # Setting the goal position
    env.goal_position = np.array([coordinate[1], coordinate[2], coordinate[3]], dtype=np.float32)

    # Converting the observation to a NumPy array
    obs = np.array(obs)

    # Geting the action from the model
    action, _states = model.predict(obs, deterministic=True)

    # Taking action in environment
    obs, reward, terminated, truncated, info = env.step(action)

    # Getting the distance between the pipette and the goal position
    distance = np.linalg.norm(obs[:3] - obs[3:])

    # Calculating the error
    error = np.linalg.norm(distance)

    # Adding the error to the overall error
    overall_error += error

    # Printing the distance
    print(distance)

    # Checking if the goal is reached
    if distance < 0.001:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        terminated = True

env.close()

# Ending the timer
end = time.time()

# Printing the time taken
print(f"Time taken: {end - start}")

# Calculating and printing the average error
average_error = overall_error / len(coordinates_list)
print(f"Average error: {average_error}")