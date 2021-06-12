import mysql.connector
class FaceBook:
    def __init__(self,):
        print('FACEBOOK')
        print('Connect with friends and the world around you on Facebook.')

    def Login(self,USERNAME,PASSWORD):
        self.username=USERNAME
        self.password=PASSWORD
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='root',database='demosocialapp')
            crsr=con.cursor()
            crsr.execute('select * from social_app_database')
            res=crsr.fetchall()
            for x in res:
                #print(list(x))
                if not self.username==x[3] and self.password==x[4]:
                    print('Invalid Username or Password')
                    break

                if (x[-1] == 'MALE' or x[-1] == 'male'):
                    print('Welcome to MR.', str(x[1]) + str(x[2]))
                else:
                    print('Welcome to Ms.', str(x[1]) + str(x[2]))



                #if not self.username==x[3] and self.password==x[4] and (x[-1]=='FEMALE'or x[-1]=='female'):
                 #   continue

                #else:
                #    print('Welcome to Ms.', str(x[1]) + str(x[2]))
                #    break


                #else:
                #    print('Invalid Username or Password ')


        except:
            print('something went wrong!')
        else:
            con.close()
    def ForgetPassowrd(self):
        pass
    def CreateNewAccount(self):
        pass

#user1=FaceBook()
#user1.Login('balajikrishnan00@gmail.com', 'Balaji@123',)
user2=FaceBook()
user2.Login('selvam','1234r56')
user3=FaceBook()
user3.Login('hansikamotwani@gmail.com','Hansika@123')

