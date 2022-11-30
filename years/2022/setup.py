import os

def main():
    for i in range(1, 26):
        os.mkdir("day" + str(i))
        os.system("copy template.py day" + str(i) + "\main_day" + str(i) + ".py")

if __name__ == "__main__":
    main()