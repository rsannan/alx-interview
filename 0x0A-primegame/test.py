#!/usr/bin/python3
"""
isWinner:
returns winner of the game
"""

class Player:
    """Class for players"""
    def __init__(self, loss_count=0):
        self.loss_count = loss_count
    
    def check_prime(self, num):
        flag = False

        if num == 1:
            return False
        elif num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break

            if flag:
                return False
            else:
                return True

    def check_multiples(self, array, num):
        for number in array:
            if number % num == 0:
                array.remove(number)

    def picknremove(self, array):
        for number in array:
            if self.check_prime(number):
                self.check_multiples(array, number)
                return 0
        
        return 1
    
    def increase_loss(self):
        self.loss_count = self.loss_count + 1

def isWinner(x, nums):
    """finds winner of game"""
    maria = Player()
    ben = Player()

    i = 0
    while i < x:
       new_arr = list(range(1,nums[i] + 1))
       l = 0
       while len(new_arr) >= 1:
           l += 1
           if (l % 2) != 0:
               result = maria.picknremove(new_arr)
               if result == 1:
                   maria.increase_loss()
                   break
           else:
               result = ben.picknremove(new_arr)
               if result == 1:
                   ben.increase_loss()
                   break
       i += 1
    
    if ben.loss_count < maria.loss_count:
        return "Ben"
    elif maria.loss_count < ben.loss_count:
        return "Maria"
    else:
        return None



print(isWinner(3, [4, 5, 1]))
print(isWinner(5, [2, 5, 1, 4, 3]))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
