def main():
    print("This program calculates the future value of a 10-year investment.")
    infile_name = input("Please enter the input filename: ")
    input_file = open(infile_name, "r")
    output_file = open("output.csv", "w")
    investment = eval(input_file.readline())
    print(investment)
    apr = eval(input_file.readline())
    print(apr)
    periods = eval(input_file.readline())
    print(periods)
    principal = 0
    print("Year        Value", file=output_file)
    print("------------------", file=output_file)
    print(" 0      ${0:>8.2f}".format(investment), file=output_file)

    for i in range(10 * periods):
        principal += investment
        principal = principal * (1 + apr/periods)
        print("{0:2}      ${1:>8.2f}".format(i+1, principal), file=output_file)

    output_file.close()

main()