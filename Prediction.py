print('''---------------HEART DISEASE PREDICTION---------------''')

print('''~~~~~~~~~~~Know Your Disease,Save Your Life~~~~~~~~~~~''')
while True:
    
    print("a)__Admin Login__")
    print("b)__User Login___")
    print("c)__Exit_____")
    print("____________________________________________________________")
    print()
    a = input("Enter Your Choice--> ")
    print()


    import pandas as pd

        
    if a == 'a':
        while True:
                
            
            print("WELCOME ADMIN")
            print("----------------------")
            print('''
    Press 1 - View Training Data
    Press 2 - View User
    Press 3 - View Feedback
    Press 4 - Logout
    ___________________________________________________________''')
            print()
            


            ch = int(input("Enter Your Choice  "))

            

            if ch == 1:
                print("_________User Information_______")
                print()
                print(df1)
                print()

           

            elif ch == 2:
                print("_________Training Dataset_______")
                print()

            elif ch == 3:
                print("_________Feedback_______")
                print()
                
            elif ch == 4:
                print('''
            ------------------------------------
            -           -THANK YOU-           -
            ------------------------------------
            ''')
                print()
                break
                
            else:
                print("INVALID CHOICE!")
                print()


            input('Press Enter key to continue....')
            

                
                
            
    elif a == 'b':
        while True:
            
            print("---------WELCOME USER-------------")
            print()
            print('''MENU
        Press 1 - Heart Analysis 
        Press 2 - View Doctor
        Press 3 - Give Feedback
        Press 4 - Exit
        ___________________________________________________________''')
            print()
            
            ch1 = int(input("Enter Your Choice  "))
            if ch1 == 1:
                print('''For moving further, You should fill the following details:''')
                print()
            #user details over here
                n = input("Name:")
                c = input("City:")
                m = input("Mobile No.:")
                e = input("Email Id:")
                a = int(input("Age:"))
                print()
                print("Thank You for the Details!")
                print()
                print('''Now its time to check your heart''')
                
                du = {'Name':[n],'City':[c],'Mobile No':[m],'Email Id'
                         :[e],'Age':[a]}
        ##        dfu1 = pd.DataFrame(du)
        ##        dfu2 = dfu1.to_csv('User_Info.csv',sep = ',')
        ##        dfu3 = pd.read_csv('User_Info.csv')
        ##        print(dfu3)
            
                while True:
                    print('''__________________________________________________''')
                    print('''Chest Pain type (cp):
        0:No Chest pain
        1:Chest pain''')
                    print()
                    cp = input("Enter Chest Pain Type ~> ")
                    print()
                    if cp not in "01":
                        print("Invalid Choice")
                        print()
                        continue
                    else:
                        
                        print("____________________________________________")
                        break
                    
                while True:
                    
                    
                    print('''fasting blood sugar(fbs):
        0 <120mg/dl
        1 >=120mg/dl''')
                    print()
                    fbs = input("Fasting Blood Sugar ~> ")
                    if fbs not in "01":
                        print("Invalid Choice")
                        print()
                        continue
                    else:
                        print("____________________________________________")
                        break
                while True:
                    print('''Exercise induced angina[Chest pain while exercising](exang):
        0 = No
        1 = Yes''')
                    print()
                    exang = input("exercise-induced angina(0 or 1) ~> ")
                    if exang not in "01":
                            print("Invalid Choice")
                            print()
                            continue
                    else:
                        print("____________________________________________")
                        break
                    
                while True:
                    
                    print('''number of major vessels(ca):
        0:No blood vessel coloured by fluoroscopy
        1:Number of major blood vessels coloured by fluoroscopy ranges from 0–3.
        ''')
                    print()
                    ca = input("Number of major vessels (0 or 1) ~> ")
                    if ca not in "01":
                        print("Invalid Choice")
                        print()
                        continue
                    else:
                        print("____________________________________________")
                        break
                
                while True:
                    print('''Whether You smoke or not:
        0:No smoking
        1:Smoking''')
                    print()
                    smoke = input("Enter value(0 or 1) ~> ")
                    if smoke not in "01":
                        print("Invalid Choice")
                        print()
                        continue
                    else:
                        print("____________________________________________")
                        break
                    
                while True:
                    print('''Chol—serum cholesterol:
        shows the amount of triglycerides present.
        Triglycerides are another lipid that can be measured in the blood.
        It should be less than 170 mg/dL.

        0:<170 mg/dl
        1:>=170 mg/dl''')
                    print()
                    chol = input("Serum cholesterol ~> ")
                    if chol not in "01":
                        print("Invalid Choice")
                        print()
                        continue
                    else:
                        print("____________________________________________")
                        break
                
                while True:
                    print('''restbps—resting blood pressure (in mm Hg).

        The normal range is 120/80 (if you have a normal blood pressure reading, it is fine,
        but if it is a little higher than it should be, you should try to lower it.
        Make healthy changes to your lifestyle).

        0:range is 120/80
        1:range below 80 or above 120''')
                    print()
                    restbps= input("Resting Blood Pressure ~> ")
                    if chol not in "01":
                        print("Invalid Choice")
                        print()
                        continue
                    else:
                        print("____________________________________________")
                        break
                while True:
                    print('''Anxiety issues:
         0:No Anxiety
         1:Anxiety''')
                    anx = input("Enter Value(0 or 1) ~> ")
                    if anx not in "01":
                        print("Invalid Choice")
                        print()
                        continue
                    else:
                        print("____________________________________________")
                        break
