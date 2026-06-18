import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd


def connect_db(host,port,dbname,user,password):
    conn=psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password,
    cursor_factory=RealDictCursor  # Ensures column names are kept
    )
    return conn

def create_db(host,port,dbname,user,password,new_dbname):
    try:
        conn=connect_db(host=host,port=port,dbname=dbname,user=user,password=password)
    except Exception as e:
        print (e)

    else:
        conn.autocommit=True
        cur=conn.cursor()

        #for db creation

        check_if_db_exists_query=f"select 1 from  pg_database where datname = '{new_dbname}'"
        cur.execute(check_if_db_exists_query)
        exists = cur.fetchone()

        if not exists:
            create_db_query=f"create database {new_dbname};"
            cur.execute(create_db_query)
            print("Database created")
        else:
            print("Database already exists")
        
        cur.close()
        conn.close()
        print("----------------------------------------------")
        print()


def create_user_for_db(host,port,dbname,user,password,new_dbname,new_user,new_password):
    try:
        conn=connect_db(host=host,port=port,dbname=dbname,user=user,password=password)
    except Exception as e:
        print (e)

    else:
        # conn.autocommit=True
        cur=conn.cursor()

        check_if_user_exists_query=f"select 1 from pg_roles where rolname = '{new_user}'"
        cur.execute(check_if_user_exists_query)
        exists=cur.fetchone()

        if not exists:
            
            #for user creaton and granting him permission on db
            create_user_query=f"create user {new_user} with password '{new_password}'"
            make_owner_query=f"alter database {new_dbname} owner to {new_user}"
            grant_privilege_query=f"grant all privileges on database {new_dbname} to {new_user}"

            cur.execute(create_user_query)
            cur.execute(make_owner_query)
            cur.execute(grant_privilege_query)
            print("User created , made owner and granted  privilage ")

        else:
            print("User already exists")
        
        conn.commit()

        cur.close()
        conn.close()
        print("----------------------------------------------")
        print()


def excel_to_postgres(host,port,dbname,user,password,excel_file):
    try:
        conn=connect_db(host=host,port=port,dbname=dbname,user=user,password=password)
    except Exception as e:
        print (e)

    else:
        cur=conn.cursor()
        check_if_table_exist_query="select 1 from information_schema.tables where table_schema = 'public' and  table_name = 'info'"
        cur.execute(check_if_table_exist_query)
        exists=cur.fetchone()

        if exists:
            delete_table_query="drop table info"
            cur.execute(delete_table_query)
            print("Table Dropped")
        
        #create table
        create_table_query="create table info(Id integer primary key, Name text, Age integer, City text)"
        cur.execute(create_table_query)
        print("Table created ")


        #inserting excel data into postgres table

        df=pd.read_excel(excel_file)

        data_tuples=list(df.itertuples(index=False, name=None))


        insert_query="insert into info(Id,Name,Age,City) values(%s, %s, %s, %s)"

        cur.executemany(insert_query,data_tuples)

        print("inserted values in table")

        conn.commit()

        cur.close()
        conn.close()
        print("----------------------------------------------")
        print()


def postgres_to_excel(host,port, dbname,user,password, export_file):
    try:
        conn=connect_db(host=host,port=port,dbname=dbname,user=user,password=password)
    except Exception as e:
        print (e)

    else:
        cur=conn.cursor()

        get_data_query="select * from info "

        cur.execute(get_data_query)

        data=cur.fetchall()


        df=pd.DataFrame(data)


        df.to_excel(export_file, index=False)

        print(f"exported the content of table 'info' to {export_file}")

        conn.commit()

        cur.close()
        conn.close()
        print("----------------------------------------------")
        print()



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

if __name__=="__main__":

    create_db(host=host, port=port,dbname=dbname,user=user,password=password,new_dbname=new_dbname)

    create_user_for_db(host=host,port=port,dbname=dbname,user=user,password=password,new_dbname=new_dbname,new_user=new_user,new_password=new_password)

    excel_to_postgres(host=host,port=port,dbname=new_dbname,user=new_user,password=new_password,excel_file=excel_file_name)

    postgres_to_excel(host=host,port=port,dbname=new_dbname,user=new_user,password=new_password,export_file=export_file_name)













