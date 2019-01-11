# Programmer: Ahmed L Saeed
# Project: Restaurant Mangement System
# Start Date: 10 Jan 2019
# TO DO: Figure out a way to get buttons to work with macOS Mojave.
# , Tkinter doesn't work for some reason

import random
import time;
import datetime
import tkinter.messagebox
from tkinter import*

# == MAIN WINDOW ==
root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background = 'Cadet Blue')

# == TOP FRAME ==
Tops = Frame(root, bg = 'Cadet Blue', bd = 20, pady = 5, relief = RIDGE)
Tops.pack(side = TOP)
lblTitle = Label(Tops, font = ('arial', 60, 'bold'), text = "Restaurant Management System", bd = 21, bg = 'Cadet Blue', fg = 'Cornsilk', justify = CENTER)
lblTitle.grid(row = 0, column = 0)

# == RIGHT FRAME ==
ReceiptCal_F = Frame(root, bg = 'Powder Blue', bd = 10, relief = RIDGE)
ReceiptCal_F.pack(side = RIGHT)
Buttons_F = Frame(ReceiptCal_F, bg = 'Powder Blue', bd = 3, relief = RIDGE)
Buttons_F.pack(side = BOTTOM)
Cal_F = Frame(ReceiptCal_F, bg = 'Powder Blue', bd = 6, relief = RIDGE)
Cal_F.pack(side = TOP)
Receipt_F = Frame(ReceiptCal_F, bg = 'Powder Blue', bd = 4, relief = RIDGE)
Receipt_F.pack(side = BOTTOM)

# == LEFT FRAME ==
MenuFrame = Frame(root, bg = 'Cadet Blue', bd = 10, relief = RIDGE)
MenuFrame.pack(side = LEFT)
Cost_F = Frame(MenuFrame, bg = 'Powder Blue', bd = 4)
Cost_F.pack(side = BOTTOM)
Drinks_F = Frame(MenuFrame, bg = 'Cadet Blue', bd = 10)
Drinks_F.pack(side = TOP)


Drinks_F = Frame(MenuFrame, bg = 'Powder Blue', bd = 10, relief = RIDGE)
Drinks_F.pack(side = LEFT)
Cakes_F = Frame(MenuFrame, bg = 'Powder Blue', bd = 10, relief = RIDGE)
Cakes_F.pack(side = RIGHT)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

# == DRINKS ==
Latte = Checkbutton(Drinks_F, text = "Latte", variable = var1, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 0, sticky = W)
Expresso = Checkbutton(Drinks_F, text = "Expresso", variable = var2, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 1, sticky = W)
Iced_Latte = Checkbutton(Drinks_F, text = "Iced Latte", variable = var3, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 2, sticky = W)
Iced_Coffee = Checkbutton(Drinks_F, text = "Iced Coffee", variable = var4, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 3, sticky = W)
Cappuccino = Checkbutton(Drinks_F, text = "Cappuccino", variable = var5, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 4, sticky = W)
Arabian_Tea = Checkbutton(Drinks_F, text = "Arabian Tea", variable = var6, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 5, sticky = W)
French_Roast = Checkbutton(Drinks_F, text = "French Roast", variable = var7, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 6, sticky = W)
Black_Tea = Checkbutton(Drinks_F, text = "Black Tea", variable = var8, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 7, sticky = W)

