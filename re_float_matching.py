import re
# need to match to start: +, - or nothing
# zero or more digits before decimal point
# need to have decimal point
# need one or more digits after decimal point
def tester():
    string = input()
    
    if re.match(r"^[+-]?[0123456789]*\.[0123456789]+$", string):
        print("True")
    else:
        print("False")

def func():
    for _ in (range(int(input()))):
        tester()
    
if __name__ == "__main__":
    func()
