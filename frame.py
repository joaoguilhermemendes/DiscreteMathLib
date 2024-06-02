'''from customtkinter import*

frame = CTk()

frame.geometry("700x400")
frame.title("Discrete Math Lib")
#frame.config(background="rey")
frame.resizable(False, False)
try:
    frame.iconbitmap("favicon.ico")
except Exception as e:
    print("Error setting icon:", e)

frame.mainloop()'''



def Summation(exp,i,n):
    j=i
    parts=[]
    while j<=n:
        x=j
        res = eval(exp)
        parts.append(res)
        j=j+1
    print(parts)
    print(sum(parts))

exp = str(input("Enter the expression - e.g. (4*x ** 2) - 1) ---- "))
i = int(input("Enter the initial index: "))
n = int(input("Enter the final index: "))

print(Summation(exp, i, n))