##                dt = {'Chest Pain':[cp],'Fasting Blood Pressure':[fbs],'Exercise Induced Agina':[exang],
##                      'Fluoroscopy':[ca],'Smoke':[smoke],'Serum Cholestrol':[chol],'Rest BP':[restbps],
##                      'Anxiety':[anx]}
##                dft = pd.DataFrame(dt)
##                print(dft)
##                    
                lst = [int(cp),int(fbs),int(exang),int(ca),int(smoke),int(chol),int(restbps),int(anx)]
                print(lst)
                target = lst.count(1)
                print(target)
                if target >= 3 and target <= 5:
                    print("Moderate Risk")
##                    print('''Diksha yo write over here......for moderate level
##             *RESULTS:
##                      Prediction:
##                      Since your level of Heart Disease is in moderate rate so you should better think
##                      of consulting a doctor.
##        
##             *PRECAUTIONS:
##                          ''')

                elif target <= 3:
                    print("Low Risk")

                else:
                    print("High Risk")
##                     

                  
          
                    
                    
                    

                          
                
                
               

            elif ch1 == 2:
                print("_________Doctor Details_______")
                print()
                print(df)
                print()

            elif ch1 == 3:
                print("~~~~In what ways can we improve our project?~~~")
                f = input("Please provide your feedback ----:")
                print("Thank You for your feedback")
                print()
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print()

            elif ch1 == 4:
                print('''
            ------------------------------------
            -           -THANK YOU-           -
            ------------------------------------
            ''')
                break
            else:
                print("INVALID CHOICE")
                print('''Please Try Again...''')
                print()
               


    elif a == 'c':
        print('''
            ------------------------------------
            -           -THANK YOU-           -
            ------------------------------------
            ''')
        break
    else:
        print("INVALID CHOICE")
        print('''Please Try Again...''')
        print()
                
               
                
    

##        Don't smoke or use tobacco. One of the best things you can do for your heart is to stop smoking or using smokeless tobacco. ...
##Get moving: Aim for at least 30 to 60 minutes of activity daily. ...
##Eat a heart-healthy diet. ...
##Maintain a healthy weight. ...
##Get good quality sleep. ...
##Manage stress. ...
##Get regular health screenings.
##            
            




