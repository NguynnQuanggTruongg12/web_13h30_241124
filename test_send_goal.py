import numpy


def odem_goal(x_goal, y_goal, z_goal, w_goal):
    if (0 <= z_goal <= 0.5 or -0.5 <= z_goal <0) and 0.8 <= w_goal <=1:
        x_goal = x_goal - 0.4
        y_goal = y_goal
    elif (0 <= z_goal <= 0.5 or -0.5 <= z_goal <0) and -1 <= w_goal <= -0.8:
        x_goal = x_goal + 0.4
        y_goal = y_goal
    return x_goal, y_goal, z_goal, w_goal

x, y, z, w = odem_goal(1,0.5,0.1,-0.9)
print(f'{x}, {y}, {z}, {w}')
    
