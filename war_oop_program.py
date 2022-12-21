# Напишите программу по следующему описанию. Есть класс "Воин".
# От него создаются два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков.
# В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

class Warrior:
    health = 100

    @staticmethod
    def result() -> str:
        if white.health == 0:
            return 'Black won!'
        elif black.health == 0:
            return 'White won!'


white = Warrior()
black = Warrior()
while True:
    if white.health == 0 or black.health == 0:
        print(Warrior().result())
        raise StopIteration
    who_attacks = input('Who beats? ')
    if who_attacks == 'white'.lower():
        black.health -= 20
        print('White attacked')
        print(f"White got {white.health}, Black got {black.health}")
    elif who_attacks == 'black'.lower():
        white.health -= 20
        print('Black attacked')
        print(f"White got {white.health}, Black got {black.health}")
