import tkinter as tk
import customtkinter as ctk
import auth
from tkinter import messagebox
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")
auth_window = ctk.CTk()
auth_window.title("Commodity price manager")
auth_window.geometry("300x400")

auth_window.iconbitmap("resources/favicon.ico")
def ok():
    pop.destroy()

def error():
    global pop
    pop = ctk.CTkToplevel()
    pop_frame = ctk.CTkFrame(master=pop)
    pop_frame.pack(padx=20,pady=20)  
    error_img = ImageTk.PhotoImage(Image.open("resources/error.png").resize((50, 50)))
    error_msg= tk.Label(pop_frame,text="Opps username or password is invalid",bg="#292929", fg="white")
    error_msg.pack(padx=20,pady=20)
    ok_btn = ctk.CTkButton(master=pop_frame,text="ok",image=error_img,hover_color="gray25",compound="right",command=ok)
    ok_btn.pack(padx=20,pady=20)

def call_auth():
    auth_ = auth.auth(user_entry,pass_entry)
    if auth_:
        auth_window.destroy()
        import gui
        gui.main_window()

    else:
        user_entry.delete(0, tk.END)
        pass_entry.delete(0,tk.END)
        error()

auth_frame = ctk.CTkFrame(master = auth_window)
auth_frame.pack(padx=50,pady=50)
user_label = tk.Label(auth_frame, text="Enter user name", bg="#292929", fg="white")
user_label.pack(padx=20,pady=10,anchor="w")
user_entry = ctk.CTkEntry(master=auth_frame,placeholder_text="Enter username")
user_entry.pack(padx=20,pady=10,anchor="w")
pass_label = tk.Label(auth_frame, text="Enter password", bg="#292929",fg="white")
pass_label.pack(padx=20,pady=10,anchor="w")
pass_entry = ctk.CTkEntry(master=auth_frame,placeholder_text="Enter password")
pass_entry.pack(padx=20,pady=10,anchor="w")
auth_img = ImageTk.PhotoImage(Image.open("resources/auth.png").resize((20, 20)))
login_btn = ctk.CTkButton(master=auth_frame, text="Authenticate", command=call_auth,image=auth_img,compound="right", width=40,height=40,hover_color="gray25")
login_btn.pack(padx=20,pady=10,anchor="c")
auth_window.mainloop()
