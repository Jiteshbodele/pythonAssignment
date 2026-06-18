from src.postgres import connect_db, create_db, create_user_for_db, postgres_to_excel, excel_to_postgres



host="localhost"
port=5432
dbname="postgres"
user="postgres"
password="12345"

new_dbname="pythondb"
new_user="python"
new_password="12345"

excel_file_name="file.xlsx"
export_file_name="export.xlsx"



def test_connect_db():
    conn=connect_db(host=host,port=port,dbname=dbname,user=user,password=password)
    assert conn is not None

    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        result=cur.fetchone()
        assert list(result.values())[0] == 1
    conn.close()


def test_create_db(capsys):
    create_db(host=host, port=port,dbname=dbname,user=user,password=password,new_dbname=new_dbname)
    capture = capsys.readouterr()
    assert "Database created" in capture.out or "Database already exists" in capture.out
    

def test_create_user_for_db(capsys):
    create_user_for_db(host=host,port=port,dbname=dbname,user=user,password=password,new_dbname=new_dbname,new_user=new_user,new_password=new_password)
    capture = capsys.readouterr()
    assert "User created , made owner and granted  privilage " in capture.out or "User already exists" in capture.out


def test_postgres_to_excel(capsys, tmp_path):
    export_file_name = tmp_path / "report.xlsx"
    postgres_to_excel(host=host,port=port,dbname=new_dbname,user=new_user,password=new_password,export_file=export_file_name)
    capture = capsys.readouterr()
    assert f"exported the content of table 'info' to {export_file_name}" in capture.out


def test_excel_to_postgres(capsys,tmp_path):
    export_file_name = tmp_path / "report.xlsx"
    postgres_to_excel(host=host,port=port,dbname=new_dbname,user=new_user,password=new_password,export_file=export_file_name)

    excel_file_name=export_file_name


    excel_to_postgres(host=host,port=port,dbname=new_dbname,user=new_user,password=new_password,excel_file=excel_file_name)
    capture=capsys.readouterr()
    assert "Table created " in capture.out and  "inserted values in table" in capture.out
    