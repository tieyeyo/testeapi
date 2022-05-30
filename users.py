from flask.json import JSONEncoder


class USERS(object):
    new_id = 1

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.id = USERS.new_id



class usersEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, USERS):
            return obj.__dict__
        return super(
            usersEncoder, self
        ).default(obj)
