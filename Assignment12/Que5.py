def Reverse(no):
    for i in range(no, 0, -1):
        print(i, end=" ")

def main():
    num = int(input("Enter a number: "))
    Reverse(num)

if __name__ == "__main__":
    main()