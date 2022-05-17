# create a class
class User:
    # pass function to leave class/function empty
    def __init__(self, user_id, username):  # initialise attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): # for methods, always have "self" as the first parameter
        user.followers += 1
        self.following += 1

user_1 = User("001", "Bruce")
# user_1.id = "001"  # .xx to add attributes
# user_1.username = "Bruce"

user_2 = User("002", "Clark")
# user_2.id = "002"
# user_2.username = "Clark"

# print(user_1.id, user_1.username, user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)