import sqlite3
import uuid
from hashlib import md5

from cis301.phonebill.phonebill_doa import AbstractPhoneBill_DOA
from cis301.phonebill.phonecall_doa import AbstractPhoneCall_DOA

# TODO Finish Implementing the abstract methods

class PhoneBill_DOA(AbstractPhoneBill_DOA, AbstractPhoneCall_DOA):
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def insert_phonebill(self, phonebill):
        pass

    def update_phonebill(self, phonebill):
        pass

    def delete_phonebill(self, phonebill):
        pass

    def select_phonebill(self, phonebill_id):
        pass

    def search_phonebills_bydate(self, startdate, enddate):
        pass

    def insert_phonecall(self, phonecall):
        conn = sqlite3.connect( self.dbfile )
        c = conn.cursor()
        data = (phonecall.get_caller(), phonecall.get_callee(), phonecall.get_starttime_string(), phonecall.get_endtime_string())
        c.execute( 'INSERT INTO phonecalls ( caller,callee, startdate, enddate) VALUES (?,?,?,?);', data )
        conn.commit()
        pid = c.lastrowid
        data = (phonecall.get_uid(), pid)
        c.execute( 'INSERT INTO phonebills ( uid, pid ) VALUES (?,?);', data )
        conn.commit()
        conn.close()
        return pid

    def update_phonecall(self, phonecall):
        pass

    def delete_phonecall(self, phonecall):
        pass

    def select_phonecall(self, phonecall_id):
        pass

    def search_phonecalls_bydate(self, startdate, enddate):
        pass

    def search_phonecalls_bycustomername(self, customer_id):
        pass



    def insert_user(self, user):
        if not self.is_user_exists(user):
            conn = sqlite3.connect(self.dbfile)
            c = conn.cursor()
            data = (user["id"], user["name"], user["email"],user["password"])
            c.execute('INSERT INTO users (id, name,email, password) VALUES (?,?,?,?);', data)
            conn.commit()
            conn.close()
            return  True
        else:
            return False

    def authenticate_user(self,user):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        #passwd = str(md5(user['password'].encode()).digest())
        c.execute('select * from users where users.email=? and users.password=?', (user["email"] , user['password']))
        if c.fetchone():
            conn.close()
            return True
        else:
            conn.close()
            return False

    def get_user_by_email(self, user):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from users where users.email=?', (user["email"],))
        return c.fetchone()

    def is_user_exists(self, user):
        conn = sqlite3.connect(self.dbfile)
        c = conn.cursor()
        c.execute('select * from users where users.email=?', (user["email"],))
        rows =c.fetchone()
        if rows:
            return True
        else:
            return False
#TODO  Implement Data Object Access(DOA) functionalities for Phonebills and PhoneCalls


if __name__ == '__main__':
    doa = PhoneBill_DOA('../data/phonebill.db')
    user = dict()
    user['id'] = str(uuid.uuid4())
    user['email'] = 'abc@abc.com'
    user['name']="Test User"
    user['password'] = "123456"
    user['password'] = str(md5(user['password'].encode()).digest())
    doa.insert_user(user)
    print(doa.is_user_exists(user))