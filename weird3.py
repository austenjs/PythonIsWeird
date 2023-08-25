class Foo:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return float(len(self.items))
    
obj = Foo()
try:
    for _ in range(len(obj)):
        print("The length attribute looks normal")
        break
except Exception as err:
    print(err)
    print("I successfully break the length attribute")
