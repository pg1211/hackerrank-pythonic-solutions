import re

# find strings with 2+ consecutive vowels between two consonants. use lookahead/behind
# in order to match correctly while still matching strings with overlapping consonants
def func():
    lst = re.findall(r"(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])", input())
    if lst:
        for item in lst:
            print(item)
    else:
        print(-1)
    
    
    
if __name__ == "__main__":
    func()
