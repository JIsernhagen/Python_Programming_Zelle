def squareEach(nums):
    squareslist = []
    for num in nums:
        squareslist.append(num**2)
    return squareslist

def main():
    nums = [1, 2, 3, 4, 5, 6]
    print(squareEach(nums))
    #print("Squares are: \n")
    #for square in squareEach(nums):
        #print(square)

main()