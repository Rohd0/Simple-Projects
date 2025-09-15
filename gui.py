# gui.py

from tkinter import *
from tkinter import ttk
from logic import valid_input, calculations

# create the GUI window
calculator = Tk()
calculator.title("Calculator")
calculator.geometry("315x150")
calculator.configure(bg="gray")

# set up entry_text variable, this is used for calculations
entry_text = StringVar()

# register validation for truecalc
validi = calculator.register(valid_input)

# inserts the numbers/math operators if buttons clicked
def insertingnum(num):
    insertnum = entry_text.get()
    entry_text.set(insertnum + str(num))

# clears the text from the calculator
def clearingtext():
    entry_text.set("")

# wrapper for calculations
def run_calculations():
    calculations(entry_text, calculator)

# the area where numbers can be displayed/entered
truecalc = ttk.Entry(calculator, width=30, textvariable=entry_text, validate="key", validatecommand=(validi, "%P"))
truecalc.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
truecalc.focus()

# numerical buttons
button1 = ttk.Button(calculator, text="1", command=lambda: insertingnum(1))
button1.grid(row=1, column=0, padx=1, pady=1)
button2 = ttk.Button(calculator, text="2", command=lambda: insertingnum(2))
button2.grid(row=1, column=1, padx=1, pady=1)
button3 = ttk.Button(calculator, text="3", command=lambda: insertingnum(3))
button3.grid(row=1, column=2, padx=1, pady=1)
button4 = ttk.Button(calculator, text="4", command=lambda: insertingnum(4))
button4.grid(row=2, column=0, padx=1, pady=1)
button5 = ttk.Button(calculator, text="5", command=lambda: insertingnum(5))
button5.grid(row=2, column=1, padx=1, pady=1)
button6 = ttk.Button(calculator, text="6", command=lambda: insertingnum(6))
button6.grid(row=2, column=2, padx=1, pady=1)
button7 = ttk.Button(calculator, text="7", command=lambda: insertingnum(7))
button7.grid(row=3, column=0, padx=1, pady=1)
button8 = ttk.Button(calculator, text="8", command=lambda: insertingnum(8))
button8.grid(row=3, column=1, padx=1, pady=1)
button9 = ttk.Button(calculator, text="9", command=lambda: insertingnum(9))
button9.grid(row=3, column=2, padx=1, pady=1)
button0 = ttk.Button(calculator, text="0", command=lambda: insertingnum(0))
button0.grid(row=4, column=0, padx=1, pady=1)

# buttons for operations
buttonplus = ttk.Button(calculator, text="+", command=lambda: insertingnum("+"))
buttonplus.grid(row=1, column=3, padx=1, pady=1)
buttonminus = ttk.Button(calculator, text="-", command=lambda: insertingnum("-"))
buttonminus.grid(row=2, column=3, padx=1, pady=1)
buttonmulti = ttk.Button(calculator, text="*", command=lambda: insertingnum("*"))
buttonmulti.grid(row=3, column=3, padx=1, pady=1)
buttondivide = ttk.Button(calculator, text="/", command=lambda: insertingnum("/"))
buttondivide.grid(row=4, column=3, padx=1, pady=1)
buttonc = ttk.Button(calculator, text="C", command=clearingtext)
buttonc.grid(row=4, column=1, padx=1, pady=1)
buttoneq = ttk.Button(calculator, text="=", command=run_calculations)
buttoneq.grid(row=4, column=2, padx=1, pady=1)

# additional keyboard bindings
calculator.bind("<Return>", lambda event: run_calculations())
calculator.bind("c", lambda event: clearingtext())

calculator.mainloop()