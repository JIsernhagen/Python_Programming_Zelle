def main():
    print("This program converts from Fahrenheit to Centigrade.")
    #n = eval(input("How many numbers should I print? "))
    for i in range(0, 100, 10):
        #C = eval(input("Enter the temperature in C: "))
        C = 5 / 9 * (i - 32)
        print("Temperature in F: ", i , " and C equivalent: ", C)
main()