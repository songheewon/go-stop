class User(object):
    def __init__(self, user_name, id, pw, seed):
        self.user_name = user_name
        self.id = id
        self.pw = pw
        self.seed = seed

    def __repr__(self):
        return "{__class__name.__name__}(user_name='{user_name}', id='{id}', pw='{pw}', seed={seed})".format(
            __class__=self.__class__, **self.__dict__)

    def __str__(self):
        return self.user_name

    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, self.__class__):
            return self.id == other.id and self.pw == other.pw
        return not NotImplemented

    def __hash__(self):
        return hash(self.id, self.pw)

    #def createAccount(self, user_name, id, pw):
        # MongoDB를 쓸지 txt파일을 쓸지 고민해보자..!