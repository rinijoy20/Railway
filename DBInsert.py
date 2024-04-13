

while True:
    a1=int(input("Enter the Admin Password Of Railway Reservation.: "))
    if a1==123:
        print("Logging in...")
        try:
            import mysql.connector as msc
            import datetime
            import random as rd
            import pandas as pd
            import sys
            import matplotlib.pyplot as plt


            mydb=msc.connect(host="localhost",
                                    user="root",
                                    password="mysql"
                                    )
            crs=mydb.cursor()
            qry01="CREATE DATABASE IF NOT EXISTS railway"
            crs.execute(qry01)
            qry02="USE railway"
            crs.execute(qry02)
                

            qry03="CREATE TABLE IF NOT EXISTS Passenger_Details (Pnr_Number int(10) primary key,Psn_Name varchar(25),Psn_Ph_no VARCHAR(10),Psn_age int(10),Psn_gender char(1),Train_from varchar(20),Train_to varchar(20),Scheduled_Date DATE,Email_ID varchar(30),Fare int(12))"
            crs.execute(qry03)


            qry21="INSERT INTO Passenger_Details   VALUES   (1021959091,'MOHAN','9658256315',25,'M','AJMER','DELHI','2021-03-09','Mohan@gmail.com',720) ON DUPLICATE KEY UPDATE Pnr_Number=1021959091"
            qry22="INSERT INTO Passenger_Details   VALUES   (1021959311,'ROHIT',9652256315,21,'M','AJMER','AJMER','2021-03-29','Rohit@gmail.com',452) ON DUPLICATE KEY UPDATE Pnr_Number=1021959311"
            qry23="INSERT INTO Passenger_Details   VALUES   (1021959332,'CARL',6235256363,20,'F','AGRA','MATHURA','2021-05-19','Carl@gmail.com', 1123) ON DUPLICATE KEY UPDATE Pnr_Number=1021959332"
            qry24="INSERT INTO Passenger_Details   VALUES   (1021959301,'MARK',6582563151,26,'M','SHIMLA','BANGLORE','2021-05-05','Mark11@gmail.com',558) ON DUPLICATE KEY UPDATE Pnr_Number=1021959301"
            qry25="INSERT INTO Passenger_Details   VALUES   (1021951231,'VON',7584635269,24,'M','CHENNAI','KANYKUMARI','2021-03-25','Von@gmail.com',320) ON DUPLICATE KEY UPDATE Pnr_Number=1021951231"
            qry26="INSERT INTO Passenger_Details   VALUES   (1021959441,'RONIT',8529639636,21,'M','HALDIA','DELHI','2021-05-09','Ronit45@gmail.com',750) ON DUPLICATE KEY UPDATE Pnr_Number=1021959441"
            qry27="INSERT INTO Passenger_Details   VALUES   (1021952331,'SUNIT',6589262529,22,'M','LUCKNOW','VARANASI','2021-06-23','Sunit11@gmail.com',950) ON DUPLICATE KEY UPDATE Pnr_Number=1021952331"
            crs.execute(qry21)
            crs.execute(qry22)
            crs.execute(qry23)
            crs.execute(qry24)
            crs.execute(qry25)
            crs.execute(qry26)
            crs.execute(qry27)
            
            qry04="USE railway"
            crs.execute(qry04) 
            qry02="CREATE TABLE IF NOT EXISTS avail_Train(Srno int(10),Train_No int(15) primary key,Train_Name varchar(250),Train_from varchar(200),Train_to varchar(300))"
            crs.execute(qry02)

            qry1="INSERT INTO avail_Train VALUES  (1001,12847,'Howrah - Digha SUPER AC Express','Howrah','Digha') ON DUPLICATE KEY UPDATE Train_No =12847"
            qry2="INSERT INTO avail_Train  VALUES  (1002,12009,'Mumbai Central - Ahmedabad Shatabdi Express','Mumbai','Ahmedabad') ON DUPLICATE KEY UPDATE Train_No =12009"
            qry3="INSERT INTO avail_Train  VALUES  (1003,120010,'New Delhi - Lucknow Jn Swarn Shatabdi Express','New Delhi'  ,'Lucknow ') ON DUPLICATE KEY UPDATE Train_No=120010"
            qry4="INSERT INTO avail_Train  VALUES  (1004,1280050,'New Delhi - Amritsar Shatabdi Express','New Delhi','Amritsa') ON DUPLICATE KEY UPDATE Train_No=1280050"
            qry5="INSERT INTO avail_Train  VALUES  (1005,1282371,'New Delhi - Daurai (Ajmer) Shatabdi Express','New Delhi','Ajmer') ON DUPLICATE KEY UPDATE Train_No=1282371"
            qry6="INSERT INTO avail_Train  VALUES  (1006,1204745,'Howrah - Ranchi Shatabdi Express','Digha','Ranchi') ON DUPLICATE KEY UPDATE Train_No=1204745"
            qry7="INSERT INTO avail_Train VALUES  (1007,1284769,'KSR Bengaluru - MGR Chennai Central Shatabdi Expres','Bengaluru','Chennai') ON DUPLICATE KEY UPDATE Train_No=1284769"
            qry8="INSERT INTO avail_Train VALUES (1008,1201789,'New Delhi - Kanpur Central Shatabdi Express','New Delhi','Kanpur') ON DUPLICATE KEY UPDATE Train_No=1201789"
            qry9="INSERT INTO avail_Train  VALUES  (1009,100052,'MGR Chennai Central - Coimbatore Shatabdi Express','Chennai','Coimbatore') ON DUPLICATE KEY UPDATE Train_No=100052"
            qry10="INSERT INTO avail_Train  VALUES  (1010,1286565,'New Delhi - Chandigarh Shatabdi Express','New Delhi','Chandigarh') ON DUPLICATE KEY UPDATE Train_No=1286565"
            qry11="INSERT INTO avail_Train VALUES   (1011,101285,'Pune - Secunderabad Shatabdi Express','Pune ','Secunderabad') ON DUPLICATE KEY UPDATE Train_No=101285"
            qry12="INSERT INTO avail_Train  VALUES (1012,100212,'New Delhi - Firozpur Cantt Shatabdi Express','New Delhi','Firozpur')  ON DUPLICATE KEY UPDATE Train_No=100212"
            qry13="INSERT INTO avail_Train  VALUES (1013,130201,'New Delhi - Jammu Tawi Rajdhani Express','New Delhi','Jammu ')  ON DUPLICATE KEY UPDATE Train_No=130201"
            qry14="INSERT INTO avail_Train  VALUES  (1014,111000,'KSR Bengaluru - Hazrat Nizamuddin Rajdhani Express','Bengaluru','Hazrat Nizamuddin') ON DUPLICATE KEY UPDATE Train_No=111000"
            qry15="INSERT INTO avail_Train  VALUES  (1015,100005,'M.G.R Chennai Central - Hazrat Nizamuddin Rajdhani E','Chennai','Hazrat Nizamuddin')  ON DUPLICATE KEY UPDATE Train_No=100005"
            qry16="INSERT INTO avail_Train  VALUES (1016,104040,'New Delhi - Ranchi Rajdhani Express','New Delhi','Ranchi')  ON DUPLICATE KEY UPDATE Train_No=104040"
            qry17="INSERT INTO avail_Train  VALUES (1017,121546,'MGR Chennai Central - Thiruvananthapuram Central','Chennai','Thiruvananthapuram')  ON DUPLICATE KEY UPDATE Train_No=121546"
            qry18="INSERT INTO avail_Train   VALUES( 1018,141524,'Mumbai LTT - Haridwar AC Express (PT)','Mumbai','Haridwar')  ON DUPLICATE KEY UPDATE Train_No=141524"
            qry19="INSERT INTO avail_Train  VALUES (1019,152634,'Bhuj - Mumbai Bandra (T.) AC SuperFast Express','Bhuj ','Mumbai') ON DUPLICATE KEY UPDATE Train_No=152634"
            qry20="INSERT INTO avail_Train  VALUES (1020,136524,'Lucknow - New Delhi AC Superfast Express','Lucknow','New Delhi') ON DUPLICATE KEY UPDATE Train_No=136524"
            qry31="INSERT INTO avail_Train VALUES (1021,1201546,'Nagpur - Amritsar AC SF Express','Nagpur','Amritsar') ON DUPLICATE KEY UPDATE Train_No=1201546"
            qry32="INSERT INTO avail_Train  VALUES (1022,126352,'Arunachal AC SF Express','New Delhi','Itanagar')  ON DUPLICATE KEY UPDATE Train_No=126352"
            qry33="INSERT INTO avail_Train  VALUES (1023,104152,'Darshan Express','Howrah','Digha')  ON DUPLICATE KEY UPDATE Train_No=104152"
            qry34="INSERT INTO avail_Train  VALUES (1024,100525,'Visakhapatnam - Secunderabad AC SF Express','Visakhapatnam','Secunderabad')  ON DUPLICATE KEY UPDATE Train_No=100525"
            qry35="INSERT INTO avail_Train  VALUES (1025,100121,'Patna - Ranchi AC Express','Patna','Ranchi')  ON DUPLICATE KEY UPDATE Train_No=100121"
            qry36="INSERT INTO avail_Train  VALUES (1026,114754,'Barmer - Yesvantpur AC Express','Barmer','Yesvantpur')  ON DUPLICATE KEY UPDATE Train_No=114754"
            qry37="INSERT INTO avail_Train  VALUES  (1027,128474,'Jammu Tawi - Ahmedabad Express','Jammu Tawi','Ahmedabad')  ON DUPLICATE KEY UPDATE Train_No=128474"
            qry38="INSERT INTO avail_Train  VALUES (1028,128654,'Jammu Tawi - Guwahati Amarnath Express (PT)','Jammu Tawi','Guwahati')  ON DUPLICATE KEY UPDATE Train_No=128654"
            qry39="INSERT INTO avail_Train  VALUES (1029,1280417,'Bandra Terminus - Gorakhpur Avadh Express (PT)','Mumbai','Gorakhpur')  ON DUPLICATE KEY UPDATE Train_No=1280417"
            qry40="INSERT INTO avail_Train  VALUES (1030,124557,'Dibrugarh - Amritsar Weekly Express (PT)','Dibrugarh','Amritsar')  ON DUPLICATE KEY UPDATE Train_No=124557"
            crs.execute(qry1)
            crs.execute(qry2)
            crs.execute(qry3)
            crs.execute(qry4)
            crs.execute(qry5)
            crs.execute(qry6)
            crs.execute(qry7)
            crs.execute(qry8)
            crs.execute(qry9)
            crs.execute(qry10)
            crs.execute(qry11)
            crs.execute(qry12)
            crs.execute(qry13)
            crs.execute(qry14)
            crs.execute(qry15)
            crs.execute(qry16)
            crs.execute(qry17)
            crs.execute(qry18)
            crs.execute(qry19)
            crs.execute(qry20)
            crs.execute(qry31)
            crs.execute(qry32)
            crs.execute(qry33)
            crs.execute(qry34)
            crs.execute(qry35)
            crs.execute(qry36)
            crs.execute(qry37)
            crs.execute(qry38)
            crs.execute(qry39)
            crs.execute(qry40)
            mydb.commit()
            
            
            crs.close()
            
        except():
            pass
    else:
            print("Password is incorrect,\nPlease enter the correct password.")
            a2=str(input("Enter any number to again apply for password or press any alphabet to exit:"))
            print()
            if a2.isalpha():
                print("Thanks for using our service.")
                break

