
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath) + "/.."
os.chdir(dname)

def main():
    print(os.getcwd())

if __name__ == "__main__":
    main()