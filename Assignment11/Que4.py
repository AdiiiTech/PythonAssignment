def Reverse(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + 1
        no = no // 10

        print("Sum =", sum)

num = int(input("Enter a num :"))
Reverse(num)