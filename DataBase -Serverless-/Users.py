import sqlite3

target_name = "Fin"

conn = sqlite3.connect("users.db") #Connecting to db (Database)
cursor = conn.cursor() #Connect the cursor instance to use methods from sqlite such as fetching data from the result sets of queries.

def search_data(id, name, city, age):
    cursor.execute('CREATE TABLE user(user_id n(5), name char (30), city char (35), age decimal(7,2));') #Creates table along with columns.
    cursor.execute("INSERT INTO user VALUES (4, 'Findlay', 'Billingham', 1)")
    cursor.execute("""
                   INSERT INTO user(user_id, name, city, age)
                   VALUES (?,?,?,?)
                   """, (id, name, city, age)) #Inserts new data (the parameters) into the table.
    rows = cursor.execute("SELECT user_id, name, city, age FROM user").fetchall()
    search = cursor.execute(
        'SELECT user_id, name, city, age FROM user WHERE name =?',(target_name,), #Selects specific name stored.
        ).fetchall() #Selects the columns from the users table and fetches them all.
    conn.commit() #Commits to changes.
    print('Data entered...')
    conn.close() #Closes connection to DB.
    print(rows)
    print(search)
    if (conn):
        conn.close()
        print('\nDatabase closed...') #If the connection is closed it will print this message.
search_data(4, 'Fin', 'Billingham', 1) #Inputs data through parameters to table.