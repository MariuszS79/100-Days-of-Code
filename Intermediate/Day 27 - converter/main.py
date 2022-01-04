from tkinter import *


# function that converts from miles to kilometers after input and clicking "Calculate" button
def calculate():
    result = round(float(inp.get()) * 1.609, 2)
    summary.config(text=result)
    return result


# window for program
window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=250, height=160)
window.config(padx=30, pady=30)

# entry
inp = Entry(width=10)
print(inp.get())
inp.grid(column=1, row=0)

# label with text "miles"
miles = Label(text="miles")
miles.grid(column=2, row=0)

# label with text "equal to"
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
equal.config(pady=15)

# label where final calculation appears
summary = Label(text="", font="Arial")
summary.grid(column=1, row=1)
summary.config(pady=15)

# label with text "km"
km = Label(text="km")
km.grid(column=2, row=1)
km.config(pady=15)

# button for calculation
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
