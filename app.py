def calculate_time():

    #This block of code below will be used to know how many times to run subsequent code.

    print('Enter the total amount of entries:')

    try:
        entry_amount = int(input)
    except:
        print('Please enter an integer - a whole number.')
        entry_amount = input()
        while entry_amount.isdigit() == False:
            print('Please enter an integer - a whole number.')
            entry_amount = input()

    entry_amount = int(entry_amount)    #This is to perform operations later on.


    #The next block of code allows the user to enter time entries. The beginning hour is entered first.
    
    for counter in range(0, entry_amount):
        print('Entry ' + str(counter + 1))  #The + 1 is to begin with 'Entry 1' instead of 'Entry 0'
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





calculate_time()
