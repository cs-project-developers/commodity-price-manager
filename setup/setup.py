import os
import tkinter as tk
from tkinter import messagebox
import time
root = tk.Tk()
root.title("cpm setup")
import requests

url = "https://youtu.be/dQw4w9WgXcQ"
timeout = 5

tk.Label(root, text = "please wait untill setup finishes").pack(padx=10,pady=10)
def setup_fn():    
    tk.Label(root, text="installation started").pack(padx=10,pady=10)
    os.system("pip install geopy")
    tk.Label(root, text="geopy installed ...").pack(padx=10, pady=10)
    os.system("pip install customtkinter")
    tk.Label(root, text="customtkinter installed ...").pack(padx=10,pady=10)
    os.system("pip install tkintermapview")
    tk.Label(root, text="Tkintermapview installed ...").pack(padx=10,pady=10)
    os.system("pip install cachetools")
    tk.Label(root, text="cachetools installed ...").pack(padx=10,pady=10)
    os.system("pip install mysql-connector")
    tk.Label(root, text="mysql-connector installed ...").pack(padx=10,pady=10)
    os.system("pip install fpdf2")
    tk.Label(root, text="fpdf2 installed ...").pack(padx=10,pady=10)
    tk.Label(root, text="INstallation completed").pack(padx=10,pady=10)
    tk.Label(root, text="closing in 3 sec").pack(padx=10,pady=10)
    time.sleep(3)
    root.destroy()

try:
    requests.get(url,timeout=timeout)
    tk.Button(root, text="INSTALL", command=setup_fn).pack(padx=10,pady=10)
except (requests.ConnectionError, requests.Timeout) as exception:
    messagebox.showerror("No internet connection", "oops looks like you don't have internet connection, connect to internet to complete your setup")

root.mainloop()
