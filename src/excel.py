import pandas as pd
import openpyxl


def create_excel_file(file_name):
    data = {
        "Id":[1,2,3],
        "Name": ["Amit", "Boby", "Charan"],
        "Age": [25, 30, 20],
        "City_name": ["pune", "mumbai", "nagpur"]
    }

    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)
    

    print(f"Excel file {file_name} created successfully.")
    print("----------------------------------------------")
    print()


def read_excel_file(file_name):
    try:
        df=pd.read_excel(file_name)
    except Exception as e:
        print(e)
    else:
        print(f"printing the contents of {file_name}")
        print(df.to_string())
        print("----------------------------------------------")
        print()


def update_cell(file_name,row_no, col_no, value):
    try:
        df=pd.read_excel(file_name)
    except Exception as e:
        print(e)
    else:
        df.iloc[row_no-1, col_no-1] = value
        df.to_excel(file_name, index=False)
        print (f"updated the value of cell ({row_no},{col_no}) to {value} successfully")
        print("----------------------------------------------")
        print()

def update_col_name(file_name, old_col_name , new_col_name):
    try:
        df=pd.read_excel(file_name)
    except Exception as e:
        print(e)
    else:
        df.rename(columns={old_col_name: new_col_name}, inplace=True)   
        df.to_excel(file_name, index=False)
        print(f"updated column name from {old_col_name} to {new_col_name}")
        print("----------------------------------------------")
        print()

def append_row(file_name,Id,Name,Age,City):
    try:
        df=pd.read_excel(file_name)
    except Exception as e:
        print (e)
    else:
        new_data = {'Id':[Id], 'Name': [Name], 'Age': [Age], 'City_name':[City]} 
        new_df = pd.DataFrame(new_data)
        combined_df = pd.concat([df, new_df], ignore_index=True)
        combined_df.to_excel(file_name, index=False)
        print ("appended  a row")

        print("----------------------------------------------")
        print()




file='file.xlsx'

create_excel_file(file)
read_excel_file(file)
update_cell(file,1,3,20)
read_excel_file(file)
append_row(file,Name="alice", Id=6, Age=34, City="pune")
read_excel_file(file)
update_col_name(file,"City_name","City")
read_excel_file(file)


