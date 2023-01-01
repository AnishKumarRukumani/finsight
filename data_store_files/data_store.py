from dataclasses import dataclass, field
from typing import Dict, List

#User defined data types to store the statment data and Accodes in a strcutured format for processing.

@dataclass
class StatmentEntry:
   '''Dataclass representing a StatmentEntry'''
   entry_name: str
   debit: float = 0 
   credit: float = 0 
   net: float = 0

   def calculate_net(self):
      self.net = self.credit - self.debit

@dataclass
class Statment:
    '''Dataclass representing a statment'''
    statment_name: str
    uniq_statment_entries: Dict[str, StatmentEntry] = field(default_factory=lambda:{})
    all_statment_entries: List[StatmentEntry] = field(default_factory=lambda:[])


@dataclass
class AC_Codes:
    '''Dataclass  representing AC codes'''
    ac_codes: Dict[str,str]
    
