def main():
    Divisible = lambda no: no % 5 == 0

    num = int(input("Enter a number: "))
    print(Divisible(num))

if __name__ == "__main__":
    main()