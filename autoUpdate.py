import dbms as db
import MandiData as md

class AutoUpdate():

    def __init__(self,date):
        self.date = date
        self.buffer_data = db.getDbData()
        self.miner_data = md.mined_data()
        

    def checkAvailabilityOfData(self):
        db_state = False
        for i in self.buffer_data:
            if self.date in i:
                db_state = True
            else:
                db_state = False
        return db_state
    
    def insert_data_not_in_db(self):
        data = self.checkAvailabilityOfData()
        if data ==False :
            for i in self.miner_data:
                try:
                    db.insertData(i)
                except:
                    pass
            
    
    

     



