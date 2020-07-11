# cball5.py (=4 plus height calculation
from projectile import Projectile

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    hmax = h0
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        if cball.getY() >  h0:
            h0 = cball.getY()
        cball.update(time)

    print("\nDistance traveled: {0:0.1f} meters, max height is {1:0.1f}.".format(cball.getX(), h0))

main()