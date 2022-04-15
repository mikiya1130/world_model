from cmath import sqrt


def reward_myenv(x, y, next_x, next_y, dest_x, dest_y):
    weight=0.01
    reward_d=sqrt((dest_x-x)**2+(dest_y-y)**2)-sqrt((dest_x-next_x)**2+(dest_y-next_y)**2)
    reward_v=sqrt((next_x-x)**2+(next_y-y)**2)
    reward=reward_d+weight*reward_v
    return reward