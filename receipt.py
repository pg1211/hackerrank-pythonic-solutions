from collections import OrderedDict
# given a list of items in form NAME NAME... PRICE print ordered bill with amt spend per item

def func():
    # get num items
    num_items = int(input())
    
    purchases = OrderedDict()
    # iterate through remaining and add to OrderedDict
    
    for _ in range(num_items):
        # need to get input, split off last element, join the other elements back together to get key
        
        # use unpacking to get the name and price separate
        *words, price = input().split()
        
        # join name back together
        name = ' '.join(words)
        
        # set the k v pair in purchases to be correct amt spent 
        purchases[name] = purchases.get(name, 0) + int(price)
    
    # iterate through ordereddict and print
    for k, v in purchases.items():
        print(k, v)
    
if __name__ == "__main__":
    func()
