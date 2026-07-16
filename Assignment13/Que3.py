def Perfect(no):
    sum = 0

    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    if sum == no:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    num = int(input("Enter a number: "))
    Perfect(num)

if __name__ == "__main__":
    main()