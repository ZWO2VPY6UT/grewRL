"""
    Add the environment you wish to train here
"""

import gym
import numpy as np
from rllab.envs.gym_env import GymEnv

# ===================================================================
# Functions used in training and testing phase

def make_train_MDP():
    return _standard_ant()

def make_test_MDP():
    return _heavy_ant()

# ===================================================================
# Local functions to create envs

def _standard_ant():
    return GymEnv('Ant-v2')

def _heavy_ant():
    # Make the torso heavy
    e = GymEnv("Ant-v2")
    bm = np.array(e.env.model.body_mass)
    gs = np.array(e.env.model.geom_size)
    bm[1] = 7; gs[1][0] = 0.1;
    e.env.model.body_mass[:] = bm;
    e.env.model.geom_size[:] = gs;
    return e

# =======================================================================================
# Generate environment corresponding to the given mode

def get_environment(env_mode):

    modes = ['train', 'test']

    if env_mode == 'train':
        env = make_train_MDP()
    elif env_mode == 'test':
        env = make_test_MDP()
    else:
        print("ERROR: Unknown environment mode specified. Allowed modes are ", modes)

    return env
