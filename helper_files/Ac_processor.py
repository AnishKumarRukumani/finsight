import re
from data_store_files.data_store import (Statment, StatmentEntry, AC_Codes)

class AccountProcessor:
    '''Class to Process account statment using the account codes and compute the transaction for a particular entity'''

    def __init__(self, statment: Statment, ac_code: AC_Codes):
        self.statment = statment
        self.ac_code = ac_code
        self.process_statment()

    def __merge_entry(self, actual_entry: StatmentEntry, merge_entry: StatmentEntry) -> None:
        actual_entry.debit +=  merge_entry.debit
        actual_entry.credit += merge_entry.credit

    def process_statment(self) -> Statment:
        for entry in self.statment.all_statment_entries:
           for code,code_format in self.ac_code.ac_codes.items():
               if re.match(code_format, entry.entry_name):
                   name = re.match(code_format, entry.entry_name).group("entry_name")
                   if name in self.statment.uniq_statment_entries.keys():
                       self.__merge_entry(self.statment.uniq_statment_entries[name], entry)
                   else:
                       self.statment.uniq_statment_entries.update({name:entry})
                   self.statment.uniq_statment_entries[name].calculate_net() 
                   
class DisplayAccounts:
    '''class to Display accounting transaction for entities involved'''

    def __init__(self, statment: Statment) -> None:
        self.statment = statment

    def display_statment(self):
        print("{:<60}\t{:<20}\t{:<20}\t{:<20}\n".format("Name|","Debit|","Credit|","Net|"))
        for name, entry in self.statment.uniq_statment_entries.items():
            print("{:<60}\t{:<20}\t{:<20}\t{:<20}\n".format(name,entry.debit,entry.credit,entry.net))

    



