import tkinter as tk
import customtkinter as ctk
import auth
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")
auth_window = ctk.CTk()
auth_window.title("Commodity price manager")
auth_window.geometry("350x400")

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

def show_pswd():
    global pswd_state,closed_eye,open_eye,show_pass
    if pswd_state != True:
        pswd_state = True
        
        pass_entry.configure(show="")
        show_pass.configure(image=closed_eye)

    else:
        pswd_state=False
        pass_entry.configure(show="#")
        show_pass.configure(image=open_eye)

    



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

pswd_state = False
auth_frame = ctk.CTkFrame(master = auth_window)
auth_frame.pack(padx=50,pady=50)
user_label = tk.Label(auth_frame, text="Enter user name", bg="#292929", fg="white")
user_label.pack(padx=20,pady=10,anchor="w")
user_entry = ctk.CTkEntry(master=auth_frame,placeholder_text="Enter username")
user_entry.pack(padx=20,pady=10,anchor="w")
pass_label = tk.Label(auth_frame, text="Enter password", bg="#292929",fg="white")
pass_label.pack(padx=20,pady=10,anchor="w")
pass_entry = ctk.CTkEntry(master=auth_frame,placeholder_text="Enter password", show="#")
pass_entry.pack(padx=20,pady=10,anchor="w")
open_eye = ImageTk.PhotoImage(Image.open("resources\open_eye.png").resize((20, 20)))
closed_eye = ImageTk.PhotoImage(Image.open("resources\eye-closed.png").resize((20, 20)))
show_pass = ctk.CTkButton(master=auth_frame,text="", image=open_eye,compound="top", hover_color="gray25",width=40,command=show_pswd)
show_pass.pack(padx=10,pady=10,side=tk.RIGHT)
auth_img = ImageTk.PhotoImage(Image.open("resources/auth.png").resize((20, 20)))
login_btn = ctk.CTkButton(master=auth_frame, text="Authenticate", command=call_auth,image=auth_img,compound="right", width=60,height=40,hover_color="gray25")
login_btn.pack(padx=20,pady=10,anchor="c")
auth_window.mainloop()
