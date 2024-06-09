# class Point():
#     x = property()
#     y = property()
#
#     def __init__(self, init_x, init_y):
#         self.__x = init_x
#         self.__y = init_y
#
#     def __str__(self):
#         return f"point x({self.__x}), point y({self.__y})"
#
#     @x.getter
#     def x(self):
#         return self.__x
#     @y.getter
#     def y(self):
#         return self.__y
#
#
# p1 = Point(3, 1)
# p2 = Point(5, 5)
# print(p1.x)
# print(p2.y)
#
#
# class Line():
#     lengt = property()
#
#     def __init__(self, init_p1, init_p2):
#         self.__p1 = init_p1
#         self.__p2 = init_p2
#
#     def __str__(self):
#         return f'''line with points
#         A({self.__p1.x},{self.__p1.y})
#         B({self.__p2.x},{self.__p2.y})
#         Lengt = {self.lengt}'''
#
#     @lengt.getter
#     def lengt(self):
#         x = self.__p2.x-self.__p1.x
#         y = self.__p1.y-self.__p2.y
#         z = (x**2 + y**2) **0.5
#         return round(z, 2)
#
# line = Line(p1, p2)
# print(line)
#
#
# class Triangle():
#     p1 = property()
#     p2 = property()
#     p3 = property()
#     square = property()
#
#     def __init__(self, init_p1, init_p2, init_p3):
#         self.__p1 = init_p1
#         self.__p2 = init_p2
#         self.__p3 = init_p3
#
#     @p1.getter
#     def p1(self):
#         return self.__p1
#
#     @p2.getter
#     def p2(self):
#         return self.__p2
#
#     @p3.getter
#     def p3(self):
#         return self.__p3
#
#     def __check(self):
#         if (self.__p1.x == self.__p2.x and self.__p1.y == self.__p2.y) or \
#            (self.__p2.x == self.__p3.x and self.__p2.y == self.__p3.y) or \
#            (self.__p3.x == self.__p1.x and self.__p3.y == self.__p1.y):
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         if self.__check():
#             return "points are not unique"
#         else:
#             return f'''Triangle with points
#                 A({self.__p1.x},{self.__p1.y})
#                 B({self.__p2.x},{self.__p2.y})
#                 C({self.__p3.x},{self.__p3.y})
#                 Square = {self.square}'''
#
#     @square.getter
#     def square(self):
#         x1 = self.__p1.x
#         x2 = self.__p2.x
#         x3 = self.__p3.x
#         y1 = self.__p1.y
#         y2 = self.__p2.y
#         y3 = self.__p3.y
#         area = 0.5 * ((x1*y2 + x2*y3 + x3*y1)-(y1*x2 + y2*x3 + y3*x1))
#         area = abs(round(area,2))
#         return area
#
#
# p1 = Point(3, 1)
# p2 = Point(5, 5)
# p3 = Point(8, 3)
# tria = Triangle(p1, p2, p3)
# print(tria)

class Unit():

    name = property()
    health = property()
    hit = property()
    defence = property()

    def __init__(self, init_name = str, init_hp = int, init_hit = int, init_deff = int):
        self.__name = init_name
        self.__health = init_hp
        self.__hit = init_hit
        self.__defence = init_deff

    @name.getter
    def name(self):
        return self.__name

    @health.getter
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @defence.getter
    def defence(self):
        return self.__defence

    def hit(self, enemy):
        damage = self.__hit - enemy.defence
        enemy.health = enemy.health - damage
        print(f'''------------------
        
        ''')


unit_1 = Unit("Anya", 100, 50,20)
unit_2 = Unit()

while unit_1.health >0 and unit_2.health >0:
    unit_1.hit(unit_2)
    unit_2.hit(unit_1)


