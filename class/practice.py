# # # class Hero:
# # #     def __init__(self, money):
# # #         self.money = money
# # #
# # #     def bu_i_money(self, price):
# # #         return self.money >= price
# # #
# # #
# # # hero = Hero(300)
# # # # hero.money = 100
# # # print(hero.bu_i_money(120))
# # # print(hero.bu_i_money(400))
# # #
# #
# # class Question:
# #     def __init__(self, question, answer):
# #         self.question = question
# #         self.answer = answer
# #
# #     def check(self, answer):
# #         return answer == self.answer
# #
# #
# # question_1 = Question("My name__ Suren", "is")
# # question_2 = Question("I live Moscow", "in")
# # question_3 = Question("I coder", "am")
# #
# # quat = [question_1, question_2, question_3]
# #
# # for q in quat:
# #     print(q.question)
# #     q_ = input()
# #     if q.answer == q_:
# #         print("Верно")
#
# class Fish():
#
#     def __init__(self, name):
#         self.name = name
#
#     def swim(self):
#         print("я плаваю")
#
#     def __repr__(self):
#         return 'Рыба ' + self.name
#
#
# fish = Fish('Виолетта')
# print(fish)