    # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
    # Any code taken from other sources is referenced within my code solution. 
    # Student ID: 18169634
    # Date: 24/10/2021
#####################################################################
#STAFF VERSION
#####################################################################
pcount=0                                                #sets the counts of each predicted outcome
pmtcount=0
dcount=0
dnpcount=0 
ecount=0
f= open("Marks.txt","w+")                               # creates the text file                                      
while True: 
    list=[]     #creates a list for the marks and predicted outcomes
    while True:
        while True:
            while True:                                 #inputs and valuechecks for marks
                rule=(0, 20, 40, 60, 80, 100, 120)
                pmark = input("\nPlease enter the pass credit : ")
                try:
                    pmark = int(pmark)                  #converts the mark inputed to an integer
                    break
                except ValueError:                      #checks to make sure the mark is an integer and if not prompts user to reinput a integer
                    print("\nInteger required")
            
            if pmark in rule:
                pmark=str(pmark)
                list.append(pmark+",")                  #adds the marks to the list =source- https://stackoverflow.com/questions/36962479/how-to-store-user-input-into-list-on-python
                pmark=int(pmark)                            
                break                                   
            else :
                print("Out of range - please only enter 0,20,40,60,80,100,120")
        while True:
            while True:
                rule=(0, 20, 40, 60, 80, 100, 120)
                dmark = input("\nPlease enter the defer credit : ")
                try:
                    dmark = int(dmark)
                    break
                except ValueError:
                    print("\nInteger required")
            
            if dmark in rule:
                dmark=str(dmark)
                list.append(dmark+",")
                dmark=int(dmark)  
                break
            else :
                print("Out of range - please only enter 0,20,40,60,80,100,120")
        while True:
            while True:
                rule=(0, 20, 40, 60, 80, 100, 120)
                fmark = input("\nPlease enter the fail credit : ")
                try:
                    fmark = int(fmark)
                    break
                except ValueError:
                    print("\nInteger required")
            
            if fmark in rule:
                fmark=str(fmark)
                list.append(fmark+",")
                fmark=int(fmark)   
                break
            else :
                print("Out of range - please only enter 0,20,40,60,80,100,120")
        total=pmark+dmark+fmark                         #checks if the total is equal to 120 if not it displays that is not correct and asks user to input correct values
        if total == 120:
            break
        else :
            print("Total incorrect - Total is not equal to 120 please re-enter")
            list=str(list)
            f.write(list)
            f.write("\nPlease disregard past three entires as they are not valid-"+list+"\n")  #if the results do not add up to 120 its writes to the text file to tell the user that the past results are not valid 
            list=[]                 #clears the list so that we can write new data
            ##pass==100      = progress module trailer
            ##pass==120      = pass
            ##fail>=80       = exclude
            ##fail<=80       = Do not Progress – module retriever
    while True:
        list=str(list)                                   #converts the integers in the list to a string
        if pmark==120:
            print("\nProgress")
            pcount=pcount+1
            f.write("Progress - "+list+"\n")                      #writes the predicted outcome infront of the list
            break
        elif pmark==100:
            print("\nProgress (Module Trailer)")
            pmtcount=pmtcount+1
            f.write("Progress (Module Trailer) - "+list+"\n")
            break
        elif fmark>=80:
            print("\nExclude")
            ecount=ecount+1
            f.write("Exclude - "+list+"\n")
            break
        elif fmark<=80:
            print("\nDo not Progress – Module Retriever")
            f.write("Do not Progress - Module Retriever"+list+"\n")
            dnpcount=dnpcount+1
            break
    list=()  #clears the list after the data is written to the text file so that we can write new data to the list
    #asks for q or y to continue or quit - source - https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input/30247200
    while True:
        quitorcontinue = str(input('\nPlease enter y to continue or q to quit and view results: '))
        quitorcontinue = quitorcontinue.lower()     #converts the input to lowercase to avoid errors if a uppercase letter if entered
        if quitorcontinue in ('y', 'q'):
            break
        print("\nPlease only enter y to continue or q to quit and view results")
        quitorcontinue = quitorcontinue.lower()
    if quitorcontinue == 'y':
        continue
    else:
        quitorcontinue == 'q'
        break
