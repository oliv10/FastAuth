from FastAuth import User, Token
from datetime import timedelta
from time import sleep

u = User("1", "oliver")

t = Token.create(u, timedelta(seconds=5))

print(Token.validate(t))
print(t)

sleep(5)

print(Token.validate(t))
print(t)