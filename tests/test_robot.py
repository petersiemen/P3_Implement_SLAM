from src.robot import Robot
from src.helpers import display_world
from random import seed
seed(1)

def test_init():
    rob = Robot()
    print(rob)


def test_sense():
    world_size = 10.0  # size of world (square)
    measurement_range = 5.0  # range at which we can sense landmarks
    motion_noise = 0.2  # noise in robot motion
    measurement_noise = 0.2  # noise in the measurements

    # instantiate a robot, r
    rob = Robot(world_size, measurement_range, motion_noise, measurement_noise)
    num_landmarks = 3
    rob.make_landmarks(num_landmarks)

    # print out our robot's exact location
    print(rob)

    # display the world including these landmarks
    display_world(int(world_size), [rob.x, rob.y], rob.landmarks)

    # print the locations of the landmarks
    print('Landmark locations [x,y]: ', rob.landmarks)

    measurements = rob.sense()
    assert len(measurements) == 3, "rob did not sense all 3 landmarks"
    print(measurements)

