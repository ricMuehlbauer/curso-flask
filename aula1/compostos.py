# Listas
# indices....0..........1........2
cores = ["vermelho", "verde", "azul"]
numeros = [1, 2, 3]
mistura = [1, "bruno", 4.5, True, cores, numeros, [1, 2, 3]]

cores.append("amarelo")
cores.insert(1, "branco")
cores.remove("azul")

print(cores)


# Tuplas
# ................0...........1.....2
identidade = ("Ricardo", "456789-9", 15)

print(f"Nome é {identidade[0]}")
print(f"CPF é {identidade[1]}")
print(f"Idade é {identidade[2]}")

# Desempacotamento
nome, cpf, idade = identidade

print("Desempacotamento", nome, cpf, idade)

# Dicionario (Array associativo, Hashmap, Object)
pessoa = {"nome": "Suelen", "cpf": "123421241-2", "idade": 18}

pessoa["idade"] = 19
pessoa["canal"] = "@suelenpicles"

print(f"Olá, a {pessoa['nome']} tem {pessoa['idade']} anos.")

# Iteracao (pegar um elemento de cada vez)

for cor in cores:
    print(cor.upper())

for letra in "Gabriel":
    if letra == "i":
        continue
    print(letra)

# Comprehension
print([letra for letra in "Gabriel"])

# Comprehension filtrada
print([letra for letra in "Gabriel" if letra != "i"])

for chave in pessoa:
    print(chave, ":", pessoa[chave])


for chave, valor in pessoa.items():
    print(chave, ":", valor)