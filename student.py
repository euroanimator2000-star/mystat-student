import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50   
        self.progress = 50   
        self.money = 100     
        self.alive = True

    def study(self):
        print("Я сажусь за учебу...")
        self.progress += 5
        self.gladness -= 3

    def sleep(self):
        print("Я иду спать...")
        self.gladness += 3

    def chill(self):
        print("Я отдыхаю с друзьями...")
        self.gladness += 5
        self.progress -= 3
        self.money -= 15 

    def work(self):
        print("Я пошел на подработку...")
        self.money += 50
        self.gladness -= 5
        self.progress -= 2

    def live(self, day):
        print("--- День " + str(day) + " ---")
        
        if self.money < 20:
            self.work()
        elif self.progress < 20:
            self.study()
        elif self.gladness < 20:
            self.chill()
        else:
            choice = random.randint(1, 4)
            if choice == 1:
                self.study()
            elif choice == 2:
                self.sleep()
            elif choice == 3:
                self.chill()
            elif choice == 4:
                self.work()

        # Проверка, живой ли еще студент
        if self.progress <= 0:
            print("Меня отчислили за неуспеваемость!")
            self.alive = False
        elif self.gladness <= 0:
            print("Я сошел с ума от депрессии...")
            self.alive = False
        elif self.money < 0:
            print("Я стал банкротом!")
            self.alive = False

        print("Счастье:", self.gladness, "| Учеба:", self.progress, "| Деньги:", self.money)
        print()

my_student = Student("Юсуф")

for day in range(1, 366):
    if my_student.alive == False:
        break
    my_student.live(day)

if my_student.alive:
    print("Ура! Студент к сожалению прожил весь год и не пропал!")
