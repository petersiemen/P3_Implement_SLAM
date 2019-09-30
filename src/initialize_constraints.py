import numpy as np


def initialize_constraints(N, num_landmarks, world_size):
    ''' This function takes in a number of time steps N, number of landmarks, and a world_size,
        and returns initialized constraint matrices, omega and xi.'''

    ## Recommended: Define and store the size (rows/cols) of the constraint matrix in a variable

    ## TODO: Define the constraint matrix, Omega, with two initial "strength" values
    ## for the initial x, y location of our robot
    rows = 2 * (N + num_landmarks)
    cols = rows

    omega = np.zeros((rows, cols))

    ## TODO: Define the constraint *vector*, xi
    ## you can assume that the robot starts out in the middle of the world with 100% confidence
    xi = np.zeros((rows, 1))

    x0 = 0
    y0 = 1
    start_x = world_size / 2.
    start_y = world_size / 2.

    omega[x0][x0] = 1
    omega[y0][y0] = 1
    xi[x0][0] = start_x
    xi[y0][0] = start_y

    return omega, xi
