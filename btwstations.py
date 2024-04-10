def btw_Stations():
                        import mysql.connector as msc
                        mydb=msc.connect(host='localhost',user='root',passwd='mysql',database='railway')
                        crs=mydb.cursor()
                        mydb.autocommit=True
                        crs.execute("use railway")

                        Sr_train=input("Enter the Source Station.:")
                        De_train=input("Enter the Destination Station.:")
                        qry='select * from avail_train WHERE TRAIN_NO = 12009'
                        crs.execute(qry,)
                        data=crs.fetchall()
                        a=[]
                        for i in data:
                            a.append(i)

                        if len(a)!=1:
                            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')

                        else:
                            print("")
                            print("")
                            print(a)
                            mydb.commit()
                            df = pd.DataFrame(data, columns=["Srno","Train_No","Train_Name", "Train_from" ,  "Train_to"])

                            #print(df)
                            mydb.commit()
                            crs.close()
                        return("")