from time import time
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import dbms as db
from datetime import date
import time
import autoUpdate as updater
from pprint import pprint 
today_ = str(date.today())
month_ = today_.split("-")[1]
date_ = today_.split("-")[2]
year_ =today_.split("-")[0]
today_ = date_+"/"+month_+"/"+year_
db.save_comodity_name()
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.title("Commodity price manager")
window.geometry("1000x600")
s = ttk.Style()
s.theme_use('clam')
hdg_label = tk.Label(window,text="Commodities Price Manager",bg="#1c1a1a",fg="white",font=("helvetica", 30))
hdg_label.pack(padx=20, pady=20)


coms_name_list = db.load_pickle_data()
coms_name_list.sort()

def get_suggestion_data():
    name = coms_combobox.get()
    result_data = []
    result_data.append(name)
    result_data.append(date) 
    main_to_result_window()
    return result_data  
def bar(x):
    x += 10    
    progress['value'] = x
    secondary_inner_window.update_idletasks()
    time.sleep(1)
    x += 10    
    progress['value'] = x
    secondary_inner_window.update_idletasks()
    time.sleep(1)
    x += 10    
    progress['value'] = x
    secondary_inner_window.update_idletasks()
    time.sleep(1)
    x += 10    
    progress['value'] = x
    secondary_inner_window.update_idletasks()
    time.sleep(1)
    x += 10    
    progress['value'] = x
    secondary_inner_window.update_idletasks()
    time.sleep(1)

def main_to_result_window():
    global secondary_inner_window, coms,progress
    coms = coms_combobox.get()
    innerWindow.destroy()
    secondary_inner_window = ctk.CTkFrame(window,width=700,height=200,corner_radius=10)
    secondary_inner_window.pack(padx=20, pady=20)
    s.configure("green.Horizontal.TProgressbar", foreground='green', background='green',)
    progress = ttk.Progressbar(secondary_inner_window, orient = tk.HORIZONTAL,length = 100, mode = 'determinate',style="green.Horizontal.TProgressbar")
    progress.pack(pady = 10)
    bar(10)
    updater.AutoUpdate(today_).insert_data_not_in_db()
    bar(50)
    progress.destroy()
    resulting_window()


def get_seleted_data():
    treeItem = tree.focus()
    data = tree.item(treeItem)["values"]
    return data



def resulting_window():
    global tree       
    tree = ttk.Treeview(secondary_inner_window, selectmode ='browse')
    tree.pack()
    
    tree["columns"] = tuple(range(1,10))
    tree['show'] = 'headings'
    for i in range(1, 10):
        if i in [8,2] :
                tree.column(i, width = 175, anchor="c")
        elif i in [3,9,4]:
                tree.column(i, width = 100, anchor="c")
        else:
                tree.column(i, width = 80, anchor="se")
    list_ = ["Date", "Commodity", "District", "Market", "max", "Min", "modal", "state", "variety"]
    for j in list_:
        tree.heading(list_.index(j) + 1, text = j)    
    result_set = db.getParticularData(coms, today_)
    for i in result_set:
        tree.insert("", 'end',values =(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
    tree.bind("show_location", get_seleted_data)
    show_location = ctk.CTkButton(master=window,text="SHOW MARKET IN MAP",command=get_seleted_data)
    show_location.pack(padx=10,pady=10)



def main_window():
    global coms_combobox,cal_box,innerWindow,date_label
    innerWindow = ctk.CTkFrame(window,width=300,height=200,corner_radius=10)
    innerWindow.pack(padx=20, pady=20)
    coms_combobox = ctk.CTkOptionMenu(master=innerWindow, values=coms_name_list)
    coms_combobox.pack(padx=20, pady=20)
    get_suggestion_btn = ctk.CTkButton(master=innerWindow, text="GET SUGGESTION",command=get_suggestion_data)
    get_suggestion_btn.pack(padx=20,pady=20)

main_window()
window.mainloop()
