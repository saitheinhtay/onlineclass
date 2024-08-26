class MiniBank:
    file_path = 'users.txt'
    main_userinfo: dict = {}
    with open(file_path, 'r') as files:
        data = files.readlines()
        for n in data:
            id: int = len(main_userinfo) + 1
            l = n.strip().split(' ')
            keys = ['r_username', 'r_passcode', 'r_amount']
            values = l
            a = dict(zip(keys, values))
            userinfo = {
                id: a
            }
            main_userinfo.update(userinfo)
    for i in main_userinfo:
        print(f"User Id :{i}\nUser Name : {main_userinfo[i]['r_username']}\nAmount :{main_userinfo[i]['r_amount']}\n\n")

    def firstOption(self):
        option: int = int(input("Press 1 to Login: \nPress 2 to Register: "))
        if option == 1:
            self.login()
        elif option == 2:
            self.register()

    def returnId(self, transfer_username):
        userInfo_length: int = len(self.main_userinfo)
        for i in range(1, userInfo_length + 1):
            if self.main_userinfo[i]["r_username"] == transfer_username:
                return i
        return None

    def menu(self, loginId):
        menu_input: int = int(
            input(
                "Press 1 to Transfer :\nPress 2 to Withdraw :\nPress 3 to Update User Data :\nPress 4 to Detail :"
            )
        )
        if menu_input == 1:
            transfer_username: str = input("Please enter transfer user name : ")
            transfer_id: int = self.returnId(transfer_username)

            print("\n\ntransfer id: ", transfer_id)
            print("myId", loginId)
            amount: int = int(input("Enter amount to transfer :"))

            n_amount = int(self.main_userinfo[loginId]['r_amount']) - amount
            self.main_userinfo[loginId]['r_amount'] = n_amount
            print(
                f"User Name : {self.main_userinfo[loginId]['r_username']}\nAmount :{self.main_userinfo[loginId]['r_amount']}"
            )


            self.menu(loginId)
        elif menu_input == 2:
            print(
                f"User Name : {self.main_userinfo[loginId]['r_username']}\nPassword : {self.main_userinfo[loginId]['r_passcode']}\nAmount :{self.main_userinfo[loginId]['r_amount']}"
            )
            cwAmount: int = int(input("Enter withdrawal Amount : "))
            amount = str(int(self.main_userinfo[loginId]["r_amount"]) - cwAmount)
            self.main_userinfo[loginId]["r_amount"] = amount

            print(
                f"User Name : {self.main_userinfo[loginId]['r_username']}\nAmount :{self.main_userinfo[loginId]['r_amount']}"
            )
            with open(self.file_path, 'w') as files:
                for i in self.main_userinfo:
                    data = f"{self.main_userinfo[i]['r_username']} {self.main_userinfo[i]['r_passcode']} {self.main_userinfo[i]['r_amount']}"'\n'
                    files.write(data)
            self.menu(loginId)
        elif menu_input == 3:
            ud = self.main_userinfo
            print(
                f"User Name : {ud[loginId]['r_username']}\nPassword : {ud[loginId]['r_passcode']}\nAmount :{ud[loginId]['r_amount']}"
            )
            ip: int = int(
                input(
                    "Choose 1 for UserName, 2 for Password , 3 for amount : , 4 for all "
                )
            )
            if ip == 1:
                n_username: str = input("Enter New UserName : ")
                ud[loginId]["r_username"] = n_username
                with open(self.file_path, 'w') as files:
                    for i in self.main_userinfo:
                        data = f"{self.main_userinfo[i]['r_username']} {self.main_userinfo[i]['r_passcode']} {self.main_userinfo[i]['r_amount']}"'\n'
                        files.write(data)
            elif ip == 2:
                n_passcode: int = int(input("Enter New Password : "))
                n_conpasscode: int = int(input("Confirm password : "))
                if n_passcode == n_conpasscode:
                    ud[loginId]["r_passcode"] = n_passcode
                    print("\n______Change Successful !_________________\n")
                    with open(self.file_path, 'w') as files:
                        for i in self.main_userinfo:
                            data = f"{self.main_userinfo[i]['r_username']} {self.main_userinfo[i]['r_passcode']} {self.main_userinfo[i]['r_amount']}"'\n'
                            files.write(data)
            elif ip == 3:
                n_amount: int = int(input("Enter New Amount : "))
                ud[loginId]["r_amount"] = n_amount
                with open(self.file_path, 'w') as files:
                    for i in self.main_userinfo:
                        data = f"{self.main_userinfo[i]['r_username']} {self.main_userinfo[i]['r_passcode']} {self.main_userinfo[i]['r_amount']}"'\n'
                        files.write(data)
            elif ip == 4:
                n_username: str = input("Enter New UserName : ")
                ud[loginId]["r_username"] = n_username
                n_passcode: int = int(input("Enter New Password : "))
                n_conpasscode: int = int(input("Confirm password : "))

                n_amount: int = int(input("Enter New Amount : "))
                ud[loginId]["r_amount"] = n_amount

                if n_passcode == n_conpasscode:
                    ud[loginId]["r_passcode"] = n_passcode
                    print("\n______Change Successful !_________________\n")
                    with open(self.file_path, 'w') as files:
                        for i in self.main_userinfo:
                            data = f"{self.main_userinfo[i]['r_username']} {self.main_userinfo[i]['r_passcode']} {self.main_userinfo[i]['r_amount']}"'\n'
                            files.write(data)

            print(
                f"User Name : {ud[loginId]['r_username']}\nPassword : {ud[loginId]['r_passcode']}\nAmount :{ud[loginId]['r_amount']}"
            )
            self.menu(loginId)
        elif menu_input == 4:
            ud = self.main_userinfo
            print(
                f"User Name : {ud[loginId]['r_username']}\nPassword : {ud[loginId]['r_passcode']}\nAmount :{ud[loginId]['r_amount']}"
            )
            self.menu(loginId)
    def login(self):
        l_username: str = input("Please enter username to login: ")
        l_passcode: int = int(input("Please enter Password: "))

        exitUser = self.exitUserName(l_username, l_passcode)

        if exitUser:
            print("\n__________Login Successful __________\n\n")
            loginId: int = self.returnId(l_username)
            self.menu(loginId)

    def exitUserName(self, l_username, l_passcode):
        user_count: int = len(self.main_userinfo)
        for i in range(1, user_count + 1):
            if (
                self.main_userinfo[i]["r_username"] == l_username
                and int(self.main_userinfo[i]["r_passcode"]) == l_passcode
                ):
                    return True
        return False



    def userList(self):
        user_list: int = len(self.main_userinfo)
        for i in range(1, user_list + 1):
            print(
                f"User Id : {i}\nUser Name : {self.main_userinfo[i]['r_username']}\nPassword : {self.main_userinfo[i]['r_passcode']}\nAmount :{self.main_userinfo[i]['amount']}\n\n"
            )


    def register(self):

        r_username:str = input("Please enter name for register: ")
        with open(self.file_path, 'r') as files:
            data = files.readlines()
            try:
                for n in data:
                    l = n.strip().split(' ')
                    if l[0] == r_username:
                        raise ValueError("User name already exists!\n\n")

                r_amount: int = int(input("Enter amount : "))
                r_userpasscode: int = int(input("please enter password: "))
                r_userpasscodecon: int = int(input("Please enter confirm password: "))

                if r_userpasscode == r_userpasscodecon:
                    setData = r_username + ' ' + str(r_userpasscode) + ' ' + str(r_amount) + '\n'
                    # Write dictionary to text file
                with open(self.file_path, 'a') as file:
                    file.write(setData)

                print("\n______Register Successful !_________________\n\n")

            except ValueError as e:
                print(e)


            # with open(self.file_path, 'r') as files:
            #       data = files.readlines()
            #       for n in data:
            #           id: int = len(self.main_userinfo) + 1
            #
            #           l = n.strip().split(' ')
            #           keys = ['r_username', 'r_passcode', 'r_amount']
            #           values = l
            #           a = dict(zip(keys, values))
            #           userinfo = {
            #               id: a
            #           }
            #           self.main_userinfo.update(userinfo)
    def checkingUserCount(self):
        count = len(self.main_userinfo)
        return count+1


if __name__=="__main__":
    miniBank :MiniBank=MiniBank()
    while True:
        miniBank.firstOption()
