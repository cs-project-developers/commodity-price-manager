from time import time
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import dbms as db
from datetime import date
import time
import autoUpdate as updater
import geologic as geo
import tkintermapview
import webbrowser
from pprint import pprint 
from PIL import Image, ImageTk

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
window.geometry("1000x650")
hdg_label = tk.Label(window,text="Commodities Price Manager",bg="#1c1a1a",fg="white",font=("helvetica", 30))
hdg_label.pack(padx=20, pady=20)


coms_name_list = db.load_pickle_data()
coms_name_list.sort()

def get_suggestion_data():
    global name
    name = coms_combobox.get()
    result_data = []
    result_data.append(name)
    result_data.append(date) 
    main_to_result_window()
    return result_data  

def open_click():
    url = f"https://www.google.com/maps/dir/{geo.user_current_location[0]},{geo.user_current_location[1]}/{loc}/"
    webbrowser.open(url, new=2)
    dir_pop.destroy()
    
def direction():
    global dir_pop
    dir_pop = ctk.CTkToplevel()
    frame_work = ctk.CTkFrame(master=dir_pop)
    label = tk.Label(frame_work, text="click the bellow button to get your direction", bg="#292929", font=("Monotype Baskerville Italic", 15), fg="white")
    label.pack(padx=10, pady=10)
    dir_btn = ctk.CTkButton(master=frame_work, text="Click here", command=open_click)
    dir_btn.pack(padx=10, pady=10)
    frame_work.pack(padx=10, pady=10)


def change_sat_view():
    global nor_btn
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    sat_btn.destroy()
    nor_btn = ctk.CTkButton(master=map_frame, text="Normal map view", command=change_nor_view)
    nor_btn.pack(padx=10, pady=10)
    
def change_nor_view():
    global sat_btn
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    nor_btn.destroy()
    sat_btn = ctk.CTkButton(master=map_frame, text="Satellite view", command=change_sat_view)
    sat_btn.pack(padx=10, pady=10)

def set_anchor():
    map_widget.set_address(loc+",india")

def map_view():
    global loc,map_widget,sat_btn,map_frame
    map_widget = tkintermapview.TkinterMapView(map_frame, width=800, height=350, corner_radius=0)
    m_prog.destroy()
    map_widget.pack()
    loc = treedata[3]
    try:
        loc=loc.split(" ")[0]+loc.split(" ")[1]
    except:
        pass
    map_widget.set_address(loc+",india")
    map_widget.set_address(loc+",india", marker=True)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=10)
    anchor_img = ImageTk.PhotoImage(Image.open("resources/gps.png").resize((20, 20)))
    anchor_point_btn = ctk.CTkButton(master=map_frame, image=anchor_img,command=set_anchor,compound="right",text="", width=40,height=40,hover_color="gray25")
    anchor_point_btn.pack(padx=10, pady=10, anchor="e")
    dir_img = ImageTk.PhotoImage(Image.open("resources/location.png").resize((20, 20)))
    show_dir = ctk.CTkButton(master=map_frame, text="Get Direction", command=direction,image=dir_img,compound="right", width=40,height=40,hover_color="gray25")
    show_dir.pack(padx=10, pady=10)
    sat_btn = ctk.CTkButton(master=map_frame, text="Satellite view", command=change_sat_view)
    sat_btn.pack(padx=10, pady=10)
    map_widget.set_zoom(5)

def bar(progress_bar,window_frame,x):
    x += 0.1    
    progress_bar.set(x)
    window_frame.update_idletasks()
    time.sleep(0.25)
    x += 0.1    
    progress_bar.set(x)
    window_frame.update_idletasks()
    time.sleep(0.25)
    x += 0.1    
    progress_bar.set(x)
    window_frame.update_idletasks()
    time.sleep(0.25)
    x += 0.1    
    progress_bar.set(x)
    window_frame.update_idletasks()
    time.sleep(0.25)
    x += 0.1    
    progress_bar.set(x)
    window_frame.update_idletasks()
    time.sleep(0.25)
    progress_bar.set(x)

