import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    head = int(data[1])
    cyl = int(data[2])
    reqs = [int(x) for x in data[3:3 + n]]
    # TODO: total movement, then reversals.

    reversals = 0
    total_cylinders = 0

    

main()
