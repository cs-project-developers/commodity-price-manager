import os
import tkinter as tk
from tkvideo import tkvideo
import customtkinter as ctk
import auth
from PIL import Image, ImageTk
from datetime import date
import pickle
import requests
import webbrowser
today_ = str(date.today())
month_ = today_.split("-")[1]
date_ = today_.split("-")[2]
year_ =today_.split("-")[0]
today_ = date_+"/"+month_+"/"+year_
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")
auth_window = ctk.CTk()
auth_window.title("Commodity price manager")
auth_window.geometry("350x550")

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
    global pass_entry, user_entry
    auth_ = auth.auth(user_entry,pass_entry)
    if auth_:
        if write_token_state:
            file_token = open("secure/bhuvanToken.dat","wb")
            pickle.dump(bhuvan_entry.get(),file_token)
            file_token.close()
        auth_window.destroy()
        import gui
        gui.main_window()

    else:
        user_entry.delete(0, tk.END)
        pass_entry.delete(0,tk.END)
        error()
write_token_state = False
def bhuvan_field():
    global bhuvan_entry, write_token_state
    if os.path.exists("secure/prebhuvandate.dat") and os.path.exists("secure/bhuvanToken.dat"):
        date_field = open("secure/prebhuvandate.dat","rb")
        date__ = pickle.load(date_field)
        if date__ == today_:
            date_field.close()
        else:
            write_token_state = True
            date_field = open("secure/prebhuvandate.dat","wb")
            pickle.dump(today_,date_field)
            bhuvan_label = tk.Label(auth_frame, text="Enter bhuvan token: ", bg="#292929",fg="white")
            bhuvan_label.pack(padx=20,pady=10,anchor="w")
            bhuvan_entry = ctk.CTkButton(auth_frame,placeholder_text="Bhuvan Token")
            bhuvan_entry.pack(padx=20,pady=10,anchor="w")
            date_field.close()

    else:
        write_token_state = True
        date_field = open("secure/prebhuvandate.dat","wb")
        pickle.dump(today_,date_field)
        bhuvan_label = tk.Label(auth_frame, text="Enter bhuvan token: ", bg="#292929",fg="white")
        bhuvan_label.pack(padx=20,pady=10,anchor="w")
        bhuvan_entry = ctk.CTkEntry(auth_frame,placeholder_text="Bhuvan Token")
        bhuvan_entry.pack(padx=20,pady=10,anchor="w")
        get_api = tk.Label(auth_frame, text="click below button.. for Token", bg="#292929",fg="white")
        get_api.pack(padx=10,pady=10)
        get_byn = ctk.CTkButton(master=auth_frame,text="Get Token",command=visit)
        get_byn.pack(padx=10,pady=10)
        date_field.close()

def help():
    help_win = ctk.CTkToplevel(auth_window)
    help_win.title("cpm help window")
    frame_help = ctk.CTkFrame(help_win)
    frame_help.pack(padx=10,pady=10)
    video_label = tk.Label(frame_help)
    video_label.pack(padx=10,pady=10)
    player = tkvideo("resources\\token_tutorial.mp4",video_label , loop = 0, size = (720,460))
    player.play()
    labell = tk.Label(frame_help, text="conatct the developers for more help | gamil: csprojectmailid@gmail.com", bg="#292929", fg="white").pack(side=tk.BOTTOM,padx=10,pady=10)

def visit():
    url = "https://bhuvan-app1.nrsc.gov.in/api/#"
    webbrowser.open(url, new=2)
    
help_btn = ctk.CTkButton(master=auth_window,text="help?",command=help,hover_color="purple",width=30)
help_btn.place(x=290,y=5)#pack(padx=10,pady=10,side=tk.RIGHT)
pswd_state = False
auth_frame = ctk.CTkFrame(master = auth_window)
auth_frame.pack(padx=50,pady=50)
user_label = tk.Label(auth_frame, text="Enter user name", bg="#292929", fg="white")
user_label.pack(padx=20,pady=10,anchor="w")
user_entry = ctk.CTkEntry(master=auth_frame,placeholder_text="Enter username")

user_entry.pack(padx=20,pady=10,anchor="w")

pass_label = tk.Label(auth_frame, text="Enter password", bg="#292929",fg="white")
open_eye = ImageTk.PhotoImage(Image.open("resources\open_eye.png").resize((20, 20)))
closed_eye = ImageTk.PhotoImage(Image.open("resources\eye-closed.png").resize((20, 20)))
show_pass = ctk.CTkButton(master=auth_frame,text="", image=open_eye,compound="top", hover_color="gray25",width=40,command=show_pswd)
show_pass.pack(padx=1,side=tk.RIGHT)
pass_label.pack(padx=20,pady=10,anchor="w")
pass_entry = ctk.CTkEntry(master=auth_frame,placeholder_text="Enter password", show="#")
pass_entry.pack(padx=20,pady=10,anchor="w")

auth_img = ImageTk.PhotoImage(Image.open("resources/auth.png").resize((20, 20)))
bhuvan_field()
login_btn = ctk.CTkButton(master=auth_frame, text="Authenticate", command=call_auth,image=auth_img,compound="right", width=60,height=40,hover_color="gray25")
login_btn.pack(padx=20,pady=10,anchor="c")

auth_window.mainloop()
