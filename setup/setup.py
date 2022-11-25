import os
import tkinter as tk
from tkinter import messagebox
import time
root = tk.Tk()
root.title("cpm setup")
root.geometry("300x400")
import requests

url = "https://youtu.be/dQw4w9WgXcQ"
timeout = 5

tk.Label(root, text = "please wait untill setup finishes").pack(padx=10,pady=10)
def setup_fn():    
    os.system("pip install geopy")
    os.system("pip install customtkinter")
    os.system("pip install tkintermapview")
    os.system("pip install cachetools")
    os.system("pip install mysql-connector-python")
    os.system("pip install fpdf2")
    os.system("pip install tkVideo")
    time.sleep(3)
    root.destroy()

try:
    requests.get(url,timeout=timeout)
    tk.Button(root, text="INSTALL", command=setup_fn).pack(padx=10,pady=10)
except (requests.ConnectionError, requests.Timeout) as exception:
    messagebox.showerror("No internet connection", "oops looks like you don't have internet connection, connect to internet to complete your setup")

root.mainloop()
