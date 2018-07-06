# mymin2.py using a conditional

def mymin2(x, y):
    return x if x <= y else y

def main():
    for i in range(5):
        for j in range(5):
            print(i, j, mymin2(i, j), mymin2(i, j) == min(i, j))

main()
