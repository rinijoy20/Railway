def Analytics():
        print("""

                    +=====================================================+  
                    |                ****  MAIN MENU  ****                |
                    +=====================================================+
                    |                                                     |      
                    |  1. BAR PLOT :-   Fare  of  Passengers              |
                    |  2. LINE PLOT :-  AC Fare  Of  Trains               |
                    |  3. BAR PLOT :-   Sleeper Fare Of  Trains           |
                    |  4. LINE PLOT :-  Average Distance Covered By Train |
                    |                                                     |                                                  
                    +=====================================================+
                """)
        opt=int(input("""       YOUR OPTION:-"""))

        if opt==1:
                        print(" ")
                        print(bar_plot())

        elif opt==2:
                        print(" ")
                        print(line_plot())

        elif opt==3:
                        print(" ")
                        print(barh_plot())

        elif opt==4:
                        print(" ")
                        print(line1_plot())

        else:
                    print(" ")
                    print("!!!~WRONG CHOICE PLEASE ENTER A VALID VALUE!!!~")





def  bar_plot():
                plt.figure(figsize=(9,6))
                plt.bar(x=["MOHAN","ROHIT","CARL","MARK","VON","RONIT","SUNIT"],
                height=[720,452,1123,558,320,750,950],color='midnightblue')
                plt.xticks(rotation=45)
                plt.title("Fare of Passengers")
                plt.savefig("Fare of Passengers.png")
                plt.show()
                return("")

def line_plot():
                print("Line Plot")
                x=["Goa Express","JammuTavi Superfast","Punjab Mail Express","Dakshin Express","Delhi-Mumbai Shatabdi"]
                y=[4500,8500,3600,7600,12000]
                plt.title("AC Fare Of Trains",fontsize=14,color="g")
                plt.xlabel("Trains",fontsize=14,color="g")
                plt.ylabel("AC Fare",fontsize=14,color="g")
                plt.xticks(rotation=12)

                plt.plot(x,y, marker="X",ls="dashed",linewidth=4, color="m")
                plt.savefig("AC Fare For Trains.png")
                plt.show()
                return("")

def barh_plot():
                print("Horizontal Bar Plot")
                x=["Goa Express","JammuTavi Superfast","Punjab Mail Express","Dakshin Express","Delhi-Mumbai Shatabdi"]
                y=[1500,4500,2600,7600,9000]
                plt.title("Sleeper Fare  Of  Trains",fontsize=14,color="b")
                plt.xlabel("Trains",fontsize=14,color="c")
                plt.ylabel("Sleeper Fare",fontsize=14,color="c")
                plt.barh(x,y, color="y", edgecolor="pink")
                plt.savefig("Sleeper Fare Of Trains.png")
                plt.show()
                return("")

def line1_plot():
        print("Line Plot")
        x=["Goa Express","JammuTavi Superfast","Punjab Mail Express","Dakshin Express","Delhi-Mumbai Shatabdi"]
        y=[500,1200,650,750,1350]
        plt.title("Average Distance Covered By Train",fontsize=14,color="c")
        plt.xlabel("Trains",fontsize=14,color="c")
        plt.ylabel("(Distance in Kms)",fontsize=14,color="r")
        plt.plot(x,y, marker="o", label="Avg Distance")
        plt.xticks(rotation=17)
        plt.legend()
        plt.savefig("Avearage Distance By Trains.png")
        plt.show()
        return("")


