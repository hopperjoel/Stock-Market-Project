import mysql.connector
import pandas as pd

mytestdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Elmakano132!",
    database="investing"
)

mycursor = mytestdb.cursor()

mycursor.execute("""CREATE TABLE exchange_market (
company_name VARCHAR(40),
ticker VARCHAR(40),
market VARCHAR(40),
currency_adjustment INT,
PRIMARY KEY(company_name)
);""")
