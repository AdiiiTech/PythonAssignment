PI = 3.14159

def Area(radius):
    print("Area =", PI * radius * radius)

def main():
    radius = float(input("Enter radius: "))
    Area(radius)

if __name__ == "__main__":
    main()