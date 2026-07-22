import multiprocessing
import os

def prime(no):
    print("Process is running with PID:", os.getpid())

    if no <= 1:
        return f"{no} is Not Prime"

    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return f"{no} is Not Prime"

    return f"{no} is Prime"

def main():
    Arr = []

    val = int(input("Enter the size of list: "))

    for i in range(val):
        no = int(input("Enter number: "))
        Arr.append(no)

    pobj = multiprocessing.Pool()

    result = pobj.map(prime, Arr)

    pobj.close()
    pobj.join()

    print("\nResult is:")
    for res in result:
        print(res)

if __name__ == "__main__":
    main()