class User:
    def __init__(self, id):
        self._id = id
    def __repr__(self):
        return "<user object with id {}>".format(self._id)
    def hello(self, shout:bool=True) -> 'void':
        if shout:
            print("HELLO!")
        else:
            print("hello")

user = User(3)

user.hello()