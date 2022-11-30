import shutil

def main():
    for i in range(1, 26):
        shutil.rmtree("day" + str(i))

if __name__ == "__main__":
    main()