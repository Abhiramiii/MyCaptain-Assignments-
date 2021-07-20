import csv

def write_into_csv(info_list):
    with open('std_info.csv','a',newline='')as csv_file:
        writer = csv.writer(csv_file)


        if csv_file.tell() == 0:
            writer.writerow(['Name','Age','Rollno','MailID'])

        writer.writerow(info_list)

if __name__== '__main__':
    condition = True
    std_num = 1

    while(condition):
        std_info = input("Enter student information for student #{} in the following format(Name Age Rollno MailID) : ".format(std_num))
       

        #split
        std_info_list = std_info.split(' ')
        

        print('\nThe entered information is -\nName: {}\nAge: {}\nRollno: {}\nMailID: {}'.format(std_info_list[0],std_info_list[1],std_info_list[2],std_info_list[3]))

        choice_check = input('Is the entered information correct? (yes/no): ')

        if choice_check == 'yes':
            write_into_csv(std_info_list)
            
            condition_check = input('Enter yes/no if you want to continue : ')
            
            if condition_check == 'yes':
                condition = True
                std_num = std_num + 1
            elif condition_check == 'no':
                condition = False

        elif choice_check == 'no':
            print('\nPlease re-enter the details!')

        
        

        
