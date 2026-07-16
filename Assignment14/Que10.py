def main():
    Largest = lambda x, y, z: x if (x > y and x > z) else (y if y > z else z)

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    print("Largest =", Largest(num1, num2, num3))

if __name__ == "__main__":
    main()