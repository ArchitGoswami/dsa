class CusQueue: 
    # FIFO
    def __init__(self): #, store, total):
        self.store = []
    
    def push (self, element):
        # searches for and element value and pops it
        self.store.insert(len(self.store), element)
        print(element + " has been added to queue")
    
    def pop (self):
        # searches for and element value and pops it
        if (~(self.isEmpty())):
            popped = self.store.pop(0)
            print(popped,"has left the queue")
        else:
            print("The queue is empty, unable to pop")
    
    def clear (self):
        self.store=[]
        print("The queue has been cleared")
    
    def isEmpty (self):
        if (len(self.store) > 0):
            print("Queue is not empty")
        else:
            print("Queue is empty")
        return ~(len(self.store) > 0)
    
    # def Searchpop (self):
    #     # searches for and element value and pops it
    #     print("Under Construction")
        
    def fakePrint(self):
        # print("check")
        print("The queue currently looks like this:", self.store , "and the current queue length is:" , len(self.store))
    

if __name__ == "__main__":
    bankQueue = CusQueue()

    bankQueue.push("Dwight")
    bankQueue.push("Andy")
    bankQueue.push("Angela")
    bankQueue.push("Jim")
    bankQueue.fakePrint()
    
    bankQueue.pop()
    bankQueue.fakePrint()
    
    print("\n\n _____________________________________________________________________________________ \n\n")
    bankQueue.isEmpty()
    print("\n\n _____________________________________________________________________________________ \n\n")

    bankQueue.pop()
    bankQueue.fakePrint()
    bankQueue.pop()
    bankQueue.fakePrint()
    bankQueue.pop()
    bankQueue.fakePrint()
    bankQueue.pop()

    print("\n\n _____________________________________________________________________________________ \n\n")
    bankQueue.isEmpty()
    print("\n\n _____________________________________________________________________________________ \n\n")
    
    # bankQueue.fakePrint()