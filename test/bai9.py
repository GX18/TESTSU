a = int(input("Cho một số nào"))
b = int(input("Cho thêm số nữa!"))
c = int(input("Và số cuối cùng!"))
def quadro(a,b,c):
    delta = b*b - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b /(2*a)
        print(x)
    elif delta > 0:
        x1 = (-b + delta**(1/2))/(2*a) 
        x2 = (-b - delta**(1/2))/(2*a)
        print("Phương trình có hai nghiệm phân biệt",x1, ",", x2)
quadro(a,b,c)



