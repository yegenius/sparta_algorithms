class Dict:
    def __init__(self):
        self.items=[None]*8
    def put(self,key,value):
        index=hash(key)%len(self.items)
        self.items[index]=value
    def get(self,key):
        return self.items[hash(key)%len(self.items)]

my_dict=Dict()
my_dict.put("test",3)
print(my_dict.get("test"))