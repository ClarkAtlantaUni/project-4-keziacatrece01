import json
import os
import pathlib
from datetime import datetime

from cis301.project4.server.db.sqlite_doa import PhoneBill_DOA
from flask import Flask, request, redirect, render_template, g, session
from flask_bootstrap import Bootstrap

class PhoneBillServer(Flask):
    def __init__(self,import_name,port=8000, file='database.txt', host='localhost'):
        super().__init__(import_name, instance_path=pathlib.Path(__file__).parent.absolute())
        self.__port = port
        self.__host = host
        self.__datalocation = os.path.join(self.instance_path, 'data')
        self.__file =  os.path.join(self.__datalocation, file)
        self.__userdb = os.path.join(self.__datalocation, "userdb.txt")
        self.__dbfilename = "phonebill.db"
        self.__db = PhoneBill_DOA(os.path.join(self.__datalocation, self.__dbfilename))

    def set_file(self, file):
        self.file = self.__datalocation + file

    def get_file(self):
        return self.__file

    def set_port(self,port):
        self.__port = port

    def get_port(self):
        return self.__port

    def get_userdb(self):
        return self.__db

    def add_record(self, phonebill):
       #TODO
        jsondata = ""
        with open( self.__file, "a" ) as database:
            # assuming JSON content
            jsondata = json.load( database )

        # convert JSON to PhoneBill

        # update the list of phonebills/phone calls with the new phonebill

        # store the data file and return success or failure

    def remove_phonecall(self, phonecall_id):
        # TODO
        raise NotImplementedError( " Cannot register user!" )

    def register_user(self):
        # TODO
        raise NotImplementedError( " Cannot register user!" )

    def authenticate(self):
        # TODO
        raise NotImplementedError( " Cannot authenticate user!" )

    def search(self, callee, caller, start_date, end_date):
        # TODO
        raise NotImplementedError( " Cannot authenticate user!" )

    def start(self,debug=True):
        print( f"Flask server is running on port[{self.__port}] and uses data file[{self.__file}]" )
        self.secret_key= "V0JlXapkgs"
        self.run( host=self.__host, port=self.__port, debug=debug )
        print( f"Closing server --> port[{self.__port}]" )