f.close()
while True:    
    while True:
        h_or_v = str(input('\nPlease enter h for horizontal histogram or v for vertical histogram: '))  #asks the user if they want the horizontal or vertical histogram via input of h or v
        h_or_v = h_or_v.lower()      
        if h_or_v in ('h', 'v'):
            break
        print("\nPlease only enter h for horizontal histogram or v for vertical histogram")
        h_or_v = h_or_v.lower() 
    if h_or_v == 'h':
        #histogram horizontal
        print("--------------------------------------------------------------------------------------------------")
        print("\n Horizontal Histogram")
        print("--------------------------------------------------------------------------------------------------")
        print("Progress,",pcount,"-                           ",pcount*'*')
        print("Exclude,",ecount,"-                            ",ecount*'*')
        print("Progress (Module Trailer)",pmtcount,"-           ",pmtcount*'*')
        print("Do not Progress - Module Retriever",dnpcount,"-  ",dnpcount*'*')
        print("\nTotal Number Of Outcomes = ",+ecount+dnpcount+pcount+pmtcount,"\n")  
        #displays the total number of outcomes by adding each predicted outcome together as each student can only have one predicted outcome
        print("--------------------------------------------------------------------------------------------------")
        # prints the contents of the text file
        f=open('Marks.txt','r')     #https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python
        file_contents = f.read()
        print (file_contents)
        f.close()
    else:
        h_or_v == 'v'
        #vertical histogram
        #create new variables for pass, exclude,progress module trailer and do not progress module retriever for each row in the histogram
        #first row
        #prow1
        #erow1
        #pmtrow1
        #dnprow1
        ##checks if there should be a * for the first row in the histogram if not it prints blank
        if pcount >=1:  
            prow1='*'
        else:
            prow1=' '
        if ecount >=1: 
            erow1='*'
        else:
            erow1=' '
        if pmtcount >=1:  
            pmtrow1='*'
        else:
            pmtrow1=' '
        if dnpcount >=1:  
            dnprow1='*'
        else:
            dnprow1=' '
        ##checks if there should be a * for the second row in the histogram if not it prints blank
        if pcount >=2:  
            prow2='*'
        else:
            prow2=' '
        if ecount >=2: 
            erow2='*'
        else:
            erow2=' '
        if pmtcount >=2:  
            pmtrow2='*'
        else:
            pmtrow2=' '
        if dnpcount >=2:  
            dnprow2='*'
        else:
            dnprow2=' '
            
        ##checks if there should be a * for the third row in the histogram if not it prints blank
        if pcount >=3:  
            prow3='*'
        else:
            prow3=' '
        if ecount >=3: 
            erow3='*'
        else:
            erow3=' '
        if pmtcount >=3:  
            pmtrow3='*'
        else:
            pmtrow3=' '
        if dnpcount >=3:  
            dnprow3='*'
        else:
            dnprow3=' '

        ##checks if there should be a * for the fourth row in the histogram if not it prints blank
        if pcount >=4:  
            prow4='*'
        else:
            prow4=' '
        if ecount >=4: 
            erow4='*'
        else:
            erow4=' '
        if pmtcount >=4:  
            pmtrow4='*'
        else:
            pmtrow4=' '
        if dnpcount >=4:  
            dnprow4='*'
        else:
            dnprow4=' '

        ##checks if there should be a * for the fifth row in the histogram if not it prints blank
        if pcount >=5:  
            prow5='*'
        else:
            prow5=' '
        if ecount >=5: 
            erow5='*'
        else:
            erow5=' '
        if pmtcount >=5:  
            pmtrow5='*'
        else:
            pmtrow5=' '
        if dnpcount >=5:  
            dnprow5='*'
        else:
            dnprow5=' '
        ##checks if there should be a * for the sixth row in the histogram if not it prints blank
        if pcount >=6:  
            prow6='*'
        else:
            prow6=' '
        if ecount >=6: 
            erow6='*'
        else:
            erow6=' '
        if pmtcount >=6:  
            pmtrow6='*'
        else:
            pmtrow6=' '
        if dnpcount >=6:  
            dnprow6='*'
        else:
            dnprow6=' '
        #prints the vertical histogram row by row
        print("--------------------------------------------------------------------------------------------------")
        print("Vertical Histogram")
        print("--------------------------------------------------------------------------------------------------")
        print("Progress",pcount," | ""Exclude",ecount," | ""Progress (Module Trailer)",pmtcount," | ""Do not progress - module retriever",dnpcount)
        print(" ",prow1,"           ",erow1,"                    ",pmtrow1,"                            ",dnprow1)
        print(" ",prow2,"           ",erow2,"                    ",pmtrow2,"                            ",dnprow2)
        print(" ",prow3,"           ",erow3,"                    ",pmtrow3,"                            ",dnprow3)
        print(" ",prow4,"           ",erow4,"                    ",pmtrow4,"                            ",dnprow4)
        print(" ",prow5,"           ",erow5,"                    ",pmtrow5,"                            ",dnprow5)
        print(" ",prow6,"           ",erow6,"                    ",pmtrow6,"                            ",dnprow6)
        print("--------------------------------------------------------------------------------------------------")
        print("\nTotal Number Of Outcomes = ",+ecount+dnpcount+pcount+pmtcount,"\n")
        f=open('Marks.txt','r')
        file_contents = f.read()
        print (file_contents)
        f.close()
        break
    break