def main_to_result_window():
    global secondary_inner_window, coms,progress,result_set, short_dist, max_dist,max_price,max_mar
    coms = coms_combobox.get()
    innerWindow.destroy()
    secondary_inner_window = ctk.CTkFrame(window,width=700,height=200,corner_radius=10)
    secondary_inner_window.pack(padx=20, pady=20)
    progress = ctk.CTkProgressBar(secondary_inner_window,width = 650,height=25)
    progress.pack(padx=100,pady=100)
    progress.set(0)
    bar(progress,secondary_inner_window,0)
    updater.AutoUpdate(today_).insert_data_not_in_db()
    result_set = db.getParticularData(coms, today_)
    locations_list = []
    price_list = []
    for i in result_set:
	    locations_list.append(i[3])
	    price_list.append(i[4])
    short_dist = geo.generate_shortest_dist(locations_list)
    max_result = db.get_max_price_cmd(today_,name)
    max_price = max_result[0]
    max_mar = max_result[1]
    max_dist = geo.get_distance(geo.user_current_location,geo.get_long_lat(max_mar))
    
    

    bar(progress,secondary_inner_window,0.5)
    progress.destroy()
    resulting_window()




def get_seleted_data():
    global treedata
    treeItem = tree.focus()
    treedata = tree.item(treeItem)["values"]
    result_map_window()


def result_map_window():
    global map_frame, m_prog
    secondary_inner_window.destroy()
    show_location.destroy()
    short_frame.destroy()
    download_data.destroy()
    map_frame = ctk.CTkFrame(window,width=700,height=200,corner_radius=10)
    map_frame.pack(padx=10,pady=10)
    m_prog = ctk.CTkProgressBar(map_frame,width = 650,height=25)
    m_prog.pack(padx=20,pady=20)
    bar(m_prog, map_frame,0.2)
    m_prog.set(1)
    map_view()




def shortest_result(location,price,pri_location, pri_dist):
    global short_frame
    short_frame = ctk.CTkFrame(master=window,width=700,height=200,corner_radius=10)
    short_frame.pack(padx=10, pady=10)
    short_label = tk.Label(short_frame, text=f"The nearest market is {location[0]} with distance {location[1]}",bg="#292929",fg="white",font=("helvetica", 15),wraplength=650)
    short_label.pack(padx=20,pady=20)
    max_profit_label = tk.Label(short_frame,text=f"The market {pri_location} has the maximim price of {price} for your commodity is of  distance {pri_dist} km away from your current location.",bg="#292929",fg="white",font=("helvetica", 15),wraplength=650)
    max_profit_label.pack(padx=20,pady=20)


def resulting_window():
    global tree,download_data, show_location       
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
    for i in result_set:
        tree.insert("", 'end',values =(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
    tree.bind("show_location", get_seleted_data)
    map_img = ImageTk.PhotoImage(Image.open("resources/map.png").resize((20, 20)))
    show_location = ctk.CTkButton(master=window,text="SHOW MARKET IN MAP",command=get_seleted_data,image=map_img,compound="right", width=40,height=40,hover_color="gray25")
    show_location.pack(padx=10,pady=10)
    down_img = ImageTk.PhotoImage(Image.open("resources/download.png").resize((20, 20)))
    download_data = ctk.CTkButton(master=window,text="DOWNLOAD YOUR SUGGESTION",image=down_img,compound="right", width=40,height=40,hover_color="gray25")
    download_data.pack(padx=10,pady=10)
    shortest_result(short_dist,max_price,max_mar,max_dist)



def main_window():
    global coms_combobox,cal_box,innerWindow,date_label
    innerWindow = ctk.CTkFrame(window,width=300,height=200,corner_radius=10)
    innerWindow.pack(padx=20, pady=20)
    coms_combobox = ctk.CTkOptionMenu(master=innerWindow, values=coms_name_list)
    coms_combobox.pack(padx=20, pady=20)
    sugest_img = ImageTk.PhotoImage(Image.open("resources/sugesstion.png").resize((40, 40)))
    get_suggestion_btn = ctk.CTkButton(master=innerWindow, text="GET SUGGESTION",command=get_suggestion_data,image=sugest_img,compound="top",height=80,hover_color="gray25")
    get_suggestion_btn.pack(padx=20,pady=20)

main_window()
window.mainloop()
