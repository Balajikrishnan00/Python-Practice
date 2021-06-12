class SignUp:
    def __init__(self, Username, Password):
        self.username = Username
        self.password = Password
        self.is_passCheck = False
        self.is_signup = False
        self.Upper = self.Lower = self.Num = self.SpecialChar = self.length = False

    def signUp(self):
        if self.is_signup:
            return f'{self.username} is already signup'
        else:

            plist = list(self.password)
            for x in plist:
                if len(plist)==8:
                    self.length=True

                if x >= 'A' or x <= 'Z':
                    self.Upper = True
                if x >= 'a' or x <= 'z':
                    self.Lower = True
                if x >= '0' or x <= '9':
                    self.Num = True
                if x in ['@', '$', '_']:
                    self.SpecialChar = True
            if self.Upper and self.Lower and self.Num and self.SpecialChar and self.length:
                self.is_passCheck = True
                self.is_signup = True
            return f'{self.username} is signup'


u1 = SignUp('balaji', 'Balaji@123')
print(u1.signUp())
print(u1.signUp())
