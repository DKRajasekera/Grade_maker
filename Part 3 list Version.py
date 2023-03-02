# I declare that my work contains no examples of misconduct, such as plagiarism, or 
# collusion. 
# Student ID: 20210327
 
# Date:28/11/2021 
try:
    total = 0
    total_2 = 0
    Progress = 0
    Trailing = 0
    Retriever = 0
    Exclude = 0
    Progress_L = []
    Trailing_L = []
    Retriever_L = []
    Exclude_L = []
    while True:
        option = input('Enter ‘y’ for yes or ‘q’ to quit and view results: ')
        if (option == 'y'):
            range_1 = range(0,121,20)
            cred_p = int(input('Please enter your credits at pass: '))
            cred_d = int(input('Please enter your credits at defer: '))
            cred_f = int(input('Please enter your credits at fail: '))
            if cred_p and cred_d or cred_f in range_1:
                total = cred_p + cred_d + cred_f
                if (total == 120):#check the total is correct or not
                    if (cred_p == 120 and cred_d == 0 and cred_f == 0):#progress unit
                        Progress +=1
                        Progress1 = []
                        Progress1.append(cred_p)
                        Progress1.append(cred_d)
                        Progress1.append(cred_f)
                        Progress_L.append(Progress1)
                        print('Progress')
                    elif (cred_p == 100):#progress(module trailer unit
                        if (0 <= cred_d <= 20):
                            if (0 <= cred_f <= 20):
                                Trailing +=1
                                Trailing1 = []
                                Trailing1.append(cred_p)
                                Trailing1.append(cred_d)
                                Trailing1.append(cred_f)
                                Trailing_L.append(Trailing1)
                                print('Progress(module trailer)')
                    elif (40 <= cred_p <= 80):#Do not progress – module retriever unit 1
                        if (0 <= cred_d <= 80):
                            if (0 <= cred_f <= 60):
                                Retriever +=1
                                Retriever1 = []
                                Retriever1.append(cred_p)
                                Retriever1.append(cred_d)
                                Retriever1.append(cred_f)
                                Retriever_L.append(Retriever1)
                                print('Do not progress – module retriever')
                            else:# Exclude unit 1
                                if (cred_d == 0):
                                    if (cred_f == 80):
                                        Exclude +=1
                                        Exclude1 = []
                                        Exclude1.append(cred_p)
                                        Exclude1.append(cred_d)
                                        Exclude1.append(cred_f)
                                        Exclude_L.append(Exclude1)
                                        print('Exclude')
                    elif (cred_p == 20):#Do not progress – module retriever unit 2
                        if (40 <= cred_d <=100):
                            if (0 <cred_f <= 60):
                                Retriever +=1
                                Retriever1 = []
                                Retriever1.append(cred_p)
                                Retriever1.append(cred_d)
                                Retriever1.append(cred_f)
                                Retriever_L.append(Retriever1)
                                print('Do not progress – module retriever')
                        else:# Exclude unit 2
                            if (0 <= cred_d <= 20):
                                if (80 <= cred_f <= 100):
                                    Exclude +=1
                                    Exclude1 = []
                                    Exclude1.append(cred_p)
                                    Exclude1.append(cred_d)
                                    Exclude1.append(cred_f)
                                    Exclude_L.append(Exclude1)
                                    print('Exclude')
                    elif (cred_p == 0):#Do not progress – module retriever unit 3
                        if (60 <= cred_d <= 120):
                            if (0 <= cred_f <= 60):
                                Retriever +=1
                                Retriever1 = []
                                Retriever1.append(cred_p)
                                Retriever1.append(cred_d)
                                Retriever1.append(cred_f)
                                Retriever_L.append(Retriever1)
                                print('Do not progress – module retriever')
                        else:# Exclude unit 3
                            if (0 <= cred_d <= 40):
                                if (80 <= cred_f <= 120):
                                    Exclude +=1
                                    Exclude1 = []
                                    Exclude1.append(cred_p)
                                    Exclude1.append(cred_d)
                                    Exclude1.append(cred_f)
                                    Exclude_L.append(Exclude1)
                                    print('Exclude')
                else:
                    print('Total incorrect')
            else:
                print('Out of range')
        if (option == 'q'):
            for a in range(len(Progress_L)):
                print('Progress: ',*Progress_L[a],sep = " ")
            for b in range(len(Trailing_L)):
                print('Trailing: ',*Trailing_L[b],sep = " ")
            for c in range(len(Retriever_L)):
                print('Retriever: ',*Retriever_L[c],sep = " ")
            for d in range(len(Exclude_L)):
                print('Exclude: ',*Exclude_L[d],sep = " ")
            break
except ValueError:
    print('Integer required')
