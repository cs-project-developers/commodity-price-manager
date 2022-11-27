import pickle
import mysql.connector as mc

def auth(user_entry, pass_entry):
    user = user_entry.get()  
    pswd = pass_entry.get()
    if user == "":
        user = "root"
    else:
        pass
    if pswd == "":
        return False 
    else:
        pass
    data = open("secure/auth.dat", "wb")
    auth_data = [user,pswd]
    pickle.dump(auth_data, data)
    data.close()
    try:
        con = mc.connect(user=user,host="localhost",password=pswd)
        return con.is_connected()
    except:

        return False


def get_auth():
    with open("secure/auth.dat","rb") as auth:
        data = pickle.load(auth)
        user = data[0]
        pswd = data[1]
    return user, pswd

    
    




