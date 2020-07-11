def bmi(weight, height):
    bmi = weight * 720 / height ** 2
    return bmi

def main():
    weight, height = eval(input("Please input weight and height: "))
    if bmi(weight, height) <=18:
        print("Eat more Twinkies!")
    elif bmi(weight, height) >=26:
        print("Eat fewer Twinkies!")
    else:
        print("Continue eating Twinkies at your current rate.")

main()