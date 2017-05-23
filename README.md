# Analysis-of-NPC-Pathfinding

# Introduction
While moving around, some NPCs in 2007scape will attack you. Sometimes this can be a unwanted encounter, but at other times you may want to NPCs to attack you if you're training a combat skill. NPCs that automatically attack you are called aggressive. Aggressive monsters will attack you once they have detected that you are k squares away from, where most monsters have k = 1. The map is laid out in a grid, of n x m cells.

# Analysis
Using this knowledge and the data of the frequency of monster presence per cell, can we determine the most optimal location such that the user maximizes the amount of time in combat with a certain type of monster?

For the first attempt, we have tracked all monster (Aberrant Spectre) movements in a closed location and have a dataset of 25,000 data points over 10 minutes. Firstly we aim to clean the data of incorrect data that may falsely influence our analysis.

Heatmap 1: All datapoints
![Screenshot](all_data.png)
