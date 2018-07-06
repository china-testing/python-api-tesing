# csv_ex.py

from csv import reader

def readcsv(filename):
    with open(filename, newline="") as f:
        for row in reader(f):
            process(row)

def process(row):
    print(row)
    
def main():
    readcsv("census.csv")

main()
