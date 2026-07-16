def CountDigits(no):
    count = 0

    while no > 0:
        count = count + 1
        no = no // 10

        print("Count =", count)

num = int(input("Enter a num :"))
CountDigits(num)