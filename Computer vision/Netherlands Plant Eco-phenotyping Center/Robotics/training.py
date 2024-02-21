import gymnasium as gym
from stable_baselines3 import PPO
from ot2_gym_wrapper import OT2Env
from clearml import Task
import argparse
import os
import wandb
from wandb.integration.sb3 import WandbCallback

def main():
    # Create the environment
    env = OT2Env(render=False)
    
    os.environ['WANDB_API_KEY'] = '931ed39263a55b4787b53054be2b8757e4ffa75d'
    run = wandb.init(project="Task11", sync_tensorboard=True)
    wandb_callback = WandbCallback(model_save_freq=1000,
                                model_save_path=f"models/{run.id}",
                                verbose=2)

    # Instantiate the agent
    model = PPO("MlpPolicy", env, verbose=1,
                learning_rate=args.learning_rate, 
                batch_size=args.batch_size, 
                n_steps=args.n_steps, 
                n_epochs=args.n_epochs,
                tensorboard_log=f"runs/{run.id}")

    model.learn(total_timesteps=5000000, callback=wandb_callback, progress_bar=True)
    model.save("ot2_model_task_11_Daniel")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--learning_rate", type=float, default=0.001)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--n_steps", type=int, default=2048)
    parser.add_argument("--n_epochs", type=int, default=10)

    args = parser.parse_args()
    main()