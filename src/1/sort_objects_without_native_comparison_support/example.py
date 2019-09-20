from operator import attrgetter


class User:
    def __init__(self, user_id, user_name=None):
        self.__user_id = user_id
        self.__user_name = user_name

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_nme):
        self.__user_name = user_nme

    def __repr__(self):
        return 'User(id = {}, name = {})'.format(self.__user_id, self.__user_name)


# Example
users = [User(23, '230'), User(3, '3'), User(99, '99'), User(99, '100'), User(99, '77')]
print(users)
print('*' * 50)

# Sort it by user-id
print(sorted(users, key=attrgetter('user_id')))
print(sorted(users, key=lambda user: user.user_id))
print('*' * 50)
# Sort it by user_name
print(sorted(users, key=attrgetter('user_name')))
print(sorted(users, key=lambda user: user.user_name))
print('*' * 50)
print(sorted(users, key=attrgetter('user_id', 'user_name')))
print(sorted(users, key=lambda user: (user.user_id, user.user_name)))
