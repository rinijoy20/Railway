def Available_ALL_Trains():
                        import mysql.connector as msc
                        mydb=msc.connect(host='localhost',user='root',passwd='mysql',database='railway')
                        crs=mydb.cursor()
                        mydb.autocommit=True
                        crs.execute("use railway")
                        crs.execute("LOAD DATA LOCAL INFILE 'D:/New folder/TRAIN.csv' into table avail_train fields terminated by ',' lines terminated by '\r\n' ;")
                        qry="Select * from avail_train "
                        crs.execute(qry)                                                                                                                             #Use Command to Upload file |LIST-OF-TRAINS| ---->
                        data1 = crs.fetchall()                                                                                                                       #"LOAD DATA LOCAL INFILE 'C:/Users/Jyoti/Desktop/Yash/Train.csv' into table avail_train fields terminated by ',' lines terminated by '\r\n' ;"

                        df = pd.DataFrame(data1, columns=["Srno","Train_No","Train_Name","Train_from","Train_to",])
                        print(df)
                        mydb.commit()
                        crs.close()
                        return("")
