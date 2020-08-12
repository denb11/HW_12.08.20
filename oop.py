
class Student():
    name = None
    spec = None
    grades = [None]

    def setProps(self, n, s, g ):
        self.name   = n
        self.spec   = s
        self.grades = g

    def calculateAVG(self):
        sum_num = 0
        for i in self.grades:
            sum_num = sum_num + i
        avg = sum_num / len(self.grades)
        print("AVG Grade: ", avg,"\n","-"*30)

    def sayHi(self):
        print("Hello! I'm student!")
        print(self.name, self.spec, self.grades)


s1 = Student()
s2 = Student()
s1.setProps("ion", "MIT", [10.0, 9, 7.5, 9, 6])
s1.sayHi()
s1.calculateAVG()
s2.setProps("maria", "ff", [10, 9, 9, 8.5])
s2.sayHi()
s2.calculateAVG()



