from abc import ABC, abstractmethod


class AbstractPhoneCall_DOA( ABC ):
    '''This bstarct class defines functions for database manipulation '''

    @abstractmethod
    def insert_phonecall(self, phonecall):
        pass

    @abstractmethod
    def update_phonecall(self, phonecall):
        pass

    @abstractmethod
    def delete_phonecall(self, phonecall):
        pass

    @abstractmethod
    def select_phonecall(self, phonecall_id):
        pass

    @abstractmethod
    def search_phonecalls_bydate(self, startdate, enddate):
        pass

    @abstractmethod
    def search_phonecalls_bycustomername(self, customer_id):
        pass

