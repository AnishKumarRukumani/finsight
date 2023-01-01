import sys
from helper_files.Ac_processor import (AccountProcessor,DisplayAccounts)
from helper_files.helper import (GenerateStatmentFromCsv, GenerateCodeFromTemplateFile)



def main(statment_file_path, ac_code_file_path):

    statment = GenerateStatmentFromCsv(statment_file_path)
    ac_code = GenerateCodeFromTemplateFile(ac_code_file_path)
    AccountProcessor(statment, ac_code)
    accounts = DisplayAccounts(statment)
    accounts.display_statment()



if __name__ == "__main__":
    statment_file_path = sys.argv[1]
    ac_code_file_path = sys.argv[2]
    main(statment_file_path, ac_code_file_path)
