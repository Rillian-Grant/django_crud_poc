from list.models import Item
import random

for i in range(5000):
    item = Item(name="Auto Generated", txt1="blob", num1=random.randint(0, 1000), num2=random.randint(0, 1000), num3=random.randint(0, 1000))
    item.save()
