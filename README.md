# To run the scripts :
***
* make a virtual environment using following command :
python3 -m venv venv 

***
* activate virtual envronment using following command :
source venv/bin/activate 

***
* move to root directory of project and then run following command to get dependencies download :
    * to run scripts only
    pip install -e .

    * to test the scripts uisng pytest 
    pip install -e .[pytest]

***
* move to the src directory to run scripts. Run following command :
    * python excel.py
    * python postgres.py

***
* move to the test directory to test the test cases. Run following command :
    * pytest .



***
***
***


# What each function does :

* ## excel.py

    * ### create_excel_file()
    creates an excel file with the help of pandas (DataFrame) with 3 rows each having fields (Id, Name, Age, City_name)


    * ### read_excel_file()
    Reads existing excel file and prints its contents . If the file is not present it will print and exception 

    * ### update_cell()
    Updates the particular cell of the excel file . Note: takes row_no and column_no from but changes the cell present at [row_no-1, column_no-1 ]. 

    * ### update_col_name()
    updates the name of column in excel sheet

    * ### append_row()
    appends the row to the existing excel file 


* ## postgres.py

    * ### connect_db()
    connects to the postgres databases using psycopg2 . every method in this file calls it to connect to the database

    * ### create_db()
    connects to the database and checks if the given database(for creating it) is present or not . if it is not present, thne it will create it 

    * ### create_user_for_db()
    connects ot the database and checks if the given user is present or not . if it is not present , it will create the specified user and also make him owner of the given database and will give all the privileges to him on that database

    * ### excel_to_postgres() 
    connects to the database and checks if the info table is present or not . if it is present then it will be dropped .
    then it will dump all the data in the excel file to the table info by creating it and inserting all the rows in the excel one-by-one.
    Note : Assumption is that excel file already exists

    * ### postgres_to_excel()
    connects to the database and retrives the table info and then converts it in DataFrames using pandas and then it wites into an excel file
    Note: Assumption is that the table "info" exist in database 



# Test files in test directory:

both the files test_excel.py and test_postgres.py contains the tests for all the functions present in excel.py and postgres.py respectively