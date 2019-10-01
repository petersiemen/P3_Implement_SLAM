import numpy as np
from src.initialize_constraints import initialize_constraints


## TODO: Complete the code to implement SLAM

## slam takes in 6 arguments and returns mu,
## mu is the entire path traversed by a robot (all x,y poses) *and* all landmarks locations
def slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise):
    ## TODO: Use your initilization to create constraint matrices, omega and xi
    omega, xi = initialize_constraints(N, num_landmarks, world_size)

    measurement_noise_weight = 1.0 / measurement_noise
    motion_noise_weight = 1.0 / motion_noise
    idx_start_landmarks = N

    ## TODO: Iterate through each time step in the data
    ## get all the motion and measurement data as you iterate
    for t, (measurements, motion) in enumerate(data):
        idx_x = t * 2
        idx_y = idx_x + 1
        # displacement along x and y axis
        motion_dx = motion[0]
        motion_dy = motion[1]

        ## TODO: update the constraint matrix/vector to account for all *measurements*
        ## this should be a series of additions that take into account the measurement noise
        for measurement in measurements:
            landmark_idx = measurement[0]
            # distance to landmark in x and y direction
            landmark_dx = measurement[1]
            landmark_dy = measurement[2]

            idx_x_landmark = (idx_start_landmarks + landmark_idx) * 2
            idx_y_landmark = idx_x_landmark + 1

            # Updating omega values for x and y coordinates
            # x
            omega[idx_x][idx_x] += measurement_noise_weight
            omega[idx_x][idx_x_landmark] -= measurement_noise_weight
            omega[idx_x_landmark][idx_x_landmark] += measurement_noise_weight
            omega[idx_x_landmark][idx_x] -= measurement_noise_weight
            # y
            omega[idx_y][idx_y] += measurement_noise_weight
            omega[idx_y][idx_y_landmark] -= measurement_noise_weight
            omega[idx_y_landmark][idx_y_landmark] += measurement_noise_weight
            omega[idx_y_landmark][idx_y] -= measurement_noise_weight

            # Update Xi measurements for x and y coordinates
            # x
            xi[idx_x] -= landmark_dx * measurement_noise_weight
            xi[idx_x_landmark] += landmark_dx * measurement_noise_weight
            # y
            xi[idx_y] -= landmark_dy * measurement_noise_weight
            xi[idx_y_landmark] += landmark_dy * measurement_noise_weight

        ## TODO: update the constraint matrix/vector to account for all *motion* and motion noise
        idx_x_next_pose = idx_x + 2
        idx_y_next_pose = idx_x_next_pose + 1

        # Update omega motions
        omega[idx_x][idx_x] += motion_noise_weight
        omega[idx_x][idx_x_next_pose] -= motion_noise_weight
        omega[idx_x_next_pose][idx_x_next_pose] += motion_noise_weight
        omega[idx_x_next_pose][idx_x] -= motion_noise_weight

        omega[idx_y][idx_y] += motion_noise_weight
        omega[idx_y][idx_y_next_pose] -= motion_noise_weight
        omega[idx_y_next_pose][idx_y_next_pose] += motion_noise_weight
        omega[idx_y_next_pose][idx_y] -= motion_noise_weight

        # Update Xi motions
        # x
        xi[idx_x] -= motion_dx * motion_noise_weight
        xi[idx_x_next_pose] += motion_dx * motion_noise_weight

        # y
        xi[idx_y] -= motion_dy * motion_noise_weight
        xi[idx_y_next_pose] += motion_dy * motion_noise_weight

    ## TODO: After iterating through all the data
    ## Compute the best estimate of poses and landmark positions
    ## using the formula, omega_inverse * Xi
    mu = np.linalg.inv(np.matrix(omega)) * xi

    return mu
