# logic.py
import time
#defines the valid list of characters to be inputted or processed by the calculator
valid_chars = (".", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "/", "+", "-", "*")

#validates input
def valid_input(typing):
    return all(char in valid_chars for char in typing)

#runs the calculations
def calculations(entry_text, calculator=None):
    import time
    equationcalc = entry_text.get()
    if all(char in valid_chars for char in equationcalc):
        try:
            calculating = eval(equationcalc)
            entry_text.set(str(calculating))
        except Exception:
            entry_text.set("Error, numerical calculation error!")
            if calculator:
                calculator.update()
                time.sleep(0.75)
                entry_text.set("")
    else:
        entry_text.set("Error, invalid characters!")
        if calculator:
            calculator.update()
            time.sleep(0.75)
            entry_text.set("")

