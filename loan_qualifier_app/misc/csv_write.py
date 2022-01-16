import sys
import questionary
import csv
from pathlib import Path

"""Saves the qualifying loans to a CSV file.
    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # The CLI tool should prompt the user to save the results as a CSV file, if there are qualifying loans. Also, the user should have an option to exit without saving.
    # If the user opts to save the list of qualifyoing loans, the CLI tool should prompt for a filew path where the file should be saved.
    # If there are no qualifying loans, the application should notify the user and exit
    # YOUR CODE HERE!

def save_qualifying_banks(bank_data_filtered):
    if len(bank_data_filtered) >0:
        print (f"You have {len(bank_data_filtered)} loans.") 
        save_file = questionary.checkbox ("Do you want to save the list of qualifying loans?", choices=["Yes", "No"]).ask()
        print(save_file)
        if save_file[0]== "Yes":
            file_path1 = questionary.text("Enter a file path to store the file (.csv):").ask()
            file_path1 = Path(file_path1)
            field_names = ("Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate")
            with open (file_path1, 'w', newline = "") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter = ',')
                csv_writer.writerow(field_names)
                csv_writer.writerows(bank_data_filtered)
            if not file_path1.exists():
                sys.exit(f"Oops! Can't find this path: {file_path1}")
            return file_path1
        else: 
            print ("Ok! Exiting without saving the file") 
            return
    else: 
        print ("There are no qualifying loans") 
        return
