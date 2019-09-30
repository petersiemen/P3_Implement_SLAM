from src.slam import slam
from src.helpers import make_data
from src.get_poses_landmarks import get_poses_landmarks
from src.print_all import print_all

def test_slam():
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

    # call your implementation of slam, passing in the necessary parameters
    mu = slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise)
    # print out the resulting landmarks and poses
    if (mu is not None):
        # get the lists of poses and landmarks
        # and print them out
        poses, landmarks = get_poses_landmarks(mu, N, num_landmarks)
        print_all(poses, landmarks)

