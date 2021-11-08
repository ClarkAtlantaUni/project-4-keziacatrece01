import datetime

from cis301.phonebill.abstract_phonecall import AbstractPhoneCall
from cis301.project4.util import Util


class PhoneCall(AbstractPhoneCall):
    def __init__(self, caller, callee, startdate, enddate):
        self.__caller = caller
        self.__callee = callee
        self.__startdate = startdate
        self.__enddate = enddate
        self.__uid = ""

    def set_uid(self,id):
        self.__uid = id

    def get_uid(self):
        return self.__uid

    def get_caller(self) -> str:
        return self.__caller

    def get_callee(self) -> str:
        return self.__callee

    def get_starttime(self) -> datetime:
        return Util.str_to_datetime(self.__startdate)

    def get_starttime_string(self) -> str:
        return self.__startdate

    def get_endtime(self) -> datetime:
        return Util.str_to_datetime(self.__enddate)

    def get_endtime_string(self) -> str:
        return self.__enddate