def main():
    Cube = lambda no: no * no * no

    num = int(input("Enter a number: "))
    print("Cube =", Cube(num))

if __name__ == "__main__":
    main()