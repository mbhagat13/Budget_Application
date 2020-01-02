# Budget_Application
# Purpose #

The purpose of this application is to automatically group purchases into various categories and keep track of monthly credit card spending. The total amount spent for each category is outputted in the command line window along with a pie chart tracking how much money was spent on each category.

The various categories are the following:

* Transportation
* Food
* Clothes and Accessories
* Entertainment
* Other

These categories are preset in the code as the application is made for my own personal use.
# Sorting Algorithm #

To sort the items, additional text files are used to store keywords which describe the credit card description. There is a text file for descriptions of each category. Initially, these text files are blank. When the application is run, the program goes through each credit card description item and checks if any keyword in the description is stored in the text files.

If a match exists, then the program sorts the data accordingly. If no match exists, an unknown description is found and the user must enter the category and the keyword to be stored in the text file. Therefore, the item will be automatically sorted the next time it appears in the statement.

This method works for the type of purchases I make as 80% of my purchases every month are the same. This accuracy rate only increases as more data is provided for the program.

# Keywords #
The keyword that is selected must be unique to that type of purchase and also be contained in the credit card description. For example, if multiple purchases are made from the same store in various parts of the city, the keyword that is entered should only be the store name. 

Example 1: Identical Stores

Description 1: TACOBELL_NorthYork

Description 2: TACOBELL_MARKHAM

Keyword to be used = TACOBELL

Example 2: The keyword MUST be unique

Description 1: UberEats

Description 2: UberBV

The keyword Uber CANNOT be used as it is a conflicting entry. Two seperate keywords, UberEats and UberBV must be used. 
# Uses #

The application can be used with any TD Credit Card. 

To use:
1. Download statement from TD Easybank website and paste in directory of git repository.
2. Run application using python with following command:
  
  python Budget.py filename.csv Year Month
  
  year must be in yyyy format
  month must be in mm format
  
  A sample input file, accountactivity(1).csv, is provided in the git repository.
  A sample output of the pi chart output is available in the git repository (sample_pi.png).
