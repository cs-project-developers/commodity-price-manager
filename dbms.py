import mysql.connector as mc
import MandiData as md
import pickle
import os
from datetime import date
today_ = str(date.today())
today_ = today_.split("-")
today_ = today_[2] +"/"+ today_[1] +"/"+ today_[0]


def establishCon():
    con = mc.connect(host="localhost",user="root",password="rocky2005", database="cpm")
    return con

def checkCon(connection):
    try:
        if connection.is_connected():
            createTable()
            return True
        else:
            return False
    except:
        con = mc.connect(host="localhost",user="root",password="rocky2005")
        cur=con.cursor()
        cur.execute("create database cpm")
        cur.commit()
        con.close()
        establishCon()
        createTable()



def createTable():
    try:
        cur=establishCon().cursor()
        cur.execute('CREATE TABLE [IF NOT EXISTS] "cpm_data" ("arrival_date"	DATE NOT NULL,"commodity"	VARCHAR(50) NOT NULL,"district"	VARCHAR(50) NOT NULL,"market"	VARCHAR(50) NOT NULL,"max_price"	INT NOT NULL,"min_price"	INT NOT NULL,"modal_price"	INT NOT NULL,"state"	VARCHAR(50) NOT NULL,"variety"	VARCHAR(50) NOT NULL)')
        cur.commit()
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
    cur.execute(f'select * from cpm_data where commodity = "{commodity}" and arrival_date = "{date}"')
    result_set = cur.fetchall()
    return result_set

def get_max_price_cmd(date, commodity):
    con = establishCon()
    cur = con.cursor()
    command = f'select max_price , market from cpm_data where commodity="{commodity}" and arrival_date="{date}"order by max_price desc limit 1'
    cur.execute(command)
    result = cur.fetchall()
    return result[0]


def save_comodity_name():
    data_pack = md.commodity_name_list()  
    try:
        data_pickle = open("preLoader_data.dat","wb")
        loaded_data = pickle.load(data_pickle)    
        for data in data_pack:
            if data not in loaded_data:
                loaded_data.append(data)
        pickle.dump(loaded_data, data_pickle)   
        data_pickle.close() 
    except:
        
        data_pickle = open("preLoader_data.dat", "wb")
        pickle.dump(data_pack, data_pickle)
        data_pickle.close()

            
def load_pickle_data():
    if os.path.exists('/preLoader_data.dat'):
        with open("preLoader_data.dat", 'rb') as data:
            data_set = pickle.load(data)
        
    else:
        save_comodity_name()
        with open("preLoader_data.dat", 'rb') as data:
            data_set = pickle.load(data)

    return data_set




