def main():
    print("This program converts from Centigrade to Fahrenheit.")
    #n = eval(input("How many numbers should I print? "))
    for i in range(0, 100, 10):
        #C = eval(input("Enter the temperature in C: "))
        F = 9/5*i + 32
        print("Temperature in C: ", i , " and Fahrenheit equivalent: ", F)
main()