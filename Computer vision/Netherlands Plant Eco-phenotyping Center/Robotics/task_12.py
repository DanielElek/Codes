# Importing the libraries
from simple_pid import PID
import time
from ot2_gym_wrapper import OT2Env
import numpy as np

# Importing the environment
env = OT2Env()

# Reseting the environment
observation, info = env.reset()

# Creating the PID controllers for each axis
pid_controller_x = PID(Kp=15, Ki=0, Kd=0)
pid_controller_y = PID(Kp=15, Ki=0, Kd=0)
pid_controller_z = PID(Kp=15, Ki=0, Kd=0)

# Setting the goal position
goal_position = np.array([np.random.uniform(-0.1872, 0.253),
                          np.random.uniform(-0.1705, 0.2195),
                          np.random.uniform(0.1693, 0.2895)], dtype=np.float32)

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
for i in range(700):

    # Breaking the loop if terminated
    if terminated:
        break

    # Incrementing the epoch
    epoch += 1

    # Resetting the environment if truncated
    if truncated:
        observation, info = env.reset()

        # Resetting the goal positions for each axis if truncated
        pid_controller_x.setpoint = goal_position[0]
        pid_controller_y.setpoint = goal_position[1]
        pid_controller_z.setpoint = goal_position[2]

    # Getting the actions for each axis
    action_x = pid_controller_x(observation[0])
    action_y = pid_controller_y(observation[1])
    action_z = pid_controller_z(observation[2])

    # Creating the action array
    action = np.array([action_x, action_y, action_z])

    # Taking a step in the environment
    observation, _, terminated, truncated, _ = env.step(action)

    # Printing the epoch, goal position and observation
    print(f"Epoch: {epoch}")
    print(f"Goal_position: {goal_position}")
    print(f"Observation: {observation}")

    # Adding a delay
    time.sleep(0.0003)