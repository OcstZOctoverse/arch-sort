from random import randint
from algo import arch_sort

list = []

for i in range(100):
  list.append(randint(1, 100))

print(arch_sort(list))
