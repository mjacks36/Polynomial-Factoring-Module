from functools import reduce
class Number:

#what makes a number factors
    other = 0
    #factorlist =[1]
    def __init__(self, number):
        self.number = number
        self.factorlist = [1]
        self.half = number // 2

        '''for num in range(2, self.half):
            if self.number % num == 0:
                #anum = self.number // num
                self.factorlist.append(num)
                #self.factorlist.append(anum)
        if self.number % self.half == 0:
            self.factorlist.append(self.half)
        self.factorlist.append(self.number)'''
        self.factorlist = sorted(reduce(list.__add__, ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))

    def displayFactors(self):
        print(self.factorlist)
        print(len(self.factorlist))

    def appendList(self, otter):
        self.factorlist.append(otter)
'''mynum = 9445128#252306#9445128
num1 = Number(mynum)
num1.displayFactors()'''
