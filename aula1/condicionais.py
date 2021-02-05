numero = 5
fracao = 6.1
online = True
texto = "Ricardo"


if numero == 5:
    print("Hello 5")
elif numero == 4 and online:
    print("Hello 4")
else:
    print("Final")

"""                                           O bloco abaixo pode ser substituido pela linha 22
if online:
    msg = "Hello, I'm online!"
else:
    msg = "I'm offline :("
"""


print("Hello, i'm online" if online else "Im Offline :/")