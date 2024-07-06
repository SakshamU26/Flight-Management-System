from operator import is_
import mysql.connector as c
try:
    con = c.connect(host = "localhost", user = "root", password = "", database = "dbms_project_flight_management")
    mycursor = con.cursor()
    # mycursor.execute(
    #     "create table airline(Airline_ID varchar(5) PRIMARY KEY, Airline_Name varchar(20))")
    # mycursor.execute(
    #     "create table airport(Airport_ID varchar(4) PRIMARY KEY, Name varchar(20))")
    # mycursor.execute(
    #     "create table plane(Plane_ID int(2) PRIMARY KEY, Model varchar(20), Total_seats int(3))")
    # mycursor.execute(
    #     "create table flight(Flight_ID int(2) PRIMARY KEY, Airline_ID int(1), Plane_ID int(2), Date_of_Flight date, Start_Airport varchar(4), FOREIGN KEY (Airline_ID) REFERENCES airline(Airline_ID), FOREIGN KEY (Plane_ID) REFERENCES plane(Plane_ID), FOREIGN KEY (Start_Airport) REFERENCES airport(Airport_Code))")
    # mycursor.execute(
    #     "create table area(Area_ID int(3) PRIMARY KEY, Flight_ID int(2), Arrival_Airport varchar(4), Arrival_Date date, FOREIGN KEY (Flight_ID) REFERENCES flight(Flight_ID), FOREIGN KEY (Arrival_Airport) REFERENCES airport(Airport_Code))")
    # mycursor.execute(
    #     "INSERT INTO airline VALUES(1,'IndiGo'),(2,'Air India'),(3,'SpiceJet'),(4,'Vistara'),(5,'Etihad'),(6,'Qatar'),(7,'Emirates')")
    # mycursor.execute(
    #     "INSERT INTO airport VALUES('DEL','Delhi'),('DXB','Dubai'),('ATL','Atlanta'),('LAX','Los Angeles'),('CDG','Paris'),('LHR','London'),('NRT','Tokyo'),('DOH','Doha'),('IST','Istanbul'),('LAS','Las Vegas')")
    # mycursor.execute(
    #     "INSERT INTO plane VALUES(21,'Boeing 707', 250),(22,'Airbus A310', 300),(23,'Boeing 747', 400),(24,'Convair 580', 175),(25,'Airbus A350', 275),(26,'Douglas DC-5', 325)")
    # mycursor.execute(
    #     "INSERT INTO flight VALUES(51, 3, 22, '2022-11-14', 'DXB'),(52, 5, 24, '2022-11-17', 'CDG'),(53, 2, 23, '2022-11-23', 'NRT'),(54, 1, 25, '2022-12-06', 'LAS'),(55, 6, 26, '2022-12-11', 'DEL'),(56, 1, 21, '2022-11-27', 'DOH'),(57, 2, 24, '2022-12-24', 'LHR'),(58, 4, 22, '2022-12-16', 'ATL')")
    # mycursor.execute(
    #     "INSERT INTO area VALUES(101, 54,'DEL','2022-12-08'),(102, 52,'DOH','2022-11-18'),(103, 56,'ATL','2022-11-29'),(104, 53,'LAS','2022-11-24'),(105, 57,'DXB','2022-12-25'),(106, 51,'LHR','2022-11-15'),(107, 55,'CDG','2022-12-12'),(108, 58,'NRT','2022-12-18')")

    print("Airplane Model with maximum number of seats:-")
    print("\n")
    mycursor.execute("SELECT max(Total_seats), Model FROM plane")
    myresult = mycursor.fetchall()
    for j in myresult:
        print(j)
    print("\n")

    print("Airplane Name and flight number with more than 300 seats:-")
    print("\n")
    mycursor.execute("SELECT Airline_Name, Flight_ID, Total_seats FROM plane NATURAL JOIN flight NATURAL JOIN airline where Total_seats>300")
    myresult = mycursor.fetchall()
    for j in myresult:
        print(j)
    print("\n")

    print("Name, Model and start airport of all airplanes in the month of December:-")
    print("\n")
    mycursor.execute("SELECT Airline_Name, Model, Start_Airport FROM airline NATURAL JOIN plane NATURAL JOIN flight where Date_of_Flight BETWEEN '2022-12-01' AND '2022-12-31'")
    myresult = mycursor.fetchall()
    for j in myresult:
        print(j)
    print("\n")

    print("Number of passengers landing in the United States in the month of November:-")
    print("\n")
    mycursor.execute("SELECT sum(Total_seats) AS Number_of_passengers FROM airline NATURAL JOIN plane NATURAL JOIN flight NATURAL JOIN area where Arrival_Airport IN ('LAS','ATL') AND Arrival_Date between '2022-11-01' AND '2022-11-30'")
    myresult = mycursor.fetchall()
    for j in myresult:
        print(j)
    print("\n")

    print("Total planes with Model Names starting with Airbus taking off from Dubai:-")
    print("\n")
    mycursor.execute("SELECT count(*) FROM airline NATURAL JOIN plane NATURAL JOIN flight NATURAL JOIN area where Model like 'Airbus%' AND Start_Airport = 'DXB'")
    myresult = mycursor.fetchall()
    for j in myresult:
        print(j)
    print("\n")




except c.error as e:
    print("Error reading data from MySQL table", e)