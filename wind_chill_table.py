def main():
    print("________________________________________________________________")
    print("T(F)     W(mph)      Wind Chill")
    for t in range (0, 50, 5):
        for v in range (-20, 60, 10):
            wc = 35.74 + (0.6215 * t) - (35.75 * v**0.16) + (0.4275 * v ** 0.16)
            print("{0:>2}F and {1:>3}mph  yields  {2:>1.2F} wind chill".format(t, v, wc))
    print("________________________________________________________________")

main()
