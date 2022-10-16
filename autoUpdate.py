import dbms as db
import MandiData as md
import pickle

class AutoUpdate():
    
    def __init__(self,date):
        self.date = date
        self.miner_data = md.mined_data()
    def check_date(self,date):
        try:
            with open("secure/preDate.dat","rb") as _data:
                old_date = pickle.load(_data)
                if old_date == date:
                    return False
                else:
                    return True
        except:
            _db_date = open("secure/preDate.dat","wb")
            _data = pickle.dump(date, _db_date)
            _db_date.close()
            return True
    def checkAvailabilityOfData(self):
        x = self.date
        state = self.check_date(x)
        if state:
            try:
                with open("secure/preDbLogic.s","rb") as _data:
                    data = pickle.load(_data)
                    if data == True:
                        db.delete_old(self.date)
                        _date = open("secure/preDate.dat","wb")
                        pickle.dump()
                        return True
                    else:
                        return False
            except:
                db_state_data = open("secure/preDbLogic.dat","wb")
                _data = pickle.dump(True, db_state_data)
                db.delete_old(self.date)
                db_state_data.close()
                return True
        else:
            return False

    def insert_data_not_in_db(self):
        data = self.checkAvailabilityOfData()
        if data :
            for i in self.miner_data:
                try:
                    db.insertData(i)
                except:
                    pass
            

