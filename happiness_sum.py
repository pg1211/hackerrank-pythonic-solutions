from collections import Counter

# Understand: need to return total happiness. happiness is determined by how many elements
# we see from each array a and b. sub one for elements appearing in b. add for elems in a.

# Match: this sounds like a Counter problem. yipee.

# Plan: create a counter, iterate through keys and check if in a or b. add/sub accordingly.


def func(arr, a, b):
    
    counts = dict(Counter(arr))
    print(sum([v for k, v in counts.items() if k in a]) - sum([v for k, v in counts.items() if k in b]))
    
if __name__ == "__main__":
    _ = input()
    arr = input().split()
    a = set(input().split())
    b = set(input().split())
    func(arr, a, b)
