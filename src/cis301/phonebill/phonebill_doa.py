from abc import ABC, abstractmethod


class AbstractPhoneBill_DOA(ABC):
    '''This bstarct class defines functions for database manipulation '''

    @abstractmethod
    def insert_phonebill(self, phonebill) :
        pass

    @abstractmethod
    def update_phonebill(self, phonebill):
        pass

    @abstractmethod
    def delete_phonebill(self, phonebill):
        pass

    @abstractmethod
    def select_phonebill(self, phonebill_id):
        pass

    @abstractmethod
    def search_phonebills_bydate(self, startdate, enddate):
        pass


