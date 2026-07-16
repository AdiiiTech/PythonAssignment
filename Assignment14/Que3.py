def main():
    Maximum = lambda x, y: x if x > y else y

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Maximum =", Maximum(num1, num2))

if __name__ == "__main__":
    main()