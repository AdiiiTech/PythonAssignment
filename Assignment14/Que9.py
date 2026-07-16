def main():
    Multiply = lambda x, y: x * y

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Multiplication =", Multiply(num1, num2))

if __name__ == "__main__":
    main()