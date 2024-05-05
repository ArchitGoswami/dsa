class Cusstack: 
    # FILO
    def __init__(self): #, store, total):
        self.store = []
    
    def push (self, element):
        # searches for and element value and pops it
        self.store.insert(len(self.store), element)
        print(element + " has been added to stack")
    
    def pop (self):
        # searches for and element value and pops it
        if (~(self.isEmpty())):
            popped = self.store.pop(-1)
            print(popped,"has left the stack")
        else:
            print("The stack is empty, unable to pop")
    
    def clear (self):
        self.store=[]
        print("The stack has been cleared")
    
    def isEmpty (self):
        if (len(self.store) > 0):
            print("stack is not empty")
        else:
            print("stack is empty")
        return ~(len(self.store) > 0)
    
    # def Searchpop (self):
    #     # searches for and element value and pops it
    #     print("Under Construction")
        
    def fakePrint(self):
        # print("check")
        print("The stack currently looks like this:", self.store , "and the current stack length is:" , len(self.store))
    

if __name__ == "__main__":
    bankstack = Cusstack()

    bankstack.push("Dwight")
    bankstack.push("Andy")
    bankstack.push("Angela")
    bankstack.push("Jim")
    bankstack.fakePrint()
    
    bankstack.pop()
    bankstack.fakePrint()
    
    print("\n\n _____________________________________________________________________________________ \n\n")
    bankstack.isEmpty()
    print("\n\n _____________________________________________________________________________________ \n\n")

    bankstack.pop()
    bankstack.fakePrint()
    bankstack.pop()
    bankstack.fakePrint()
    bankstack.pop()
    bankstack.fakePrint()
    bankstack.pop()

    print("\n\n _____________________________________________________________________________________ \n\n")
    bankstack.isEmpty()
    print("\n\n _____________________________________________________________________________________ \n\n")
    
    # bankstack.fakePrint()