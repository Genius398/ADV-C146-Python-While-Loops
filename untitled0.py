from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("400x400")


 label_series = Label(root, text="Fobonacci Series")

 label_flower = Label(root)

 label_spiral = Label(root)

 def Fibonacci():
    
    num = 10
    first_no=0
    second_no=1
    sum=first_no + second_no
    label_flower['text'] = "Flower Bloomed"
    label_spiral['text'] = "Right spirals are" + str(first_no) + "Left Spirals are" + str(second_no)


    btn = Button(root, text="Show", commands=Fibonacci) 
    btn.pack()
    label_series.pack()
    label_flowers.pack()
    label_spiral.pack()
 root.mainloop()