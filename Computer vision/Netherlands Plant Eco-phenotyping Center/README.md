# This was the most advanced project I have worked on, with also the strictest client requirements

## We needed to create a Computer Vision pipeline that could automatically measure the length of the individual roots of the plants upon creating a photograph of them, as well as finding the very bottom of them for further inoculation by a machine in the research center.

## Afterwards, we also needed to train a Reinforcement Learning Model to inoculate the end of the root with a 1 mm accuracy

    - Step 0: Images get taken by the system
<img src="media/pic1_raw.png" alt="Raw image" width="700"/>

    - Step 1: Cropping the images and masks while taking into account that not all images are taken from 100% same angle
<img src="media/pic1_cut.png" alt="Cut image" width="700"/>
<img src="media/cutting_code.png" alt="Cut image" width="700"/>

    - Step 2: Using U-NET with patches to find the roots in the pictures
<img src="media/pic1_after_DL.png" alt="After Deep Learning" width="700"/>
<img src="media/U-NET training.png" alt="U-NET training" width="700"/>

    - Step 3: Cleaning up the output images using connected components
<img src="media/pic1_cleaned.png" alt="After cleaning" width="700"/>
<img src="media/Cleaning_code.png" alt="Cleaning code" width="700"/>

    - Step 4: Skeletonizing the roots to 1 px thickness to find the different type of connections in the image
<img src="media/pic_1_skeletonized.png" alt="Skeletonized" width="700"/>
<img src="media/skeletonizing_code.png" alt="Skeletonizing code" width="700"/>

    - Step 5: Finding the bottom most pixel of each root for the inoculation
<img src="media/pic1_bottompx.png" alt="Bottom pixel" width="700"/>
<img src="media/bottomfinding_code.png" alt="Bottomfinding code" width="700"/>

    - Step 6: Measuring the length of each root
<img src="media/pic1_length.jpg" alt="Root length" width="700"/>
<img src="media/length_code.png" alt="Lengthfinding code" width="700"/>

    - Step 7: Training the Reinforcement Learning Model
<img src="media/PID controller.gif" alt="Machine control" width="700"/>
<img src="media/reinforcement_learning.png" alt="RL_code" width="700"/>