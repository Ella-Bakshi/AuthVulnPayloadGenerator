def repeat(iterate,main_list,count,flag):
    if flag==0:
        flag_out="output_user.txt"
    elif flag==1:
        flag_out="output_password.txt"
    else:
        flag_out="output_user_attacker_controlled.txt"
    f=open(flag_out,"w+")
    i=0
    if flag not in (0, 1):
        frequency=int(input("Enter the frequency of attacker controlled username: "))  
        f.write(main_list[i])
        f.write("\n")
        i+=1
        while i < iterate:
            if i%frequency==0:
                f.write(main_list[0])
                f.write("\n")
                i+=1
            else:
                f.write(main_list[i%count])
                f.write("\n")
                i+=1
    else:
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
    flag=int(input("Enter 0 for username list, 1 for password list, 2 for alterating username-list: "))
    if flag not in (0, 1, 2):
        print("Invalid input")
    else:
        valid_input = False
        while not valid_input:
            try:
                count = int(input("Enter the number of items:"))
                valid_input = True
            except ValueError:
                print("Enter a valid number")
        
        if flag == 2:
            attacker_user = input("Enter attacker controlled username: ")
            main_list.append(attacker_user)
            for i in range(count-1):
                user = input("Enter user's username: ")
                main_list.append(user)
        else:
            for i in range(count):
                if flag==0:
                    user=input("Enter user's username: ")
                    main_list.append(user)
                else:
                    password=input("Enter password: ")
                    main_list.append(password)

        if flag in (0, 1, 2):
            repeat(iterate, main_list, count, flag)
        switch=1
