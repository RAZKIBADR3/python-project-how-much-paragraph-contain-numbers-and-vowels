def chercheV(p):
    v = "aoieuy"
    comp = 0
    for i in p:
        for j in v:
            if i == j:
                comp += 1
    return(comp)

def chiffre(ch):
    nums = "0123456789"
    comp = 0
    for i in ch:
        for j in nums:
            if i == j:
                comp += 1
    return(comp)

p = input("entrer une paragraph :\n")
compV = chercheV(p)
print("le nombre de voyelle est :" , compV)
compCH = chiffre(p)
print("le nombre de chiffre est :" , compCH)