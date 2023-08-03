def repeat(iterate,main_list,count,flag):
    if flag==0:
        flag_out="output_user.txt"
    else:
        flag_out="output_password.txt"
    f=open(flag_out,"w+")
    i=0
    while i < iterate:
        f.write(main_list[i%count])
        f.write("\n")
        i+=1
    f.close()
    print("Done")

main_list=[]
iterate=int(input("Enter the number of times you want to repeat: "))
switch=0
while switch==0:
    flag=int(input("Enter 0 for username list, 1 for password list: "))
    if flag not in (0, 1):
        print("Invalid input")
    else:
        valid_input = False
        while not valid_input:
            try:
                count = int(input("Enter the number of items:"))
                valid_input = True
            except ValueError:
                print("Enter a valid number")
        
        for i in range(count):
            if flag==0:
                user=input("Enter user's username : ")
                main_list.append(user)
            else:
                password=input("Enter password : ")
                main_list.append(password)

        if flag==0:
            repeat(iterate,main_list,count,flag)
        else:
            repeat(iterate,main_list,count,flag)
        switch=1
