 def self_booked_ticket():
                        import mysql.connector as msc
                        mydb=msc.connect(host='localhost',user='root',passwd='mysql',database='railway')
                        crs=mydb.cursor()
                        mydb.autocommit=True
                        Self_Pnr=int(input('Enter your Pnr_number No:'))
                        crs.execute('select * from passenger_details where Pnr_Number=(%s)',(Self_Pnr,))
                        data=crs.fetchall()
                        a=[]
                        for i in data:
                            a.append(i)

                        if len(a)!=1:
                            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')

                        else:
                            print(a)
                            mydb.commit()
                        return("")