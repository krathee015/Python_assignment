# Create a class to find three elements that sum to zero from a set of n real numbers

class ThreeElements:
    def __init__(self,values):
        self.values = values

    def find_elements(self):
        length = len(self.values)
        result = []
        sum = 0
        for first in range(0, length):
            for second in range(first+1, length):
                for third in range(second+1, length):
                    if self.values[first] + self.values[second] + self.values[third] == sum:
                        result.append([self.values[first],self.values[second],self.values[third]])
        print(result)

input_list = [-25,-10,-7,-3,2,4,8,10]
s = ThreeElements(input_list)
s.find_elements()