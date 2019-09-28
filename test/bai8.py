x = [1,2,3,4]
y = input("Do you want to delete the first or last position?")
if y == "first":
    x.pop(0)
    print("sequence:",*x)
elif y == "last":
    x.pop(-1)
    print("sequence:",*x)