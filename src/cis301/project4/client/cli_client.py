#TODO Implement the client application
import json

import requests

from cis301.project4.phonecall import PhoneCall
from cis301.project4.util import Util


class PhoneBillClient():

    def __init__(self, username, password, hostname="localhost", port="8000"):
        self.__host = hostname
        self.__port = port
        self.__uname = username
        self.__password = password


    def get_username(self):
        return self.__uname

    def get_password(self):
        return self.__password

    def set_username(self, uname):
         self.__uname = uname

    def set_password(self, passwd):
         self.__password = passwd

    def register_user(self):
        raise NotImplementedError ("Cannot register user!")


    def add_phonecall(self, phonecall):
        # convert data to JSON
        phonecallJSON = Util.phonecallToJSON(phonecall, True)
        #generate a request
        #every request needs authentication
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email":f"{self.__uname}", "password":f"{self.__password}", "client":True}

        headers={'content-type':'application/json',}
        auth_res = requests.post( url, data=json.dumps(data), headers= headers )

        # check response
        print( auth_res )
        print( auth_res.text )
        # send request (POST)
        url = 'http://'+self.__host+':'+self.__port+'/user/add'
        res = requests.post(url, data=json.dumps(phonecallJSON), cookies=auth_res.cookies,headers=headers )

        #check response
        print(res)
        print( res.text )

        if json.loads(res.text)['res'] == "200":
            print(f"Added a new phone call: {phonecall.__str__()}")
        else:
            print("Operation Failed: could not add a new record \n\t{json.loads(res.text)['res']}")

    def del_phonecall(self, phonecall_id):
        # convert data to JSON
        #generate a request
        #every request needs authentication
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email":f"{self.__uname}", "password":f"{self.__password}", "client":True}

        headers={'content-type':'application/json',}
        auth_res = requests.post( url, data=json.dumps(data), headers= headers )


        url = 'http://'+self.__host+':'+self.__port+'/user/delete'
        res = requests.post(url, data=json.dumps({"phonecall_id":str(phonecall_id)}), cookies=auth_res.cookies,headers=headers )
        if json.loads( res.text )['res'] == '200':
            print(f'Phone call {phonecall_id} deleted!')
        else:
            print(f"Operation Failed: could not delete the phone call record {phonecall_id}\n\t{json.loads( res.text )['res']}")

        #check response
        print(res)
        print( res.text )

    def update_phonecall(self, phonecall_id):
        # convert data to JSON
        phonecallJSON = Util.phonecallToJSON(phonecall, True)
        # generate a request
        # every request needs authentication
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email": f"{self.__uname}", "password": f"{self.__password}", "client": True}

        headers = {'content-type': 'application/json', }
        auth_res = requests.post(url, data=json.dumps(data), headers=headers)



if __name__== '__main__':
    username = "morgan@cau.edu"
    password = "123456"
    phonecall = PhoneCall('404-880-4567', '404-880-9632', '11/11/2020 15:10', '11/11/2020 15:25')
    pbc = PhoneBillClient(username, password)
    pbc.set_username(username)
    pbc.set_password(password)
    pbc.add_phonecall(phonecall)
    #if you comment out the delete function it runs(i think it's because there is nothing to delete because of the value?
    pbc.del_phonecall(phonecall)

