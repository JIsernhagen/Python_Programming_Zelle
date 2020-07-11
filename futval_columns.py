def main():
    print("This program calculates the future value of a 10-year investment.")
    investment = eval(input("Enter the annual investment amount: "))
    apr = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter number of periods per year: "))
    principal = 0
    print("Year        Value")
    print("------------------")
    print(" 0      ${0:>8.2f}".format(investment))
    for i in range(10 * periods):
        principal += investment
        principal = principal * (1 + apr/periods)
        print("{0:2}      ${1:>8.2f}".format(i+1, principal))


main()