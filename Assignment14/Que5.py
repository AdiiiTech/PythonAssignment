def main():
    Even = lambda no: no % 2 == 0

    num = int(input("Enter a number: "))
    print(Even(num))

if __name__ == "__main__":
    main()