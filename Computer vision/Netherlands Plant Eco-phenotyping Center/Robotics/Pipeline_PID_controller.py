# Importing the libraries
from simple_pid import PID
import time
from ot2_gym_wrapper import OT2Env
import numpy as np
import pandas as pd
import time

# Importing the coordinates
coordinates = pd.read_csv("Final_pipeline_coordinates.csv")

# Turning the coordinates into a numpy array
coordinates.columns = ['id', 'x', 'y', 'z']

# Convert DataFrame to a list of tuples
coordinates_list = list(coordinates.itertuples(index=False, name=None))

# Importing the environment
env = OT2Env(render=True)

# Creating the PID controllers for each axis
pid_controller_x = PID(Kp=15, Ki=0, Kd=0)
pid_controller_y = PID(Kp=15, Ki=0, Kd=0)
pid_controller_z = PID(Kp=15, Ki=0, Kd=0)

# Creating a dictionary to store the goal position and observation
goal_and_observation = {}

# Creatin a variable to store the error
overall_error = 0

# Starting the timer
start = time.time()

for coordinate in coordinates_list:
    # Reseting the environment
    observation, info = env.reset()

    # Setting the goal position
    goal_position = np.array([coordinate[1], coordinate[2], coordinate[3]], dtype=np.float32)
    
    env.goal_position = goal_position

    # Setting the goal position for each axis
    pid_controller_x.setpoint = goal_position[0]
    pid_controller_y.setpoint = goal_position[1]
    pid_controller_z.setpoint = goal_position[2]

    # Setting termination and truncation false
    terminated = False
    truncated = False

    # Setting the epoch to 0 to start the loop
    epoch = 0

    # Looping through 500 epochs
    for i in range(10000):

        # Incrementing the epoch
        epoch += 1

        # Getting the actions for each axis
        action_x = pid_controller_x(observation[0])
        action_y = pid_controller_y(observation[1])
        action_z = pid_controller_z(observation[2])

        # Creating the action array
        action = np.array([action_x, action_y, action_z])

        # Taking a step in the environment
        observation, _, terminated, truncated, _ = env.step(action)

        # Getting the distance between the pipette and the goal
        distance = observation[3:] - observation[:3] # goal position - pipette position

        # Calculating the error between the pipette and the goal
        error = np.linalg.norm(distance)

        if error < 0.001:
            # Adding the error to the overall error
            overall_error += error
            break
        
        # Printing the epoch, goal position and observation
        print(f"Epoch: {epoch}")
        print(f"Goal_position: {goal_position}")
        print(f"Observation: {observation}")

        # Adding a delay
        time.sleep(0.0003)

# Ending the timer
end = time.time()

# Printing the time taken
print(f"Time taken: {end - start}")

# Calculating and printing the average error
average_error = overall_error / len(coordinates_list)
print(f"Average error: {average_error}")