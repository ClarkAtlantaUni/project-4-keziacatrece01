from typing import List

from cis301.phonebill.abstract_phonebill import AbstractPhoneBill


class PhoneBill(AbstractPhoneBill):

    def __init__(self, customername, uid ):
        self.__custromername = customername
        self.__id = uid
        self.__phonecalls = list()

    def get_customer(self) -> str:
        return self.__custromername

    def add_phonecall(self, phonecall):
       self.__phonecalls.append(phonecall)

    def get_phonecalls(self) -> List[AbstractPhoneBill]:
        return self.__phonecalls