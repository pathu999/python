class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):#The __iter__() method returns the iterator object itself and is used to initialize the iterator. 
        return self
    
    def __next__(self): #The __next__() method returns the next value in the sequence represented by the iterator.

        if self.num<= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration
        
values = TopTen()

for i in values:
    print(i)