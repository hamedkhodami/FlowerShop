
class UserAuth():
    def __init__(self):
        self.State=False
        self.User=None
    def StateLogin(self,request):
        if request.user.is_authenticated:
            self.User=request.user
            self.State=True
            dic={"State":self.State,"User":self.User}
            return dic
        else:
            self.User=None
            self.State=False
            dic={"State":self.State,"User":self.User}
            return dic