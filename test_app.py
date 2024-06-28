from FastAuth import User, Token

u = User("1", "oliver")

t = Token.create(u)

print(t)