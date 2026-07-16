def Grade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():
    marks = float(input("Enter marks: "))
    Grade(marks)

if __name__ == "__main__":
    main()