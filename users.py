from orm import session, User

for user in session.query(User, User.id, User.name, User.lastname).filter(User.name=="Ivo").all():
    print(user.User)