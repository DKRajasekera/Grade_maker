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
    Excluded = 0
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
                        Progress = Progress + 1
                        print('Progress')
                    elif (cred_p == 100):#progress(module trailer unit
                        if (0 <= cred_d <= 20):
                            if (0 <= cred_f <= 20):
                                Trailing = Trailing + 1
                                print('Progress(module trailer)')
                    elif (40 <= cred_p <= 80):#Do not progress – module retriever unit 1
                        if (0 <= cred_d <= 80):
                            if (0 <= cred_f <= 60):
                                Retriever = Retriever + 1
                                print('Do not progress – module retriever')
                            else:# Exclude unit 1
                                if (cred_d == 0):
                                    if (cred_f == 80):
                                        Excluded = Excluded + 1
                                        print('Exclude')
                    elif (cred_p == 20):#Do not progress – module retriever unit 2
                        if (40 <= cred_d <=100):
                            if (0 <cred_f <= 60):
                                Retriever = Retriever + 1
                                print('Do not progress – module retriever')
                        else:# Exclude unit 2
                            if (0 <= cred_d <= 20):
                                if (80 <= cred_f <= 100):
                                    Excluded = Excluded + 1
                                    print('Exclude')
                    elif (cred_p == 0):#Do not progress – module retriever unit 3
                        if (60 <= cred_d <= 120):
                            if (0 <= cred_f <= 60):
                                Retriever = Retriever + 1
                                print('Do not progress – module retriever')
                        else:# Exclude unit 3
                            if (0 <= cred_d <= 40):
                                if (80 <= cred_f <= 120):
                                    Excluded = Excluded + 1
                                    print('Exclude')
                else:
                    print('Total incorrect')
            else:
                print('Out of range')
        if (option == 'q'):
            header = ['Progress', 'Trailing', 'Retriever', 'Excluded']
            print(' '.join(header))
            for x in range(max(Progress, Trailing, Retriever, Excluded)):
                print("   {0}         {1}        {2}         {3}".format(
                    '*' if x < Progress else ' ',
                    '*' if x < Trailing else ' ',
                    '*' if x < Retriever else ' ',
                    '*' if x < Excluded else ' '
                ))
            break
except ValueError:
    print('Integer required')
