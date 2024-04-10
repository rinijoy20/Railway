def ticket_booking():
                    import mysql.connector
                    mydb=mysql.connector.connect(host='localhost',
                                                 user='root',
                                                 password="mysql",
                                                 database='railway')
                    crs=mydb.cursor()
                    mydb.autocommit=True
                    Psn_Name=input('Enter  Name.:')
                    Psn_Ph=input('Enter  Phone No.:')
                    Psn_Ph_no=str(Psn_Ph)
                    Psn_age=int(input('Enter age.:'))
                    print()
                    print('               M=MALE','\t','F=FEMALE','\t','N=NOT TO MENTION')
                    while True:
                        Psn_gender=input('Enter  Gender M/F:')
                        if Psn_gender==("M") or Psn_gender==("F"):
                            break
                        else:
                            print("        !~!~!~~ M\F only ~~!~!~!~")
                    Gender=Psn_gender.upper()
                    print()
                    print('Journey Details__')
                    Train_from=input('       From Station.:')
                    Train_to=input('       Destination.:')
                    Scheduled_Date=input('Enter Date of Journey (YYYY-MM-DD):')

                    Pnr_Number="10"+str(Psn_age)+str(rd.randint(100000,999999))
                    Email_ID=input("Enter the Email_ID :")
                    Fare=rd.randint(400,1200)
                    s1="INSERT INTO  Passenger_Details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    data=(Pnr_Number,Psn_Name,Psn_Ph_no,Psn_age,Psn_gender,Train_from,Train_to,Scheduled_Date,Email_ID,Fare)
                    crs.execute(s1,(data),)
                    print()
                    print('  ***TICKET BOOKED SUCCESSFULLY***')
                    print("\t","Your Pnr Number is: ", Pnr_Number)
                    return("")

