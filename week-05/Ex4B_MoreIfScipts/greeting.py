# LAB 2 

# Create a script that defines a variable that contains the current hour
# (0-23). Display one of the greetings below based on the current hour: 

current_hour = int(input('Enter the current hour (0-23): '))

#if current_hour < 10:
   # print('Good morning!')
#elif current_hour < 17:
   # print('Good day!')  
#else:
    #print('Good evening!')


#Update your script to include an additional condition that will print “What are you
#doing up so late??” if the hour is between 11pm and 4am.

if 4 < current_hour < 10:
    print('Good morning!')
elif 10 < current_hour < 17:
    print('Good day!')  
elif 17 <= current_hour < 23:
    print('Good evening!')
else:
    print('What are you doing up so late??')