# app.py
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

if __name__ == "__main__":
    result_add = addition(5, 7)
    result_sub = soustraction(10, 3)
    print(f"Le résultat de l'addition est : {result_add}")
    print(f"Le résultat de la soustraction est : {result_sub}")
