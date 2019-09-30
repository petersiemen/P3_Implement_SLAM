# a helper function that creates a list of poses and of landmarks for ease of printing
# this only works for the suggested constraint architecture of interlaced x,y poses
def get_poses_landmarks(mu, N, num_landmarks):
    # create a list of poses
    poses = []
    for i in range(N):
        poses.append((mu[2 * i].item(), mu[2 * i + 1].item()))

    # create a list of landmarks
    landmarks = []
    for i in range(num_landmarks):
        landmarks.append((mu[2 * (N + i)].item(), mu[2 * (N + i) + 1].item()))

    # return completed lists
    return poses, landmarks
