import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("600x400")

        # Add a text area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Create a menu
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.file_name = None
        self.create_widgets()

    def create_widgets(self):
        # File Menu
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Edit Menu
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Help Menu
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

    # File Functions
    def new_file(self):
        self.file_name = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        self.file_name = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_name:
            with open(self.file_name, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        if self.file_name:
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_name, "w") as file:
                file.write(content)
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_name = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_name:
            content = self.text_area.get(1.0, tk.END)
            with open(self.file_name, "w") as file:
                file.write(content)

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.root.quit()

    # Edit Functions
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    # Help Function
    def show_about(self):
        messagebox.showinfo("About", "Simple Notepad using Tkinter")
