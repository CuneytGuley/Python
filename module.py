#import matematik as m   # sadece bu dosya içinde m takma ismi ile çağrılabilir. Takma isim verilmeyebilir.
from matematik import topla as toplamaIslemi
from day2 import sayHello,Human
# built in python modülleri
import random
from seleniumExample import webdriver
# package

# print(m.topla(10,20))
print(toplamaIslemi(10,20))

print(random.randint(0,1000))

human1 = Human("Mirza")
human1.talk("Merhaba")

# packages
# pypi.org/project/pip    paketleri buradan yüklüyoruz.

chromeDriver = webdriver.Chrome()
