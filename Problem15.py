#Recursive solution:
table = {}

def f(x, y):
    if (x, y) in table:
        return table[(x, y)]
    else:
        if x <= 0 or y <= 0:
            table[(x, y)] = 1
            return 1
        else:
            result = f(x-1, y) + f(x, y-1)
            table[(x, y)] = result
            return result

print f(20, 20)

#There is also a closed form soluton. This is a very common problem in combinatorics.
#There are a total of (x+y) directions to be travelled, and we must strictly the define
#the position of either x or y of the directions. In combinatorics, this is defined as
#choose(x+y, x) == choose(x+y, y) == (x+y)*(x+y-1)*...*(y+1)/(x!) == (x+y)*(x+y-1)*...*(x+1)/(y!)

