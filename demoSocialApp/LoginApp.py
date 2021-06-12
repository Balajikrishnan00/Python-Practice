from Signup import SignUp

class Login(SignUp):
    def __init__(self,**kwargs):
        super(SignUp,self).__init__(**kwargs)

    def login(self):
        if self.is_signup:
            pass

