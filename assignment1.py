class MiniBank:
    main_userinfo: dict = {}

    def firstOption(self):
        option: int = int(input("Press 1 to Login: \nPress 2 to Register: "))
        if option == 1:
            self.login()
        elif option == 2:
            self.register()

    def returnId(self,transfer_username):
        userInfo_length : int = len(self.main_userinfo)
        for i in range(1, userInfo_length+1):
            if self.main_userinfo[i]["r_username"]==transfer_username:
                return i
        return None

    def menu(self,loginId):
        menu_input: int = int(input("Press 1 to Transfer :\nPress 2 to Withdraw :\nPress 3 to Update User Data :"))
        if menu_input == 1:
            transfer_username: str = input("Please enter transfer user name : ")
            transfer_id: int= self.returnId(transfer_username)
            print("\n\ntransfer id: " ,transfer_id)
            print("myId",loginId)
            amount:int =int(input("Enter amount to transfer {0}:".format(self.main_userinfo[transfer_id]['r_username'])))
            

    def login(self):
        l_username: str = input("Please enter username to login: ")
        l_passcode: int = int(input("Please enter Password: "))

        exitUser= self.exitUserName(l_username,l_passcode)
        if exitUser:
            print("\n__________Login Successful __________\n\n")
            loginId:int = self.returnId(l_username )
            self.menu(loginId)

    def exitUserName(self,l_username,l_passcode):
        user_count: int = len(self.main_userinfo)
        for i in range(1, user_count + 1):
            if self.main_userinfo[i]["r_username"] == l_username and self.main_userinfo[i]["r_passcode"] == l_passcode:
                return True
        return False


    def register(self):

        r_username:str = input("Please enter name for register: ")
        r_amount:int = int(input("Enter amount : "))
        r_userpasscode:int = int(input("please enter password: "))
        r_userpasscodecon:int = int(input("Please enter confirm password: "))

        if r_userpasscode == r_userpasscodecon:
            id: int = self.checkingUserCount()
            userInfoForm: dict = {id:{"r_username":r_username,"r_passcode":r_userpasscode,"amount":r_amount}}
            self.main_userinfo.update(userInfoForm)

            print("\n______Register Successful !_________________")
            print(self.main_userinfo)

    def checkingUserCount(self):
        count = len(self.main_userinfo)
        return count+1


if __name__=="__main__":
    miniBank :MiniBank=MiniBank()
    while True:
        miniBank.firstOption()
