class User:
    active_users = 0

    @classmethod
    def get_active_users(cls):
        return f'There are {cls.active_users} active users'
    @classmethod
    def from_string(cls, data_str):
        first_name, last_name, age = data_str.split(',')
        return cls(first_name, last_name, int(age))


    def __init__(self, first_name, last_name, age, *args):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.args = args
        User.active_users += 1

    #def __init__(self, **kwargs):
        #self.first_name = kwargs.get('first_name', None)
        #self.last_name = kwargs.get('last_name', None)
        #self.age = kwargs.get('age', None)
        #User.active_users += 1

    def __repr__(self):
        return f'User({self.first_name}, {self.last_name}, {self.age})'

    def logout(self):
        User.active_users -= 1
        return f"{self.first_name} has logged out"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


us1 = User('Nique', 'Radtke', 21, 'something', 'more', 'evenmore')
us2 = User.from_string('Nique,Radtke,21')
us3 = us1
print(User.active_users)
print(us1.full_name())
print(us2.full_name())

print(us1)
print(us3)
print(us2)
print(us1 == us3)
print(us1 == us2)


#us4 = User(first_name = 'Nique', last_name = 'Radtke', age= 21)
#print(us4.full_name())

