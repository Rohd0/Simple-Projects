# testing.py

import pytest
import time
import tkinter
from tkinter import ttk
from logic import valid_input, calculations
from tkinter import *


# checking if expressions are properly calculated
def test_calculations_pass():
    root = Tk()
    entry_text = StringVar()
    entry_text.set("((20 + 41) - 3)")
    calculations(entry_text, root)
    assert entry_text.get() == str(58)
    root.destroy()

def test_calculations_fail():
    root = Tk()
    entry_text = StringVar()
    entry_text.set("((20 + 41) - 3)-2")
    calculations(entry_text, root)
    assert entry_text.get() != str(58)
    root.destroy()

def test_calculations_division0():
    root = Tk()
    entry_text = StringVar(master=root)
    entry_text.set("20/0")
    calculations(entry_text, calculator=None)
    assert "Error" in entry_text.get()
    root.destroy()


def test_valid_input_pass():
    assert valid_input( "((51*23)+46/7)-89.0 ") is True

# a test case involving alphabets
def test_valid_input_fail():
    assert valid_input("123 + 2 + x - y - z") is False