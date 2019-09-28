x = [1,2,3,4]
y = input("Xoá đầu hay cuối")
if y == "Đầu":
    x.pop(0)
    print(x)
elif y == "Cuối":
    x.pop(-1)
    print(x)