# == ENTRY BOX FOR DRINKS ==
txtLatte = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtLatte.grid(row = 0, column = 1)
txtExpresso = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtExpresso.grid(row = 1, column = 1)
txtIced_Latte = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtIced_Latte.grid(row = 2, column = 1)
txtIced_Coffee = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtIced_Coffee.grid(row = 3, column = 1)
txtCappuccino = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtCappuccino.grid(row = 4, column = 1)
txtArabian_Tea = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtArabian_Tea.grid(row = 5, column = 1)
txtFrench_Roast = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtFrench_Roast.grid(row = 6, column = 1)
txtBlack_Tea = Entry(Drinks_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtBlack_Tea.grid(row = 7, column = 1)

# == CAKES ==
Chocolate_Cake = Checkbutton(Cakes_F, text = "Chocolate Cake", variable = var9, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 0, sticky = W)
Velvet_Cake = Checkbutton(Cakes_F, text = "Velvet Cake", variable = var10, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 1, sticky = W)
StrawberryShort_Cake = Checkbutton(Cakes_F, text = "Strawberry Short Cake", variable = var11, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 2, sticky = W)
Cheese_Cake = Checkbutton(Cakes_F, text = "Cheese Cake", variable = var12, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 3, sticky = W)
IceCream_Cake = Checkbutton(Cakes_F, text = "Ice Cream Cake", variable = var13, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 4, sticky = W)
Butterscotch_Cake = Checkbutton(Cakes_F, text = "Butterscotch Cake", variable = var14, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 5, sticky = W)
Lemon_Cake = Checkbutton(Cakes_F, text = "Lemon Cake", variable = var15, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 6, sticky = W)
Pound_Cake = Checkbutton(Cakes_F, text = "Pound Cake", variable = var16, onvalue = 1, offvalue = 0, font = ('arial', 18, 'bold'), bg = 'Powder blue').grid(row = 7, sticky = W)

# == ENTRY BOX FOR CAKES ==
txtChocolate_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtChocolate_Cake.grid(row = 0, column = 1)
txtVelvet_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtVelvet_Cake.grid(row = 1, column = 1)
txtStrawberryShort_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtStrawberryShort_Cake.grid(row = 2, column = 1)
txtCheese_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtCheese_Cake.grid(row = 3, column = 1)
txtIceCream_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtIceCream_Cake.grid(row = 4, column = 1)
txtButterscotch_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtButterscotch_Cake.grid(row = 5, column = 1)
txtLemon_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtLemon_Cake.grid(row = 6, column = 1)
txtPound_Cake = Entry(Cakes_F, font = ('arial', 16, 'bold'), bd = 8, width = 6, justify = LEFT, state = DISABLED)
txtPound_Cake.grid(row = 7, column = 1)

# == RECEIPTS ==
txtReceipt = Text(Receipt_F, width = 46, height = 12, bg = "white", bd = 4, font = ('arial', 12, 'bold'))
txtReceipt.grid(row = 0, column = 0)

# == BUTTONS ==
btnTotal = Button(Buttons_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "Total", bg = "powder blue").grid(row = 0, column = 0)
btnReceipt = Button(Buttons_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "Receipt", bg = "powder blue").grid(row = 0, column = 1)
btnReset = Button(Buttons_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "Reset", bg = "powder blue").grid(row = 0, column = 2)
btnExit = Button(Buttons_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "Exit", bg = "powder blue").grid(row = 0, column = 3)

# == CALCULATOR DISPLAY ==
txtDisplay = Entry(Cal_F, width = 45, bg = "white", bd = 4, font = ('arial', 12, 'bold'), justify = RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, "0")

# == CALCULATOR BUTTONS ==
btn7 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "7", bg = "powder blue").grid(row = 2, column = 0)
btn8 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "8", bg = "powder blue").grid(row = 2, column = 1)
btn9 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "9", bg = "powder blue").grid(row = 2, column = 2)
btnAdd = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "+", bg = "powder blue").grid(row = 2, column = 3)

btn4 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "4").grid(row = 3, column = 0)
btn5 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "5").grid(row = 3, column = 1)
btn6 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "6").grid(row = 3, column = 2)
btnSub = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "-", bg = "powder blue").grid(row = 3, column = 3)

btn1 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "1").grid(row = 4, column = 0)
btn2 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "2").grid(row = 4, column = 1)
btn3 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "3").grid(row = 4, column = 2)
btnMult = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "x", bg = "powder blue").grid(row = 4, column = 3)

btn0 = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "0", bg = "powder blue").grid(row = 5, column = 0)
btnClr = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "C", bg = "powder blue").grid(row = 5, column = 1)
btnEquals = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "=", bg = "powder blue").grid(row = 5, column = 2)
btnDiv = Button(Cal_F, padx = 16, pady=1, bd = 7, fg = "black", font = ('arial', 16, 'bold'), width = 4, text = "/", bg = "powder blue").grid(row = 5, column = 3)


# !! YOU STOPPED HERE











root.mainloop()
