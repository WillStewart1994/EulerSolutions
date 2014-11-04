#Recursive solution:
def f(x, y):
    if x == 1 and y == 1:
        return 1
    elif x <= 0:
        return f(x, y-1)
    elif y <= 0:
        return f(x-1, y)
    else:
        return f(x-1, y) + f(x, y-1)

print f(20)

#There is also a closed form soluton. This is a very common problem in combinatorics.
#There are a total of (x+y) directions to be travelled, and we must strictly the define
#the position of either x or y of the directions. In combinatorics, this is defined as
#choose(x+y, x) == choose(x+y, y) == (x+y)*(x+y-1)*...*(y+1)/(x!) == (x+y)*(x+y-1)*...*(x+1)/(y!)


