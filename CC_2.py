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
    prev1, prev2 = head, reqs[0]
    

    sign = 1 if head < reqs[0] else -1


    for swing in reqs:
        diff = abs(prev1-prev2) 
        total_cylinders += deff
        prev1,prev2 = prev2,swing






main()
