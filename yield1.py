# # Ör1 : return ile değer döndürme
# meyveler = ["elma","muz","dut"]

# def xxx (aa):
#     for b in aa:
#         return b

# sonuc = xxx(meyveler)
# print(sonuc)

# sonuc = xxx(meyveler)
# print(sonuc)


# # Ör2 : return yerine yield ile değer üretme
# meyveler = ["elma","muz","dut"]

# def xxx (aa):
#     for b in aa:
#         yield b

# sonuc = xxx(meyveler)
# print(sonuc)

# print(next(sonuc))
# print(next(sonuc))
# print(sonuc[1])

# Ör3: return
# def deneme():
#     return "merhaba"
# print(deneme()*3)

# # Ör4: yield
def deneme():
    yield "merhaba"
    yield "nasılsın"

liste = deneme()
print(next(liste))
print(next(liste))




