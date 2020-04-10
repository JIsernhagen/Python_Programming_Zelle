def main():
    print("This program calculates the future value of a 10-year investment.")
    investment = eval(input("Enter the annual investment amount: "))
    apr = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter number of periods per year: "))
    principal = 0
    for i in range(10 * periods):
        principal = principal + investment
        principal = principal * (1 + apr/periods)
        print("The value of the principal in", i, "periods is: ", principal)

main()