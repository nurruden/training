#-*-coding:utf-8-*-
#/usr/bin/env python



def verify_old_passwd(username,old_passwd):
    username = input("Please input the username which you want to modify:")
    start = 0
    with open("account",'r+',encoding='utf-8') as account:


        for line in account:
            li = line.strip()
            account_list = li.split("&")
            while start < 3:
                old_passwd = input("Please input old password:")
                if account_list[0] == username:
                    if account_list[1] == old_passwd:
                        return True
                        break
                    else:
                        start += 1
                        if 3 - start > 0:
                            print("Wrong password, please try again,you still have " + str(3-start) + "chance!")
                        else:
                            print("You have input wrong password 3 times, now force quit!")

            return False

def modify_pw(username,new_password):
    """

    :param username:
    :param new_password:
    :return:
    """
    with open("account",'r+',encoding='utf-8') as old_account,open("new_account",'w') as new_account:
        for line in old_account:
            li = line.strip()
            account_list = li.split("&")
            if account_list[0] == username:
                marker = 0
                while marker < 3:
                    first_new_password = input("Please input new password:")
                    second_new_password = input("Please input new password again:")
                    if first_new_password == second_new_password:
                        new_account.write(username+"&"+new_password+"\n")
                        new_account.write(line+"\n")
                        print("Modify password successfully!")
                        break
                    else:
                        marker += 1
                        if 3 - marker > 0:
                            print("The passwords you typed do not match, please try again, you still have " + str(3-marker)+ " chance")
                        else:
                            print("Password modification failed! quit force!")
                            quit()


def main():
    if verify_old_passwd(username=None,old_passwd=None):
        modify_pw(username="allan",new_password="qweasd")
    else:
        quit()
main()