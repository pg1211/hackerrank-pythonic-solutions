def checker():
    n_a, n_b = map(int, input().split())
    
    # generate list a
    a = [input() for i in range(n_a)]

    # generate mappings of values to ints (1-indexed)
    mappings = defaultdict(list)
    output = ""
    for index, value in enumerate(a):
        mappings[value].append(str(index + 1))

    # now, iterate through remaining input and check if in mappings.
    # if in mappings, print the indices. otherwise, print -1.
    for i in range(n_b):
        key = input()
        
        print(' '.join(mappings[key]) if key in mappings else "-1")

if __name__ == "__main__:
  checker()
