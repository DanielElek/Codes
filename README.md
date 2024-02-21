# This GitHub repository contains my most interesting projects from the start of my studies of Applied Data Science & Artificial Intelligence, so from the last 1.5 years
## I categorized my projects into two subfolders, with one more, Natural Language Processing still being in works, as that is the current project I am working on
 * ## Computer vision: this contains projects where I worked with image data
    * Netherlands Plant Eco-phenotyping Center: 
        - I developed a pipeline for the Netherlands Plant Eco-phenotyping Center that recognizes the roots of plants, cleans the resulting masks of false positives and measures the main root length of each individual plant with an sMAPE value of 18.963 %. Afterwards, I trained a robot with the help of reinforcement learning to find the end coordinates of the roots and inoculate them.
        - For the CNN that recognizes the roots of the plants, I used the U-net architecture, training it on around 120 images.
    * Soldier Recognition:
        - I had the task to develop an idea for an application that can make decisions based on computer vision and could have the potential to be a real life product, therefore I also had to conduct market research, market segmentation, competitor analysis, etc.
        - I developed a custom CNN model that I tuned myself with a trial and error approach.
        - The goal of the model is to differentiate soldiers from civilians, which it manages to do with an accuracy of ~ 82% after training it with around 500 images.
