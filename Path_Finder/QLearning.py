# PROJECT MANAS RL Workshop
'''
*
*   ===================================================
*       PROJECT MANAS - RL Workshop
*   ===================================================
*
*  This script contains the Q-Learning Logic and Definitions.
*
*  Filename:		QLearning.py
*  Author:		    PROJECT MANAS
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*
*****************************************************************************************
'''
import numpy as np
ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

def get_reward(state, goal_state):
    pass
    if (state== goal_state)
    return 100
    else
    return -1

def get_action(q_table, state, epsilon, action_space_size):
    pass
    ## [WORKSHOP] Implement the action selection function
x,y = state
if np.random.uniform(0 ,1)< epsilon:
    return np.random.randint(0.action_space_size)
else:
    retun np.argmax(q_table[x,y])
def update_q_table(q_table, state, action, reward, next_state, alpha, gamma):
    pass
    ## [WORKSHOP] Implement the Q-table update function
    x, y = state
    next_x, next_y = next_state

old_value = q_table[x,y]
next_max = np.max(q_table[next_x,next_y])

new_value = old_value + alpha* (reward + game*next_max . old_values)
q_table[x,y,action]= new_value
