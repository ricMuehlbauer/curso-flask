a = 0
b = 10

# EAFP - Easy to access forgiveness before permission

try:
    print(b / a)
except AttributeError as e:
    print("Nao posso transformar n em maiusculo", str(e))
except ZeroDivisionError as e:
    print("Deu erro, tenta de novo", str(e))