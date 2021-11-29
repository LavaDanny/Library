import pandas as pd
import mysql.connector
import aws_config
import csv

# import book info from good reads csv
data = pd.read_csv(r'C:\Users\LavaDanny\Desktop\Coding\Library\books2.csv')
df = pd.DataFrame(data)

# print(df)
# for x in df.columns:
#     print(x)


# connect to aws rds
con = mysql.connector.connect(
        host = aws_config.host,
        user = aws_config.user,
        password = aws_config.pw)

c = con.cursor()
c.execute("USE db1")

# create book table if non existent
query1 = """CREATE TABLE IF NOT EXISTS books (
bookID MEDIUMINT,
title VARCHAR(100),
authors VARCHAR(50),
average_rating DECIMAL(3,2),
isbn VARCHAR(15),
isbn13 INT,
language_code VARCHAR(5),
num_pages SMALLINT,
ratings_count MEDIUMINT,
text_reviews_count MEDIUMINT,
publication_date DATE,
publisher VARCHAR(100),
PRIMARY KEY(bookID)
)"""
c.execute(query1.replace('\n',' '))


csv_data = csv.reader(open(r'C:\Users\LavaDanny\Desktop\Coding\Library\books2.csv', encoding="utf8"))
for row in csv_data:
    c.execute('INSERT INTO books(bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher)' \
          'VALUES("%d", "%s", "%s", "%f", "%s", "%d", "%s", "%d", "%d", "%d", "%s", "%s")', 
          row)
        
#close the connection to the database.
con.commit()
c.close()
print("Done")