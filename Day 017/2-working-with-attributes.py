class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.follower = 0

user_1  = User("1", "Mario")

print(user_1.follower)

user_2 = User("2", "Luigi")

print(user_2.name)