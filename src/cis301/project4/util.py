from datetime import datetime
import json
import pickle
import re

class Util:

    regx_ip = r'^(25[0-5]|2[0-4]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]|[01]?[0-9][0-9]?)$'
    regex_phone = r'^[1-9]\d{2}-\d{3}-\d{4}$'

    datetime_format = "%m/%d/%Y %H:%M"


    @staticmethod
    def validate_email(email)->bool:
        """
         This function validates email string format. (abc@doamin.com)
         Also it checks if the domain is valid

        :param email: the email address to be validated
        :return: True if passes format and domain check, otherwise, False
        """
        pass

    @staticmethod
    def toPickle( obj, filename):
        with open(filename, "wb") as pickledFile:
            pickle.dump(obj, pickledFile)

    @staticmethod
    def fromPickled(filename)->object:
        with open(filename, "rb") as pickledFile:
            return pickle.load(pickledFile)


    @staticmethod
    def toJSONFile1(jsonStr, filename):
        with open(filename, "w") as jsonfile:
            jsonfile.write(jsonStr);
            jsonfile.flush();

    @staticmethod
    def toJSONFile2(obj, filename):
        with open(filename, "w") as jsonfile:
            json.dump(obj, jsonfile)

    @staticmethod
    def fromJSONFile2(filename)->object:
        with open(filename, "r") as jsonfile:
            return json.load(jsonfile)


    @staticmethod
    def phonecallToJSONString(phonecall, client=False) -> str:
        '''
            caller = caller
            callee = callee
            startdate = startdate
            enddate = enddate
        :param phonecall:
        :return: JSON representation of the passed phoncall
        '''
        jsonStr = "{"
        jsonStr += '"caller":"' + phonecall.get_caller() + '",'
        jsonStr += '"callee":"' + phonecall.get_callee() + '",'
        jsonStr += '"startdate":' + phonecall.get_starttime_string()+ ','
        jsonStr += '"enddate":"' + phonecall.get_endtime_string() + '"'
        if client:
            jsonStr += ',"client":"True"'
        jsonStr += "}"
        return jsonStr

    @staticmethod
    def phonecallToJSON(phonecall, client=False) -> str:
        '''
            caller = caller
            callee = callee
            startdate = startdate
            enddate = enddate
        :param phonecall:
        :return: JSON representation of the passed phoncall
        '''
        json ={"caller":f"{phonecall.get_caller()}",
               "callee": f"{phonecall.get_callee()}",\
               "startdate":f"{phonecall.get_starttime_string()}",\
               "enddate": f"{phonecall.get_endtime_string()}"}
        if client:
            json['client'] = True
        return json

    @staticmethod
    def isValidIPAddress(ip)-> bool:
        if re.search(Util.regx_ip, ip):
            return True
        else:
            return False

    @staticmethod
    def isValidDate(date) -> bool:
        dt = None
        try:
            dt = datetime.strptime(date, Util.datetime_format)
            return True
        except:
            return False

    @staticmethod
    def str_to_datetime(datestr) -> datetime:
        dt = None
        try:
            dt = datetime.strptime(datestr, Util.datetime_format)
            return dt
        except:
            return dt


    @staticmethod
    def isValidPhoneNumber(number) -> bool:
        if re.search(Util.regex_phone, number):
            return True
        else:
            return False
