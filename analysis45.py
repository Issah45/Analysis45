import csv

class CSV:
    def __init__(self, filename):
        self.filename = filename
        self.table = []
        self.primary_row = ""
    
    def init(self):
        with open(self.filename, "r") as f:
            self.reader = csv.reader(f)
            self.primary_row = next(self.reader)
            
            for t in self.reader:
                self.table.append(t)
    
    def output(self):
        for x in self.primary_row:
            print(x, end=" ")
        print()
        for y in self.table:
            for z in y:
                print(z, end=" ")
            print()
    
    def row(self, num):
        return self.table[num-1]
    
    def column(self, num):
        columns = []
        for r in self.table:
            columns.append(r[num-1])
        return columns
            

def average(list):
    num = len(list)
    whole = 0
    for i in range(num):
        whole += list[i-1]
    whole = whole / num
    return whole