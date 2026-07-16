def Area(length, width):
    print("Area =", length * width)

def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    Area(length, width)

if __name__ == "__main__":
    main()