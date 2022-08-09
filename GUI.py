import tkinter as tk
import customtkinter as ctk
import tkintermapview

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.title("Commodity price manager")
window.geometry("690x420")



hdg_label = tk.Label(window, text="Commodities Price Manager", bg="#1c1a1a",fg="white", font=("helvetica", 30))
hdg_label.pack(padx=20, pady=20)
inputsFrame = ctk.CTkFrame(master=window,width=600,height=200,corner_radius=10,fg_color="#2b2a33")
inputsFrame.pack(padx=20, pady=20)
comName_label = tk.Label(inputsFrame, text="enter your commodity name :", bg="#2b2a33",fg="white")
comName_label.pack(padx=10,pady=5, anchor=tk.W)
inputProduct = ctk.CTkEntry(master=inputsFrame,width=600,placeholder_text="Enter your commodity")
inputProduct.pack(padx=10, pady=5)
btn = ctk.CTkButton(master=inputsFrame, text="GET MARKETS")
btn.pack(padx=20, pady=10)


window.mainloop()
