from collections import deque
# given a list of deque functions, execute them on a deque then print out the contents
# input:
# appendleft 3
# pop
# append 4
# append 5
# append 6
# popleft
# pop
# output:
# 5
def func():
    d = deque()
    
    num = int(input())
    
    lines = [input().split() for _ in range(num)]
    
    for line in lines:
        op = line[0]
        if op == "pop":
            d.pop()
            continue
        elif op == "popleft":
            d.popleft()
            continue
            
        val = int(line[1])
        
        if op == "append":
            d.append(val)
        else:
            d.appendleft(val)
        
    print(*d)

if __name__ == "__main__":
    func()
