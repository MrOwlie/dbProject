import random

class Character:

    def __init__(self, stats):
        self.__cha = stats.pop()
        self.__wis = stats.pop()
        self.__int = stats.pop()
        self.__con = stats.pop()
        self.__dex = stats.pop()
        self.__str = stats.pop()


    def toString(self):
        return "Str: {}, Dex: {}, Con: {}, Int: {}, Wis: {}, Cha: {}".format(self.__str, self.__dex, self.__con, self.__int, self.__wis, self.__cha)

    @staticmethod
    def randomCharacter():
        return Character(Character.randStat());

    @staticmethod
    def randStat():
        stats = list()
        #Iterate through every stat
        for i in range(6):
            temp = list()
            #Generate 4 numbers
            for j in range(4):
                temp.insert(j, random.randint(1,6))
            temp.sort(reverse=True)
            #pick 3 highest
            temp.pop()
            #Sum and insert into stat slot
            stat = sum(temp)
            stats.insert(i, stat)
        #Return list of stats
        return stats

#Code that runs when program is executed
for i in range(10):
    print(Character.randomCharacter().toString())
