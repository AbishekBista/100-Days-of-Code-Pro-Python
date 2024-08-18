class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1  = User("1", "Mario")

print(user_1.followers)

user_2 = User("2", "Luigi")

print(user_2.name)

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)