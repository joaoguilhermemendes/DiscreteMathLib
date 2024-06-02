from customtkinter import*

frame = CTk()

frame.geometry("700x400")
frame.title("Discrete Math Lib")
#frame.config(background="rey")
frame.resizable(False, False)
try:
    frame.iconbitmap("favicon.ico")
except Exception as e:
    print("Error setting icon:", e)



frame.mainloop()