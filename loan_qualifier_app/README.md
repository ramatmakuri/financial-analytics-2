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
## Project functionality and Examples of Usage:

1. Bank Data is loaded: For this purpose, user of the application has to provide the file path for processing. Examnple of usage provided below:
<img width="567" alt="Screen Shot 2022-01-15 at 9 14 14 PM" src="https://user-images.githubusercontent.com/96159292/149648254-656105a7-e9f6-4316-a165-f4a774419ee8.png">
2. Applicant information is gathered using a series of questions. Examnple of usage provided below:
<img width="569" alt="Screen Shot 2022-01-15 at 9 17 27 PM" src="https://user-images.githubusercontent.com/96159292/149648327-e6188842-3427-4d6f-bd29-01d5d07abb45.png">
3. The data received from the applicant is used to caluclate financial liquidty, and risk of default. Examnple of usage provided below:
<img width="1358" alt="Screen Shot 2022-01-15 at 9 22 05 PM" src="https://user-images.githubusercontent.com/96159292/149648417-504b6b86-eaf6-40c4-a399-90cc75235205.png">
4. The data received from the applicants and the ratios calculated therefrom are validated against the Bank information to filter banks that are willing to extend the loans to the applicant.
5. The list of qualifying loans are displayed to the applicant and the appliucant is provided an option to save the file for further use and processing.Examnple of usage provided below:
<img width="1361" alt="Screen Shot 2022-01-15 at 9 22 22 PM" src="https://user-images.githubusercontent.com/96159292/149648433-47786717-3a27-46b3-8e46-2360a8caab58.png">

6. If the applicant opts to save the file, a file path is obtained and stored at the path provided. Else, the program exits. Examnple of usage provided below:
<img width="908" alt="Screen Shot 2022-01-15 at 9 28 54 PM" src="https://user-images.githubusercontent.com/96159292/149648527-d6e92a35-a149-49f5-ae84-726130570206.png">
<img width="510" alt="Screen Shot 2022-01-15 at 9 29 27 PM" src="https://user-images.githubusercontent.com/96159292/149648532-5f2f9c4e-ab3c-4a76-a605-610e003002bd.png">

## Contributors
Brought to you by Ram Atmakuri (ram.atmakuri@outlook.com)

## License
[MIT] (https://choosealicense.com/licenses/mit/)
