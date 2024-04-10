def railsmenu():
                                print("""
                    
                                       +====================================+  
                                       |      ****  MAIN MENU  ****         |
                                       +====================================+
                                       |                                    |      
                                       |  1. Ticket Booking                 |
                                       |  2. Train_btw_Stations             |   
                                       |  3. Train List                     |
                                       |  4. Your Ticket                    |                                     
                                       |  5. Ticket Cancellation            |
                                       |  6. Analytics                      |
                                       |  7. Exit                           |
                                       |                                    |         
                                       |                                    |
                                       +====================================+
                                  """)
                                    #break
                                x=int(input("""YOUR OPTION:-"""))

                                if x==1:
                                        ticket_booking()

                                elif x==2:
                                          print(" ")
                                          print(btw_Stations())

                                elif x==3:
                                          print(" ")
                                          print("-----FOLLOWING TRAINS ARE AVAILABLE-----")
                                          print(" ")
                                          print(Available_ALL_Trains())

                                elif x==4:
                                          print(" ")
                                          print(self_booked_ticket())

                                elif x==5:
                                          print(" ")
                                          print(ticket_cancellation())


                                elif x==6:
                                          print(" ")
                                          print(Analytics())

                                elif x==7:
                                          print(" ")
                                          print("\n"
                                                  "      \n"
                                                  "          ##======================================================##\n"
                                                  "          ||                      THANK YOU                       ||\n"
                                                  "          ##======================================================##\n"
                                                                                                                              "\n")
                                          print('''
                        
                                                   DEVELOPED BY syed
                                                ''')


                                else:
                                     print(" ")
                                     print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
                                return("")

