import numpy as np
from src.initialize_constraints import initialize_constraints


## TODO: Complete the code to implement SLAM

## slam takes in 6 arguments and returns mu,
## mu is the entire path traversed by a robot (all x,y poses) *and* all landmarks locations
def slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise):
    ## TODO: Use your initilization to create constraint matrices, omega and xi
    omega, xi = initialize_constraints(N, num_landmarks, world_size)

    measurement_noise_weight = (1.0 / measurement_noise)
    motion_noise_weight = 1.0 / motion_noise
    landmark_positions = N

    ## TODO: Iterate through each time step in the data
    ## get all the motion and measurement data as you iterate
    for pose, step_data in enumerate(data):
        x = pose * 2
        y = x + 1
        measurements = step_data[0]
        motion = step_data[1]

        ## TODO: update the constraint matrix/vector to account for all *measurements*
        ## this should be a series of additions that take into account the measurement noise
        for measurement in measurements:
            print(measurement)
            landmark_idx = measurement[0]
            dx = measurement[1]
            dy = measurement[2]

            landmark_pos_x = (landmark_positions + landmark_idx) * 2
            landmark_pos_y = landmark_pos_x + 1

            # Updating omega values based on current position and measured langmark data
            omega[x][x] += measurement_noise_weight
            omega[x][landmark_pos_x] -= measurement_noise_weight
            omega[landmark_pos_x][x] -= measurement_noise_weight
            omega[landmark_pos_x][landmark_pos_x] += measurement_noise_weight

            omega[y][y] += measurement_noise_weight
            omega[y][landmark_pos_y] -= measurement_noise_weight
            omega[landmark_pos_y][y] -= measurement_noise_weight
            omega[landmark_pos_y][landmark_pos_y] += measurement_noise_weight

            # Update Xi measurements
            xi[x] -= dx / measurement_noise
            xi[landmark_pos_x] += dx / measurement_noise

            xi[y] -= dy / measurement_noise
            xi[landmark_pos_y] += dy / measurement_noise

    ## TODO: update the constraint matrix/vector to account for all *motion* and motion noise
        next_pose_x = x + 2
        next_pose_y = next_pose_x + 1

        motion_dx = motion[0]
        motion_dy = motion[1]

        # Update omega motions
        omega[x][x] +=  motion_noise_weight
        omega[x][next_pose_x] -=  motion_noise_weight
        omega[next_pose_x][x] -=  motion_noise_weight
        omega[next_pose_x][next_pose_x] += motion_noise_weight

        omega[y][y] +=  motion_noise_weight
        omega[y][next_pose_y] -=  motion_noise_weight
        omega[next_pose_y][y] -=  motion_noise_weight
        omega[next_pose_y][next_pose_y] += motion_noise_weight

        # Update Xi motions
        xi[x] -= motion_dx / motion_noise
        xi[next_pose_x] += motion_dx / motion_noise

        xi[y] -= motion_dy / motion_noise
        xi[next_pose_y] += motion_dy / motion_noise

    ## TODO: After iterating through all the data
    ## Compute the best estimate of poses and landmark positions
    ## using the formula, omega_inverse * Xi
    mu = np.linalg.inv(np.matrix(omega)) * xi

    return mu  # return `mu`
