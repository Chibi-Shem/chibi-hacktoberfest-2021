input1 = int(input("Enter 1st number: "))
input2 = int(input("Enter 2nd number: "))
try:
    quotient = input1 / input2
    print(f"The quotient is: {quotient}")
except ZeroDivisionError:
    print("Invalid result!")