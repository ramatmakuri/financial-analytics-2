# Financial Analytsics -  Loan Processing Application
---
This is a python application that allows users to identify potential lenders. The application takes inputs from users about their specific loan eligiiblity conditions, evaluates these inputs against loan criteria from various loan proviers, and returns a short-list of qualifying loans. The loan criteria for a hypothetical list of loan providers is provided in a csv file  titled `daily_rate_sheet'.

## Packages Used
This project leverages python 3.7 

## Installation Guide
The application requires the below programs to be installed 
```
*python
*fire
*questionary
*csv

```
## Project functionality:


1. Bank Data is loaded: For this purpose, user of the application has to provide the file path for processing.
2. Applicant information is gathered using a series of questions
3. The data received from the applicant is used to caluclate financial liquidty, and risk of default
4. The data received from the applicants and the ratios calculated therefrom are validated against the Bank information to filter banks that are willing to extend the loans to the applicant.
5. The list of qualifying loans are displayed to the applicant and the appliucant is provided an option to save the file for further use and processing.
6. If the applicant opts to save the file, a file path is obtained and stored at the path provided.

## Contributors
Brought to you by Ram Atmakuri (ram.atmakuri@outlook.com)

## License
[MIT] (https://choosealicense.com/licenses/mit/)