#######################################################################
###STUDENT VERSION
#######################################################################
##while True:
##    while True:
##        ##inputs and valuechecks for marks
##        while True:
##            rule=(0, 20, 40, 60, 80, 100, 120)
##            pmark = input("\nPlease enter the pass credit : ")
##        #converts the mark inputed to an integer
##        #checks to make sure the mark is an integer and if not prompts user to reinput a integer
##            try:
##                pmark = int(pmark)
##                break
##            except ValueError:
##                print("\nInteger required")
##        
##        if pmark in rule:
##            break
##        else :
##            print("Out of range - please only enter 0,20,40,60,80,100,120")
##    while True:
##        while True:
##            rule=(0, 20, 40, 60, 80, 100, 120)
##            dmark = input("\nPlease enter the defer credit : ")
##            try:
##                dmark = int(dmark)
##                break
##            except ValueError:
##                print("\nInteger required")
##        
##        if dmark in rule:
##            break
##        else :
##            print("Out of range - please only enter 0,20,40,60,80,100,120")
##    while True:
##        while True:
##            rule=(0, 20, 40, 60, 80, 100, 120)
##            fmark = input("\nPlease enter the fail credit : ")
##            try:
##                fmark = int(fmark)
##                break
##            except ValueError:
##                print("\nInteger required")
##        
##        if fmark in rule:
##            break
##        else :
##            print("Out of range - please only enter 0,20,40,60,80,100,120")
##
##    #checks if the total is equal to 120 if not it displays that is not correct and asks user to input correct values
##    total=pmark+dmark+fmark
##    if total == 120:
##        break
##    else :
##        print("Total incorrect - Total is not equal to 120 please re-enter")
##        
##        ##pass=100  = progress module trailer
##        ##pass=120       = pass
##        ##fail>=80       = exclude
##        ##fail<=80       = Do not Progress – module retriever
##while True:
##    if pmark==120:
##        print("\nPass")
##        break
##    elif pmark==100:
##        print("\nProgress (Module Trailer)")
##        break
##    elif fmark>=80:
##        print("\nExclude")
##        break
##    elif fmark<=80:
##        print("\nDo not Progress – Module Retriever")
##        break
##    break
##break
##
