def ola(nome, cpf, idade=0, maiusculo=False):
    if maiusculo:
        msg = f"Olá, {nome}".upper()
    else:
        msg = f"Olá, {nome}, {cpf}, idade: {idade}"

    print(msg)


"""
ola("Ricardo", "123123")
ola("Suelen", "123123", maiusculo=True)
ola("Marcelo", "123123", True)
"""

pessoa = ["Karla", "43214231", 15]

ola(*pessoa)

pessoa = {"nome": "Karla",
          "cpf": "43214231",
          "idade": 15}

ola(**pessoa)
