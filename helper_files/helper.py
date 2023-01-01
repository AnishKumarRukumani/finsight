import csv, yaml
from pathlib import Path
from data_store_files.data_store import (Statment, StatmentEntry, AC_Codes)

class GenerateCodeFromTemplateFile:

    def __new__(cls, file: Path) -> AC_Codes:
        cls.file = file
        return cls.generate_ac_code()

    @classmethod
    def generate_ac_code(cls) -> AC_Codes:
        with open(cls.file, 'r') as yamlfile:
            return AC_Codes(yaml.load(yamlfile))

class GenerateStatmentFromCsv:

    def __new__(cls, file: Path) -> Statment:
        cls.file = file
        return cls.generate_statment()

    @classmethod
    def generate_statment(cls) -> Statment:
        convert = lambda value: 0 if value == ' ' else float(value)
        with open(cls.file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            statment_instance=Statment(csvfile)
            for row in reader:
               statment_entry=StatmentEntry(row['PARTICULARS'],convert(row['DR']),convert(row['CR']))
               statment_instance.all_statment_entries.append(statment_entry)
        return statment_instance
            
