def class_standing(credits):
    if credits >= 26:
        class_standing = 'Senior'
    elif credits >= 16:
        class_standing = 'Junior'
    elif credits >=7:
        class_standing = 'Sophomore'
    else:
        class_standing = 'Freshman'
    return class_standing

def main():
    credits = eval(input("Please submit credits: "))
    print("Class standing = "+ class_standing(credits))

main()