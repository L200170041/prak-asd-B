class stack():
    def __init__(self): #membuat stack kosong
        self.item = []
    def empty(self): #mengembalikan nilai boolean yg menunjukkan apakah
                     #stack itu kosong
        return len(self) == 0
    def __len__(self): #mengembalikan banyaknya item di stack
        return len(self.item)
    def peek(self): #mengembalikan nilai posisi atas tanpa menghapus data dan
                    #mengembalikan nilai dari item yg paling atas tanpa mnghpus
        assert not self.empty()
        return self.item[-1]
    def pop(self): #mengembalikan nilai posisi atas lalu menghapus, stack
                   #kosong tidak dapat kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stack & menambah item ke puncak
                          #stack
        self.item.append(data)


nilai = stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0 :
        nilai.pop()

print(nilai.item)
