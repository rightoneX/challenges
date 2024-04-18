class SocksMatch:

    def __init__(self, array):
        self.array = array

    def getQtyOfPair(self):
        array = self.array
        length  = len(self.array)
        qty = 0
        for i in range(0, length):
            for j in range(i + 1, length):  
                if (array[i] == array[j]) and (array[j] != 'x'):
                    array[i] = array[j] = 'x'
                    qty += 1
        return qty
        

test_1 = [1, 2, 1, 2, 1, 3, 2] # resutl 2
test_2 = [10, 20, 20, 10, 10, 30, 50, 10, 20] # resutl 3

result = SocksMatch(test_2)
print(result.getQtyOfPair())