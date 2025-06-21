from collections import Counter, OrderedDict

# Understand: need to output number of occurrences of each word. output order corresponds with
# input order. 

# Match: counting occurrences: use Counter. retain order of input: OrderedDict?

# Plan: take in words as list. use Counter. print len(dict) and values in order

def func():
    num_words = int(input())

    # create list of words from input
    lst = [input() for _ in range(num_words)]

    # create counter dict
    my_dict = dict(Counter(lst))

    # print all output
    print(len(my_dict))
    output = [v for _, v in my_dict.items()]
    print(*output)
        
if __name__ == "__main__":
    func()
