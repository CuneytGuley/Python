class Human:
    # builtin fonksiyon  __init__ , constructor => yapıcı blok
    def __init__(self,name):
        self.name = name
        print("Bir human instance ı üretildi.")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer : {self.name}"
    def talk(self,sentence):
        name = "Ercan"
        print(f"{sentence} {self.name}")  #self.name Halit yazdırı, sadece name Ercan yazdırı
    def walk(self):
        print(f"{self.name} is walking...")

# self parametresi c# ve java daki this karşılığı. self yerine humanobj gibi başka bir parametre de kullanılabilir, 
# ama community  self kullanır. Bir class içinde fonksiyon tanımladığımızda, bunu muhakkak kullanmalıyız.