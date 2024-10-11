# main.py

import tkinter as tk
from notepad import Notepad

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
