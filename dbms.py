import mysql.connector as mc
import requests
from tkinter import messagebox
url = "https://youtu.be/dQw4w9WgXcQ"
timeout = 5
try:
    requests.get(url,timeout=timeout)
    import MandiData as md
    pass
except (requests.ConnectionError, requests.Timeout) as exception:
    messagebox.showerror("No internet connection", "oops looks like you don't have internet connection, connect to internet to complete your setup and restart the program")
import pickle
import os
from datetime import date
import auth 
today_ = str(date.today())
today_ = today_.split("-")
today_ = today_[2] +"/"+ today_[1] +"/"+ today_[0]

user, pswd = auth.get_auth()
def establishCon():
    con = mc.connect(host="localhost",user=user,password=pswd, database="cpm")
    return con

def checkCon():
    try:
        connection = mc.connect(host="localhost",user=user,password=pswd, database="cpm")
        if connection.is_connected():
            createTable()
            return True
        else:
            return False
    except:
        con = mc.connect(host="localhost",user=user,password=pswd)
        cur=con.cursor()
        cur.execute("create database cpm")
        con.commit()
        con.close()
        establishCon()
        createTable()



def createTable():
    try:
        con=establishCon()
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS cpm_data(arrival_date	VARCHAR(10) NOT NULL,commodity	VARCHAR(50) NOT NULL ,district VARCHAR(50) NOT NULL,market	VARCHAR(50) NOT NULL,max_price	FLOAT NOT NULL,min_price VARCHAR(10) NOT NULL,modal_pricE VARCHAR(10) NOT NULL,state	VARCHAR(50) NOT NULL,variety VARCHAR(50) NOT NULL)')
        con.commit()
        establishCon().close()
    except:
        return None



def insertData(data):
    date =data["arrival_date"]
    commodity=data["commodity"]
    district = data["district"]
    market = data["market"]
    max_price = data["max_price"]
    min_price =data["min_price"]
    modal_price = data["modal_price"]
    state = data["state"]
    variety = data["variety"]
    con=establishCon()
    cur=con.cursor()
    cur.execute(f'INSERT INTO cpm_data VALUES("{date}", "{commodity}", "{district}", "{market}", {float(max_price)}, {min_price}, {modal_price}, "{state}", "{variety}")')
    con.commit()
    con.close()




def getDbData():
    con=establishCon()
    cur=con.cursor()
    cur.execute("select * from cpm_data")
    data = cur.fetchall()
    return data


def getParticularData(commodity, date = today_):
    con = establishCon()
    cur = con.cursor()
    com = f'select * from cpm_data where commodity = "{commodity}" and arrival_date = "{date}"'
    cur.execute(com)
    result_set = cur.fetchall()
    return result_set

def get_max_price_cmd(date, commodity):
    con = establishCon()
    cur = con.cursor()
    command = f'select max_price , market from cpm_data where commodity="{commodity}" and arrival_date="{date}"order by max_price desc limit 1'
    cur.execute(command)
    result = cur.fetchall()
    return result[0]


def delete_old(date):
    con = establishCon()
    cur = con.cursor()
    command = f'DELETE FROM cpm_data WHERE arrival_date != "{date}"'
    try:
        cur.execute(command)
        con.commit()
    except:
        pass
    con.close()
def save_comodity_name():
    data_pack = md.commodity_name_list()
    data_pickle = open("secure/preLoader_data.dat", "wb")
    pickle.dump(data_pack, data_pickle)
    data_pickle.close()


def load_pickle_data():
    if os.path.exists('secure/preLoader_data.dat'):
        with open("secure/preLoader_data.dat", 'rb') as data:
            data_set = pickle.load(data)
        
    else:
        save_comodity_name()
        with open("secure/preLoader_data.dat", 'rb') as data:
            data_set = pickle.load(data)
    
    result = []
    for i in data_set:
        result.append(i["commodity"])
    output = []
    for x in result:
        if x not in output:
            output.append(x)
    output.sort()
    return output

checkCon()