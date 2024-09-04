'''

==================================      SQLITE     ==============================================================

'''

'''

)1( כתוב ליד כל סעיף או פעולה( מה היא עושה:

1. Create/Drop table:
CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
INTEGER);
_____________________________________________________________________
Answer: Creates a table named shopping that has a primary key column named id of integer type,
and columns named name of the text type, and amount of the integer type.

DROP TABLE shopping
_____________________________________________________________________
Answer: Drops the table named shopping.

################################################################################################################
2. Rename table:
ALTER table shopping RENAME to shopp
______________________________________________________________________
Answer: Rename the table shopping, so it will be named shopp

ALTER table shopp RENAME to shopping
______________________________________________________________________
Answer: Renames the table back to shopping

###############################################################################################################
3. Insert rows into table:
INSERT INTO shopping VALUES (1, 'Avokado', 5);
_______________________________________________________________________
Answer: inserts the values (1, 'Avokado', 5) into the matching keys (id, name, amount) accordingly.

INSERT INTO shopping VALUES (2, 'Milk', 2);
_______________________________________________________________________
Answer: inserts the values (2, 'Milk', 2) into the matching keys (id, name, amount) accordingly.

INSERT INTO shopping VALUES (3, 'Bread', 3);
_______________________________________________________________________
Answer: inserts the values (3, 'Bread', 3) into the matching keys (id, name, amount) accordingly.

INSERT INTO shopping VALUES (4, 'Chocolate', 8);
_______________________________________________________________________
Answer: inserts the values (4, 'Chocolate', 8) into the matching keys (id, name, amount) accordingly.

INSERT INTO shopping VALUES (5, 'Bamba', 5);
_______________________________________________________________________
Answer: inserts the values (5, 'Bamba', 5) into the matching keys (id, name, amount) accordingly.

INSERT INTO shopping VALUES (6, 'Orange', 10);
_______________________________________________________________________
Answer: inserts the values (6, 'Orange', 10) into the matching keys (id, name, amount) accordingly.

##################################################################################################################
4. Display table:
select * from shopping
_______________________________________________________________________
Answer: displays all the shopping table contents.

##################################################################################################################
5. ?
SELECT id, name FROM shopping
_______________________________________________________________________
Answer: displays the id and name values for each row from the table named shopping.

##################################################################################################################
6. ?
SELECT * FROM shopping WHERE amount > 5
_______________________________________________________________________
Answer: displays all the shopping table row contents where the amount value is over 5.

SELECT * FROM shopping WHERE amount = 2
_______________________________________________________________________
Answer: displays all the shopping table row contents where the amount value is 2.

SELECT * FROM shopping WHERE name LIKE 'Bamba'
________________________________________________________________________
Answer: displays all the shopping table row contents where the name value is 'Bamba'.

###################################################################################################################
7. ?
DELETE from shopping WHERE name like 'Orange';
________________________________________________________________________
Answer: deletes all the rows of the shopping table, where the name value is 'Orange'.

###################################################################################################################
8. ?
UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
________________________________________________________________________
Answer: changes the name contents of the name value to 'Bisli' in the rows where the name value is 'Bamba'.

UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'
________________________________________________________________________
Answer: changes the amount contents of the amount value to 1 in the rows where the name value is 'Milk'.

##################################################################################################################
9. ?
ALTER TABLE shopping ADD COLUMN maavar
_________________________________________________________________________
Answer: adds the column maavar to the shopping table.

##################################################################################################################
10. ?
UPDATE shopping SET maavar=6 WHERE id=1;
_________________________________________________________________________
Answer: changes the maavar contents of the maavar value of the shopping table, to 6 in the rows where the id value is 1.

UPDATE shopping SET maavar=3 WHERE id=2;
_________________________________________________________________________
Answer: changes the maavar contents of the maavar value of the shopping table, to 3 in the rows where the id value is 2.

UPDATE shopping SET maavar=12 WHERE id=3;
_________________________________________________________________________
Answer: changes the maavar contents of the maavar value of the shopping table, to 12 in the rows where the id value is 3.

UPDATE shopping SET maavar=8 WHERE id=4;
_________________________________________________________________________
Answer: changes the maavar contents of the maavar value of the shopping table, to 8 in the rows where the id value is 4.

UPDATE shopping SET maavar=5 WHERE id=5;
_________________________________________________________________________
Answer: changes the maavar contents of the maavar value of the shopping table, to 5 in the rows where the id value is 5.

##################################################################################################################
11. ?
SELECT * FROM shopping WHERE amount > 1 AND maavar > 5
_________________________________________________________________________
Answer: display all row values of the shopping table, where the amount value is over 1 and the maavar value is over 5.

SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5
_________________________________________________________________________
Answer: display all row values of the shopping table, where the maavar value is between 3 and 5 (3, 4, 5).

#################################################################################################################
12. ?
SELECT * FROM shopping ORDER BY maavar
_________________________________________________________________________
Answer: display all row values of the shopping table, ordered by maavar values in ascending (default) order.

SELECT * FROM shopping ORDER BY maavar DESC
_________________________________________________________________________
Answer: display all row values of the shopping table, ordered by maavar values in descending order.

################################################################################################################
13. ?
CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
_________________________________________________________________________
Answer: creates a table named books that has a primary key column named id of integer type,
and a column named name of the text type.

INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
_________________________________________________________________________
Answer: inserts the values (1, 'SQL PROGRAMMING') into the matching keys (id, name) of the books table accordingly.

INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
_________________________________________________________________________
Answer: inserts the values (2, 'CSHARP PROGRAMMING') into the matching keys (id, name) of the books table accordingly.

DELETE FROM books;
_________________________________________________________________________
Answer: deletes all the values of the table books.

###############################################################################################################
14. ?
SELECT COUNT(*)from shopping
_________________________________________________________________________
Answer: display the number of rows in the shopping table. 

SELECT MAX(amount) from shopping
_________________________________________________________________________
Answer: display the maximal value of the amount key in the shopping table. 

SELECT AVG(amount) from shopping
_________________________________________________________________________
Answer: display the average value of the amount key in the shopping table.

SELECT MIN(amount) from shopping
_________________________________________________________________________
Answer: display the minimal value of the amount key in the shopping table.

###############################################################################################################
15. ?
INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
_________________________________________________________________________
Answer: inserts the values (6, 'Onions', 3, 6) into the matching keys (id, name, amount, maavar) of the shopping accordingly.

INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
_________________________________________________________________________
Answer: inserts the values (7, 'Orio', 1, 8) into the matching keys (id, name, amount, maavar) of the shopping accordingly.

Select maavar, COUNT(*)FROM shopping GROUP BY maavar
_________________________________________________________________________
Answer: display the number of values corresponding to each distinct value of the maavar key.

###############################################################################################################
16. ?
SELECT id AS "SECRET", name, amount, maavar FROM shopping
_________________________________________________________________________
Answer: displays the values of the shopping table, in the columns id("SECRET"), name, amount, maavar . 
The name of the key id is displayed as SECRET.

###############################################################################################################
17. ?
Select maavar, COUNT(*)FROM shopping GROUP BY maavar HAVING COUNT(*)>1
_________________________________________________________________________
Answer: display the number of values corresponding to each distinct value of the maavar key, for the rows where 
their number is larger then 1 (there are more then 1 item corresponding to that value of maavar).  

##############################################################################################################
18. ?
CREATE TABLE prices (id INTEGER PRIMARY KEY, price INTEGER);
_________________________________________________________________________
Answer: creates a table named prices that has a primary key column named id of integer type,
and another column named price of the integer type.

INSERT INTO prices VALUES (1, 3);
_________________________________________________________________________
Answer: inserts the values (1, 3) into the matching keys (id, price) of the prices table accordingly.

INSERT INTO prices VALUES (2, 7);
_________________________________________________________________________
Answer: inserts the values (2, 7) into the matching keys (id, price) of the prices table accordingly.

INSERT INTO prices VALUES (3, 12);
_________________________________________________________________________
Answer: inserts the values (3, 12) into the matching keys (id, price) of the prices table accordingly.

INSERT INTO prices VALUES (4, 5);
_________________________________________________________________________
Answer: inserts the values (4, 5) into the matching keys (id, price) of the prices table accordingly.

INSERT INTO prices VALUES (5, 3);
_________________________________________________________________________
Answer: inserts the values (5, 3) into the matching keys (id, price) of the prices table accordingly.

INSERT INTO prices VALUES (6, 2);
_________________________________________________________________________
Answer: inserts the values (6, 2) into the matching keys (id, price) of the prices table accordingly.

INSERT INTO prices VALUES (7, 10);
_________________________________________________________________________
Answer: inserts the values (7, 10) into the matching keys (id, price) of the prices table accordingly.

SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN prices p ON s.id=p.id
_________________________________________________________________________
Answer: displays the joint values of the shopping table and prices table (joined on the primery key id), 
in the columns id, name, amount, maavar, price . 

##############################################################################################################
מה מחושב בתוך SECRET ? 19.
SELECT s.id, s.name, s.amount, s.maavar, p.price, s.amount * p.price AS
"SECRET" FROM shopping s JOIN prices p ON s.id=p.id
_________________________________________________________________________
Answer: "SECRET" is the amount of the goods (taken from the shopping table) multiplied by the price of the goods
(Example:  amount there are 5 Avocados, price is 3 per Avocado, to buy all 5 you need 15 (which is the "SECRET")). 

##############################################################################################################
20. ?
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN prices p ON s.id=p.id 
WHERE p.price = (SELECT MAX(price) FROM prices)
_________________________________________________________________________
Answer: display the id, name, maavar, and price values for the good (or goods) 
the price of which is the maximal in the prices table (in this case Bread).

'''
'''

)2( פתור:

Students
ID (INTEGER)PRIMARY KEY NAME (TEXT) CITY (TEXT) BIRTH (INTEGER)
1 SHALOM TEL AVIV 1974
2 YURI RAANANA 1980
3 ANAT RISHON 1994
4 DANA REHOVOT 1990
5 OMER JERUSALEM 1987

GRADE
ID (INTEGER)PRIMARY KEY GRADE (INTEGER)
1 95
2 70
3 85
4 99
5 91


- כתוב את השאילתות ליצירת הטבלאות )ללא האיכלוס(
___________________________________________________________________
Answer: 
CREATE TABLE Students(id INTEGER PRIMARY KEY, name TEXT, city TEXT, birth INTEGER);
CREATE TABLE GRADE (id INTEGER PRIMARY KEY, grade INTEGER);


- כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל
___________________________________________________________________
Answer: 
SELECT * FROM Students stu JOIN GRADE gr ON stu.id = gr.id;


- כתוב שאילתא אשר מחשבת את הממוצע הכיתתי
___________________________________________________________________
Answer: 
SELECT AVG(grade) from grade


- כתוב שאילתא להוספת עמודה EXCELLENT. כעת שים YES כאשר הציון גבוה מ90- אחרת שים NO
___________________________________________________________________
Answer: 
ALTER TABLE grade ADD COLUMN EXCELLENT;
UPDATE grade SET excellent = "NO"
UPDATE grade SET excellent = "YES" WHERE grade > 90;


- *כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל רק עבור
התלמידים אשר קיבלו מעל הממוצע
___________________________________________________________________
Answer: 
select stu.name, gr.grade FROM Students stu JOIN GRADE gr ON stu.id = gr.id 
where gr.grade > (select avg(grade) from grade);


- * כתוב שאילתא אשר מדפיסה את התלמיד ואת ציונו עבור התלמיד אשר קיבל את הציון הגבוה
ביותר_______________________________________________________________
Answer: 
select stu.name, gr.grade FROM Students stu JOIN GRADE gr ON stu.id = gr.id 
where gr.grade = (select max(grade) from grade);


'''