import os

def main():
    for i in range(1, 26):
        os.mkdir("day" + str(i))
        with open("day" + str(i) + "\input.txt", "w") as f:
            pass
        os.system("copy template.py day" + str(i) + "\main_day" + str(i) + "_task1.py")
        os.system("copy template.py day" + str(i) + "\main_day" + str(i) + "_task2.py")

if __name__ == "__main__":
    main()