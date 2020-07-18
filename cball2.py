#cball2.py
from math import sin, cos, radians

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time_interval = eval(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time_interval

def getXYComponents(vel, angle):
    # convert angle to radians
    theta = radians(angle)

    # set the initial position and velocities in x and y direcitons
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel, yvel

def updateCannonBall(time_interval, xpos, ypos, xvel, yvel):
    # calculate position and velocity in time seconds
    xpos = xpos + time_interval * xvel
    yvel1 = yvel - time_interval * 9.8
    ypos = ypos + time_interval * (yvel + yvel1)/2.0
    yvel = yvel1
    return xpos, ypos, yvel

def main():
    angle, vel, h0, timeinterval = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos>= 0:
        xpos, ypos, yvel = updateCannonBall(timeinterval, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

main()