# Izveidot klases: kvadrātam, taisnstūrim, trijstūrim.
# Izveidot katrā klasē metodi, kura sevi nosauc
# Ārpus klasēm ciklā ar vienu metodi izdrukāt visu daudzstūru nosaukumus un malu skaitu
# Darbu iesniegt txt formātā
print("Sveicināti, VP3!")
class Figura:
  def __init__(self,vards,malas):
    self.vards = vards
    self.malas = malas
  def druka(self):
    dr=(f"Figūras nosaukums ir {self.vards}, malu skaits ir {self.malas}")
    return dr
        
figura1=Figura("kvadrats","4")
figura2=Figura("taisnsturis","4")
figura3=Figura("trijsturis","3")

saraksts=[figura1,figura2,figura3]

for i in saraksts:
    print(i.druka())