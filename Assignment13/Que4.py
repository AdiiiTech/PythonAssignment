def Binary(no):
    print("Binary =", bin(no)[2:])

def main():
    num = int(input("Enter a number: "))
    Binary(num)

if __name__ == "__main__":
    main()