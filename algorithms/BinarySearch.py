def binarySearch(A, t):
    A.sort()
    low = 0
    high = len(A)-1

    while (low+1 < high):
        split = (low + high)//2

        if (A[split] > t):
            high = split
        else:
            low = split

    if (A[low] == t):
        print("Value found")
    else:
        print("Value not found")


#file = open("numberlist.txt")
file = open("{}".format(input("Enter file name: ")))
df = file.read().split(", ")
arr = []
for num in df:
    num = int(num)
    arr.append(num)


x = input("Search: ")
try:
    intVal = int(x)
    binarySearch(arr, intVal)
except ValueError:
    print("Input needs to be a number")
