import numpy as np
from helpers import make_data
from src.initialize_constraints import initialize_constraints
import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn as sns

def test_make_data():

    # your implementation of slam should work with the following inputs
    # feel free to change these input values and see how it responds!

    # world parameters
    num_landmarks = 5  # number of landmarks
    N = 20  # time steps
    world_size = 100.0  # size of world (square)

    # robot parameters
    measurement_range = 50.0  # range at which we can sense landmarks
    motion_noise = 2.0  # noise in robot motion
    measurement_noise = 2.0  # noise in the measurements
    distance = 20.0  # distance by which robot (intends to) move each iteratation

    # make_data instantiates a robot, AND generates random landmarks for a given world size and number of landmarks
    data = make_data(N, num_landmarks, world_size, measurement_range, motion_noise, measurement_noise, distance)
    time_step = 0

    print('Example measurements: \n', data[time_step][0])
    print('\n')
    print('Example motion: \n', data[time_step][1])


def test_initialize_constraints_show_omega():
    N_test = 5
    num_landmarks_test = 2
    small_world = 10

    # initialize the constraints
    initial_omega, initial_xi = initialize_constraints(N_test, num_landmarks_test, small_world)
    plt.rcParams["figure.figsize"] = (10, 7)

    # display omega
    sns.heatmap(DataFrame(initial_omega), cmap='Blues', annot=True, linewidths=.5)

    plt.show()

def test_initialize_constraints_show_xi():
    N_test = 5
    num_landmarks_test = 2
    small_world = 10

    # initialize the constraints
    initial_omega, initial_xi = initialize_constraints(N_test, num_landmarks_test, small_world)

    plt.rcParams["figure.figsize"] = (1, 7)

    # display xi
    sns.heatmap(DataFrame(initial_xi), cmap='Oranges', annot=True, linewidths=.5)
    plt.show()
