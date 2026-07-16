def main():
    Odd = lambda no: no % 2 != 0

    num = int(input("Enter a number: "))
    print(Odd(num))

if __name__ == "__main__":
    main()