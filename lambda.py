def isEven(i):
    return i%2==0

list1 = [3, 4, 10, 9, 18, 66, 13, 15]
evenNum = list(filter(isEven,list1))
print(evenNum)
evenNum = list(filter(lambda i : i%2==0, list1))
print(evenNum)
squareNum = list(map(lambda i : i ** 2, list1))
print(squareNum)

list1 = [10,20,30,40,50]
# triple the values of the list
triple = list(map(lambda i : i * 3, list1))
print(triple)

list2 = ["a", "B", "c", "D", "e", "f"]
lowercase= list(map(lambda x: x.lower(), ["B", "D"]))
uppercase= list(map(lambda x: x.upper(), ["a", "c", "e", "f"]))
print((lowercase) + (uppercase))

def div(a,b):
    print(a/b)

def good_div(func):
    def inner_div(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

    return inner_div

output = good_div(div)
div(2,4)




