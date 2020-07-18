#cball1.py
from math import sin, cos, radians

def main():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time_interval = eval(input("Enter the time interval between position calculations: "))

    # convert angle to radians
    theta = radians(angle)

    # set the initial position and velocities in x and y direcitons
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    # loop until the ball hits the ground
    while ypos >= 0.0:
        # calculate position and velocity in time seconds
        xpos = xpos + time_interval * xvel
        yvel1 = yvel - time_interval * 9.8
        ypos = ypos + time_interval * (yvel + yvel1)/2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f) meters.".format(xpos))

