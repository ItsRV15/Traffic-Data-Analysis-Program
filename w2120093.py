#Author:Ravindu Isurantha Ranasinghe
#Date:08/12/2024
#Student ID:w2120093

# Task A: Input Validation
def validate_date_input():#Define the function
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """


    
    
    while True:
        while True: #if the user inputs wrong date range the question will be asked again
            try:
                    
                day=int(input("please enter the day of the survey in the format DD:")) #ask user to enter the date
                
                if day>31 or day<1:    #checks whether the date entered by the user is incorrect
                    print("out of range-Values must be in the range 1 and 31")
                    continue    #if the user input is out of the range the loop will be run again
                break       #loop stops when the user inputs a month in the correct range
             
            except ValueError:#checks if there is another data type entered instead of a integer
                print("Integer required")
                



        while True:  #if the user inputs wrong month range the question will be asked again
            try:
                month=int(input("please enter the month of the survey in the format MM:"))#ask user to enter the month
                if month>12 or month<1:   #checks whether the month entered by the user is incorrect
                    print("please range-Values must be in the range 1 and 12")
                    continue    #if the user input is incorrect the loop will be run again
                break       #loop stops when the user inputs a month in the correct range

            except ValueError:  #checks if there is another data type entered instead of a integer
                print("Integer required")
                

                
            
        
        while True:#if the user inputs wrong year range the question will be asked again
            try:
                    
                year=int(input("please enter the year of the survey in the format YYYY:"))  #ask user to enter the year
                if year>2024 or year<2000:   #checks whether the year entered by the user is incorrect
                    print("out of range-Values must be in an range 2000 and 2024")
                    continue   #if the user input is incorrect the loop will be run again
                break     #loop stops when the user inputs a month in the correct range

            except ValueError:    #checks if there is another data type entered instead of a integer
                print("Integer required")






        leap_year=(year%4==0 and year % 100 !=0) or (year%400==0) #Checking leap year
     

      
        if month in [4,6,9,11] and day > 30: #checks if the month is April, June, September, or November, and whether the day is greater than 30
            print("Out of range-Date must be range from 1 to 30")
            continue #skip the rest of the current loop iteration, prompting the user again
        if month ==2:
            if leap_year and day >29: #Checks whether the month is february,if it is a leap year and day is greater than 29 
                print ("This is a leap year therefore the date must be in range 1-29")
                continue
            elif not leap_year and day >28: #if the year is not a leap year it checks whether the month of Feb has only 28 days 
                print ("This is not a leap year so the month of february has only 28 days in this year")
                continue
        break #exits the loop and the program proceeds



    formatted_day=str(day).zfill(2) #Format numbers as strings with leading zeros(if the user inputs 6 it becomes 06)/chatgbt
    formatted_month=str(month).zfill(2) #Format numbers as strings with leading zeros
    date=f"{formatted_day}/{formatted_month}/{year}" #Extracting the date for the histogram
    
    
       
          

    filename="traffic_data"+formatted_day+formatted_month+str(year)+".csv" #Getting the file name according to the user inputs
    return filename,date #Returning the filename to assign for a varaiable in the main loop





   
            


def validate_continue_input(): #Defining the function
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
        
    
    while True:  #ask the user to enter again if the format is wrong
        user=input("Do you want to select another data file for a different date? Y/N:") #Getting user input
        if user=="Y" or user=="y": #checks whether user input is y or Y(checks whether he wants to load another dataset)

                MultiCSVProcessor().process_files()#Calling the main loop from MultiCSvprocessor class(part E)
                return #exits this loop after calling once 

        elif user=="N" or user=="n":  #checks whether user input is n or N(checks whether he wants to end the task)
            print("End of run")
            return #program will be stopped  
        else:
            print("please enter \"Y\" or \"N\" ")  #Informs the user that his input is incorrect
            
            










# Task B: Processed Outcomes


def process_csv_data(file_path):
    
    junName=[]
    time=[]
    directionIn=[]
    directionout=[]
    weather=[]
    junction_speedlimit=[]
    vehicle_speed=[]                  #Assigning the 1st line of the file(Header part)to a  avariable to remove it from the dataset
    vehicle_type=[]
    electric_hybrid=[]
    outcomes=[]
    outcomes.append(file_path)


    file=open(file_path,'r')  #opening the file to read
       
    

    title=file.readline().strip()#Read the header part of the dataset and assigning to a variable to remove it from the dataset

    for line in file: # Read each line in the file upto last line in the file after the header
            
        line=line.strip()     #reads the csv file line by line and remove\n and whitespaces
        if line:  #make sure the line is not empty
               
            JunctionName,Date,timeOfDay,travel_Direction_in,\
            travel_Direction_out,Weather_Conditions,JunctionSpeedLimit,VehicleSpeed,VehicleType,elctricHybrid=line.split(",")

#This line splits the current line by commas (,)and Unpack the line into individual components and assigns each value to the corresponding  variable
#Each variable corresponds to a specific piece of data from the line


        #Appending all the data stored in variables to the relavant list
            junName.append(JunctionName)
            time.append(timeOfDay)
            directionIn.append(travel_Direction_in)
            directionout.append(travel_Direction_out)
            weather.append(Weather_Conditions)
            junction_speedlimit.append(JunctionSpeedLimit)
            vehicle_speed.append(VehicleSpeed)
            vehicle_type.append(VehicleType)
            electric_hybrid.append(elctricHybrid)
    file.close() #closing the file



    #Finding total no of vehicle count
    vehicle_count=len(vehicle_type)  #getting the length of vehicle_type list
    outcomes.append(vehicle_count)#Add the vehicle count to the outcomes list
    





    #Finding total no of trucks

    trucksCount=0  #Defines a variable to 0
    for i in range(len(vehicle_type)): #Loop runs untill end of the list
        if vehicle_type[i]=="Truck": #Going thrue each elemnet in the vehicle_type list to checks for trucks
            trucksCount=trucksCount+1 #Increment the trucks count                                         
    
    outcomes.append(trucksCount) #appending trucks count to the outcomes list




    #Finding total no of electric vehicles for this date

    Evehicles=0
    for i in range(len(electric_hybrid)):#Loop runs untill end of the electric_hybrid list
        if electric_hybrid[i]=="True": ##Going thrue each elemnet in the electric_hybrid  list to checks for electric hybrid vehicle
            Evehicles=Evehicles+1  #Increment the trucks count   
    outcomes.append(Evehicles) #appending trucks count to the outcomes list







    #Finding total no of two wheeled vehicles

    two_wheel=0
    for i in range(len(vehicle_type)):#Loop runs untill end of the vehicle_type list
        if vehicle_type[i]=="Motorcycle"or  vehicle_type[i]=="Bicycle" or  vehicle_type[i]=="Scooter": 
            #Going thrue each elemnet in the vehicle_type  list to checks for motorcycles,bicycle and scooters                                                                                           in the vehicle_type list to checks for trucks
            two_wheel=two_wheel+1 #Increment the count
    
    outcomes.append(two_wheel)







    #Finding total no of busses leaving Elm Avenue/Rabbit Road juction and have direction out N
    
    bus=0
 
    for i in range(len(vehicle_type)):#Loop runs untill end of the vehicle_type list
        if vehicle_type[i]=="Buss" and directionout[i]=="N" and junName[i]=="Elm Avenue/Rabbit Road":
            #Going thrue each elemnet in the vehicle_type list to checks for busses
            #Going thrue each elemnet in the directionout list to checks for "N" 
            #Going thrue each elemnet in the junName list to checks for Elm avenue
            
            bus=bus+1#Increment the count
    
    outcomes.append(bus)#Appending to the list

            

    
            
    #Finding total number of vehicles through both junctions not turning left or right

    straight_vehicle=0
    for i in range(len(vehicle_type)): #Loop runs untill end of the vehicle_type list
        if directionIn[i]==directionout[i]: #Going thrue each elemnet in the lists and checks for vehicles going forward

            straight_vehicle= straight_vehicle+1 #Increment the count
    outcomes.append(straight_vehicle) #Appending to the outcomes list

    
    



    #Finding the percentage of total vehicles that are trucks

    percentage=(trucksCount/len(vehicle_type))*100 #Dividing the trucks count from total no vehicles and multiply by 100
    perTrucks=round(percentage) #Rounding the percentage
    outcomes.append(perTrucks)#Appending to the outcomes list
    


   
    #Finding the average number of bikes per hour
    
    bikecount=0
    for i in range(len(vehicle_type)):#Loop runs untill end of the vehicle_type list
        if vehicle_type[i]=="Bicycle": #Going thrue each elemnet in the vehicle_type list to checks for bicycles
            bikecount=bikecount+1 #Increment the bike count
    avgbikes=round(bikecount/24) #Getting the avg of bikecount according to the overall vehicle count
    outcomes.append(avgbikes)#Appending to the outcomes list
    





    #total number of vehicles going over the speed limit
    
    speeding=0
    for i in range(len(vehicle_type)):#Loop runs untill end of the vehicle_type list
        if int(vehicle_speed[i])>int(junction_speedlimit[i]) : #converting to an integer since everything in the list is stored as strings 
            speeding+=1 
    outcomes.append(speeding)
    








    #Total number of vehicles recorded through Elm Avenue/ Rabbit Road
    
    EAPass=0
    for i in range(len(vehicle_type)):#Loop runs untill end of the vehicle_type list 
        if  junName[i]=="Elm Avenue/Rabbit Road":#checks for the vehicle going through elm avenue
            EAPass+=1 
    outcomes.append(EAPass)
    



    

    #Total number of vehicles recorded through Hanley Highway/Westway
    
    HHPass=0
    for i in range(len(vehicle_type)): #Loop runs untill end of the vehicle_type list
        if junName[i]=="Hanley Highway/Westway":#checks for the vehicles going through hanley highway
            HHPass+=1 
    outcomes.append(HHPass)
    



    #Percentage of scooters going throughhe Elm avenue junction

    scooters=0
    for i in range(len(vehicle_type)): 
        if junName[i]=="Elm Avenue/Rabbit Road" and vehicle_type[i]=="Scooter":#Checks for scooters going through elm avenue
            scooters+=1     #Increment the count                                                       
    
    Spercentage=int((scooters/EAPass)*100)#Rounding to the integer

    outcomes.append(Spercentage)



    


    
    def getting_hlist(junction):#Defining a function to reuse
        
        hours=[] #Defining a empty list
        for i in range(len(vehicle_type)):##Loop runs untill end of the vehicle_type list( going through Each and every record)
            if junName[i]==junction:#Checks for the vehicles that going through the relavant junction
                h,mins,secs=time[i].split(":")#Splitting the time of all vehicles that going through the relavant junction
                                                                       #and assigning to the relavant variables
                hours.append(int(h))#Appending the hours to the hours list as integerrs


      
        hoursList=[] 
        for i in range(24): #uses a for loop to find out how many vehicles per hour 
            count_hours=hours.count(i)#
            hoursList.append(count_hours) # adds the nuber of vehicles per hour to a new list

        return hoursList

    hoursList=getting_hlist("Hanley Highway/Westway")#Calling the above fuction for the Hanley Highway/westway


    peak=max(hoursList) #finding the max vehivles out of all hours 
    index_peak=hoursList.index(peak)# finding the index where the max number of vehicles are in the list 
    outcomes.append(peak) # appending the peak num of vehicles to the outcomes list 
    outcomes.append(index_peak)#appending the peak time to the outcomes list 







    #finding the number of hours that rained 
    raining_time=[] 
    for i in range(len(vehicle_type)): #going through each and every record to find out the hours it rained 
        if weather[i]=="Light Rain" or "Heavy Rain": 
            h,mins,sec=time[i].split(":") #extracts the hour from the time
            raining_time.append(int(h))#adds the time to the rain time list 



    raining_time=list(set(raining_time))#takes care of repeated hours 
    raining_hours=len(raining_time)#finding the number of hours 
    outcomes.append(raining_hours)#adding to the outcomes list


    #This is to extarct the data for the histogram

    ElmA_List=getting_hlist("Elm Avenue/Rabbit Road")#Calling the function and retrieves and returns a list of data related to Elm avenue
    HanleyH_List=getting_hlist("Hanley Highway/Westway")##Calling the function and retrieves and returns a list of data related to hanley highway
    traffic_data={"Elm Avenue/Rabbit Road":ElmA_List,
                  "Hanley Highway/Westway":HanleyH_List}#Making a traffic data dictionary so it can be added to the histogram
    outcomes.append(traffic_data)#Appending the traffic_data dictionary to the outcomes list







    return outcomes # returns the outcomes list so it can be used for displaying 




    







def display_outcomes(outcomes): #Defining a function
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
  #printing the results in the outcomes list according to the index
    print("**************")
    print("data file selected is",outcomes[0])
    print("**************")
    print("The total number of vehicles recorded for this date is ",outcomes[1])
    print("The total number of trucks recorded for this date is ", outcomes[2])
    print("The total number electric vehicles for this date is",outcomes[3])
    print("The total number of two-wheeled vehicles for this date is ",outcomes[4])
    print("The total number of Busses leaving Elm Avenue/Rabbit Road heading North is",outcomes[5])
    print("The total number of Vehicles through both junctions not turning left or right is",outcomes[6])
    print("The percentage of total vehicles recorded that are trucks for this date is", str(outcomes[7])+"%")
    print("The average number of Bikes per hour for this date is",outcomes[8])
    print("")
    print("")
    print("The total number of Vehicles recorded as over the speed limit for this date is",outcomes[9])
    print("The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is",outcomes[10])
    print("The total number of vehicles recorded through Hanley Highway/Westway junction is",outcomes[11])
    print(str(outcomes[12])+"%","of vehicles recorded through Elm Avenue/Rabbit Road are Scooters")
    print("")
    print("")
    print("The highest number of vehicles in an hour on Hanley Highway/Westway is",outcomes[13])
    print("The most vehicles through Hanley Highway/Westway were recorded between",str(outcomes[14])+":00","and",str(outcomes[14]+1)+":00")
    print("The number of hours of rain for this date is",outcomes[15])
   
    







   
    












# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):#Defining a function
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    output_lines = [
        "********************",
        f"Data file selected is {str(outcomes[0])}",
        "********************",
        f"The total number of vehicles recorded for this date is {str(outcomes[1])}",
        f"The total number of trucks recorded for this date is {str(outcomes[2])}",
        f"The total number of electric vehicles for this date is {str(outcomes[3])}",
        f"The total number of two-wheeled vehicles for this date is {str(outcomes[4])}",
        f"The total number of buses leaving Elm Avenue/Rabbit Road heading North is {str(outcomes[5])}",
        f"The total number of vehicles through both junctions not turning left or right is {str(outcomes[6])}",
        f"The percentage of total vehicles recorded that are trucks for this date is {str(outcomes[7])}%",
        f"The average number of bikes per hour for this date is {str(outcomes[8])}",
        "",
        f"The total number of vehicles recorded as over the speed limit for this date is {str(outcomes[9])}",
        f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {str(outcomes[10])}",
        f"The total number of vehicles recorded through Hanley Highway/Westway junction is {str(outcomes[11])}",
        f"{str(outcomes[12])}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters",
        "",
        f"The highest number of vehicles in an hour on Hanley Highway/Westway is {str(outcomes[13])}",
        f"The most vehicles through Hanley Highway/Westway were recorded between {str(outcomes[14])}:00 and {str(outcomes[14]+1)}:00",
        f"The number of hours of rain for this date is{outcomes[15]}"
    ]#Define a list and add the outputs as string-To display in results.txt



    file2=open(file_name,'a')#opening a file to append
    for line in output_lines:#going through each element in the list
        file2.write(line + '\n')#write each element in a new line
                   
    file2.close()#closing the file









from graphics import *

class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        #Assigning the respective parameters to the respective attributes
        self.traffic_data = traffic_data
        self.date = date

        #assigning the width and height to the respective attributes
        self.width=1000
        self.height=500

        #Colours of the two bars are assigned to the self.colours attribute
        self.colours=[color_rgb(51,153,255),color_rgb(0,204,204)]
        

    def setup_window(self):
        """
        Sets up the  window  for the histogram.
        """
        self.window=GraphWin("Histogram",self.width,self.height)#This creates the window
        title=Text(Point(315,25), f"Histogram of Vehicle Frequency per Hour ({self.date})")#Getting a title for the window
        title.setSize(14)#Set the size of the title to 15
        title.setStyle("bold")#Makes the tittle bold
        title.draw(self.window)#Displays the title on the window

        



        
         # Setup logic for the window and canvas

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """

        x_axis= Line(Point(65,self.height-60 ), Point(self.width-65, self.height-60))#Drawing the horizontal line
        x_axis.draw(self.window)#Displays the line on the window

        #Drawing a name for x axis
        
        x_name=Text(Point(500,self.height-25),"Hours 00:00 to 24:00")#Adding a text under the line
        x_name.setSize(10)#set the size of the title to 10
        x_name.setStyle("bold")#Makes the text bold
        x_name.draw(self.window)#Displays the text on the window



        #Assigning label for x axis

        for hour in range(24):#Labelling the x axis with 00-24
            x_label=Text(Point((hour*37)+75,self.height-50),f"{hour:02}")#calculates the position where the text label will be placed
                                                                          #Formats the hour variable to ensure it's always two digits
            x_label.setSize(9)#set the size of the title to 10
            x_label.draw(self.window)#Displays the text on the window


         #Finding the highest no of vehicle from the both lists

        junctions=list(self.traffic_data.keys())#Takes the junction names by extarcting the keys in the dictionary and adding to a list
        max_volume=0#Assigning a variable to 0
        for data in self.traffic_data.values():#Iterates over the values of the traffc data dictionary
            if max(data)>max_volume:#Checks whether the maximum of the list is greater than the max volume
                max_volume=max(data)#Then assign the max value in the list to the max volume



          #Drawing the bars
        junction_number=0 #Intializing a junction number
        for junction in junctions:#Iterates over the junction names

            data=self.traffic_data[junction]#Takes the list of data from the corrsponding junction
            width=14#set the width of the bar to 14
            if junction_number==0:#This code runs for the firts junction
                for i in range(len(data)):#Goes through each element in the list of the 1st junction

                
                    #Find the 2 x and y coordinates that are needed to draw the bars of the first junction(rectangle)
                    x1=60+((i*37))
                    x2=x1+width
                    y1=self.height-60
                    y2=self.height-100-(data[i]/max_volume)*250#Calculating the height based on the scaled data value



                    bar=Rectangle(Point(x1,y1),Point(x2,y2))#Draws the bar using the rectangle function in the graphics.py
                    bar.setFill(self.colours[0])#Setting the first colour to the all bars in the firt junction
                    bar.draw(self.window)#Displays the 1st junction bars

                    #Adding the labels over the bar to show the frequency
                    bar_label=Text(Point((x1+x2)/2,y2-6),f"{data[i]}")
                    bar_label.setSize(7)
                    bar_label.setFill(self.colours[0])#Taking the same colour of the bar to the label
                    bar_label.setStyle("bold")
                    bar_label.draw(self.window)#Displays the labels



            else:#this code will run for the 2nd junction
                for i in range(len(data)):#Goes through each element in the list of the 2nd junction
                    x1=(60+width)+((i*37))
                    x2=x1+width
                    y1=self.height-60
                    y2=self.height-100-(data[i]/max_volume)*250#Calculating the height based on the scaled data value




                    
                    bar=Rectangle(Point(x1,y1),Point(x2,y2))#Draws the bar using the rectangle function in the graphics.py
                    bar.setFill(self.colours[1])#Setting the second colour to the all bars in the second junction
                    bar.draw(self.window)#Displays the 2nd junction bars

                      #Adding the labels over the bar to show the frequency
                    bar_label=Text(Point((x1+x2)/2,y2-6),f"{data[i]}")
                    bar_label.setSize(8)
                    bar_label.setFill(self.colours[1])#Taking the same colour of the bar to the label
                    bar_label.setStyle("bold")
                    bar_label.draw(self.window)#Displays the labels of the 2nd bars in the window





            junction_number+=1#Increment the junction number afeter the iteration


                    










    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        #Adding the list legend
        legend1=Rectangle(Point(70,65),Point(85,50))#Drawing the 1st legend
        legend1.setFill(self.colours[0])#setting the colour of the legend according to the bar it represents
        legend1.draw(self.window)#Draw the legend in the window

        legend_label1=Text(Point(180,55),"Elm Avenue/Rabbit Road")#Adding text to the 1st legend
        legend_label1.draw(self.window)#Displays the text infront of the legend




         #Adding the list legend
        legend2=Rectangle(Point(70,85),Point(85,70))#Drawing the 2nd legend
        legend2.setFill(self.colours[1])#setting the colour of the legend according to the bar it represents
        legend2.draw(self.window)#Draw the legend in the window
        
        legend_label2=Text(Point(180,80),"Hanley Highway/Westway")#Adding text to the 1st legend
        legend_label2.draw(self.window)#Displays the text infront of the legend

        

        






        

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """



        self.setup_window()#Calling the function to setup the window
        self.draw_histogram()#Calls the function to draw the histogram
        self.add_legend()#Calls a function to add a legend
        self.window.getMouse()#keeps the window open till the mouse is clicked on the window
        self.window.close()#When the mouse is clicked on the window it will close

        








# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None
        self.filename=""
        self.outcomes=""
        self.Histogram=""
        






    def load_csv_file(self, file_path):
        """
        Loads a CSV file and processes its data.
        """
        self.outcomes=process_csv_data(file_path)# to open the file with the given date and process the data
        return self.outcomes
        
       

        




    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        self.current_data = None
        self.filename=""
        self.outcomes=""
        self.Histogram=""

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        validate_continue_input()

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        
        while True:#Loops if the file i not found
            self.clear_previous_data()
            self.filename,self.date= validate_date_input()#to get the date input from the user
            
            try:
                self.load_csv_file(self.filename)
                
            except FileNotFoundError:#Checking whether there is a file for the entered date
                print("The file has not been found. Please Try again")#If there is a not a file for the entered date it gives an error
                continue#Loops continues from here so the user will be prompted with the date again
                
            display_outcomes(self.outcomes) #to display the procced data
            save_results_to_file(self.outcomes, file_name="results.txt")#Saving the results to the results.txt file
            self.Histogram=HistogramApp(self.outcomes[-1],self.date)#Creates an instance of HistogramApp with the correct date
            #and the traffic_data dictionary that is stored in the last element of the outcomes list

            self.Histogram.run()#Creates the histogram using.run function
            self.handle_user_interaction()#looping again and asking user whether he wants to check for another date
            break #Ending the loop
        





MultiCSVProcessor().process_files() #calling the class in task E to run the main loop


