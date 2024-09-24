"""
对不支持比较的对象排序
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
sorted_users = sorted(users, key=lambda u: u.user_id)
print(sorted_users)

sorted_users = sorted(users, key=attrgetter('user_id'))
print(sorted_users)
