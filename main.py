import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("NBI SRT Launcher")
root.geometry("400x120")
root.resizable(False, False)

observatory_launcher = Planisphere(root)

observatory_launcher.mainloop()