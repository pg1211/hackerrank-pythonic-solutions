# Understand: stacking cubes where you can only select left and right cubes from list of cubes
# cubes must be larger than cubes "on top" of them
# return either "Yes" or "No" if possible or not.

# Match: both sides operations: deque.

# Plan: take from each side and keep track of min element seen. if both elements bigger than min, return No

from collections import deque

def handle_case():
    _ = int(input())
    
    blocks = deque([int(item) for item in input().split()])
    # while blocks still has items, check if something is smaller than min
    top = float('inf')
    
    while blocks:
        # if right element is closest to top while being smaller or equal to top
        if blocks[-1] <= top and (blocks[0] > top or blocks[-1] >= blocks[0]):
            top = blocks.pop()
        # else, if left element is less than top
        elif blocks[0] <= top:
            top = blocks.popleft()
        # nothing works: leave now
        else:
            print("No")
            return
            
    # all blocks gone
    print("Yes")
    return
    

def func():
    num_cases = int(input())
    
    # handling procedure for cases goes through helper for clarity
    for _ in range(num_cases):
        handle_case()
    
if __name__ == "__main__":
    func()
