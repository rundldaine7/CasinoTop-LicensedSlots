import random

print("Лицензионные слоты - Демо!")
spins = 5
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {5 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Крути лицензионные слоты в топ-казино и выигрывай честно!")
