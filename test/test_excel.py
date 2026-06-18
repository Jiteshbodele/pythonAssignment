from src.excel import create_excel_file, read_excel_file, update_cell, update_col_name, append_row
import pandas as pd
import pytest
def test_create_excel_file(tmp_path):
    
    file_path = tmp_path / "report.xlsx"

    create_excel_file(file_path)

    assert file_path.exists()
    assert file_path.stat().st_size > 0

    



def test_read_excel_file(capsys, tmp_path):
    file_path = tmp_path / "report.xlsx"

    create_excel_file(file_path)
    read_excel_file(file_path)
    capture = capsys.readouterr()

    assert "printing the contents of" in capture.out

    
    read_excel_file("non_existing.xlsx")
    capture=capsys.readouterr()
    assert "No such file" in capture.out



    
def test_update_cell(tmp_path):
    file_path = tmp_path / "report.xlsx"

    create_excel_file(file_path)

    update_cell(file_path,1,3,20) 

    df = pd.read_excel(file_path)

    assert df.iloc[0, 2] == 20  #[0,2]  because function also do iloc[1-1, 3-1]=20     # doesn't use 0 index for user convenieance



def test_update_col_name(tmp_path):
    file_path = tmp_path / "report.xlsx"

    create_excel_file(file_path)

    update_col_name(file_path,"City_name","City")

    df=pd.read_excel(file_path)
    
    assert "City" in df.columns
    assert "City_name" not in df.columns



def test_append_row(tmp_path):
    file_path = tmp_path / "report.xlsx"

    create_excel_file(file_path)
    old_df=pd.read_excel(file_path)

    append_row(file_path,Name="alice", Id=6, Age=34, City="pune")

    new_df=pd.read_excel(file_path)

    assert len(new_df)-1 == len(old_df)
