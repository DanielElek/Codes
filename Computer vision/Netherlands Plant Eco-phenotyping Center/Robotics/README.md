The environment setup consists of
- a ot_2_simulation_v6.urdf file which is the simulation we are working in
- a custom.urdf file which is the machine we teach
- a sim_class.py which sets up and controls the simulation
- a uvmapped_dish_large_comp.png which is the image of the petri dish containing the plants
- The coordinates of the 8 corners of the envelope:
    - front_right_top: [0.253, 0.2195, 0.2895]
    - back_right_top: [-0.1871, 0.2195, 0.2895]
    - back_left_top: [-0.1869, -0.1705, 0.2895]
    - front_left_top: [0.253, -0.1705, 0.2895]
    - front_left_bottom: [0.2526, -0.1705, 0.1693]
    - front_right_bottom: [0.2526, 0.2195, 0.1695]
    - back_right_bottom: [-0.1872, 0.2195, 0.1695]
    - back_left_bottom: [-0.187, -0.1705, 0.1695]
 - Required libraries:
    - Gym
    - sim_class
    - 

Final model hyperparameters:
   - Learning rate: 0.001
   - Batch size: 64
   - n_steps: 2048
   - n_epochs: 10
   