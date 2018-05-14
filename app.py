def calculate_time():

    #This block of code below will be used to know how many times to run subsequent code.

    print('Enter the total amount of entries:')

    try:
        entry_amount = int(input())
    except:
        print('Please enter an integer - a whole number.')
        entry_amount = input()
        while entry_amount.isdigit() == False:
            print('Please enter an integer - a whole number.')
            entry_amount = input()
        entry_amount = int(entry_amount)    #This is to perform operations later on.


    total_time = 0  #This will be used to store entry time values.


    #The next block of code allows the user to enter time entries. The beginning hour is entered first.
    
    for counter in range(0, entry_amount):
        print('\nEntry ' + str(counter + 1))  #The + 1 is to begin with 'Entry 1' instead of 'Entry 0'
        print('Beginning time-')
        print('Enter hour:')

        try:
            beginning_hour = int(input())
            beginning_hour *= 60    #This is to convert the hour to minutes - for later operations.
        except:
            print('Please enter an integer - a whole number.')
            beginning_hour = input()
            while beginning_hour.isdigit() == False:
                print('Please enter an integer - a whole number.')
                beginning_hour = input()
            beginning_hour = int(beginning_hour)
            beginning_hour *= 60



    #The next block of code is used for the beginning minute entries.

        print('Enter minutes:')

        try:
            beginning_minutes = int(input())
        except:
            print('Please enter an integer - a whole number.')
            beginning_minutes = input()
            while beginning_minutes.isdigit() == False:
                print('Please enter an integer - a whole number.')
                beginning_minutes = input()
            beginning_minutes = int(beginning_minutes)



    #This block of code is used to create a float value for the 'hour' and 'minutes' that were previously entered.
    #It takes the beginning hour, which was converted to minutes, and it adds it to the beginning minutes. 
    #This value will be used later to be subtracted from the 'total_ending_time'

        beginning_time = beginning_hour + beginning_minutes
        beginning_time /= 60  #This converts the time back into hours, but now it considers the minutes as well, 
                                #thus giving us a decimal, or float, value.



    #This next block of code will then ask the user for the ending times.

        print('\nEnding time-')
        print('Enter hour:')

        try:
            ending_hour = int(input())
            ending_hour *= 60   #Once again, this is to convert hours to minutes.
        except:
            print('Please enter an integer - a whole number.')
            ending_hour = input()
            while ending_hour.isdigit() == False:
                print('Please enter an integer - a whole number.')
                ending_hour = input()
            ending_hour = int(ending_hour)
            ending_hour *= 60
        


    #The next block of code is for the minute entries.

        print('Enter minutes:')

        try:
            ending_minutes = int(input())
        except:
            print('Please enter an integer - a whole number.')
            ending_minutes = input()
            while ending_minutes.isdigit() == False:
                print('Please enter an integer - a whole number.')
                ending_minutes = input()
            ending_minutes = int(ending_minutes)



    #This block will add up the ending time, and it will be used to subtract the beginning time.

        ending_time = ending_hour + ending_minutes
        ending_time /= 60   #Once again, this is performed to convert minutes to hours.



    #The next block will subtract the beginning_time from the ending_time, and we will output a total for each entry.

        per_entry_time = ending_time - beginning_time
        print('\nThe amount of hours worked for entry ' + str(counter +1) + ' is: ' + str(per_entry_time) + '.')

    


    #This block of code will be used to calculate the total amount of time worked for all entries. 

        total_time += per_entry_time

    print('\nThe total amount of hours you have worked is: ' + str(total_time) + '.')
        

calculate_time()
