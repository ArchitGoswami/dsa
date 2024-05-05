class CuslinkedList: 
    # FILO
    def __init__(self): #, store, total):
        self.store = {}
    
    def push (self, element):
        print(element + " has been added to linkedList")

    def push (self, element, index):
        print(element + " has been added to linkedList at index")
    
    def pop (self):
        print("The linkedList is empty, unable to pop")

    def pop (self, index):
        print("The linkedList is empty, unable to pop")

    def search(self, index)
    
    def clear (self):
        print("The linkedList has been cleared")
    
    def isEmpty (self):
        print("linkedList is not empty")
        
    def fakePrint(self):
        print("check")
    

if __name__ == "__main__":
    banklinkedList = CuslinkedList()

    banklinkedList.push("Dwight")
    banklinkedList.push("Andy")
    banklinkedList.push("Angela")
    banklinkedList.push("Jim")
    banklinkedList.fakePrint()
    
    banklinkedList.pop()
    banklinkedList.fakePrint()
    
    print("\n\n _____________________________________________________________________________________ \n\n")
    banklinkedList.isEmpty()
    print("\n\n _____________________________________________________________________________________ \n\n")

    banklinkedList.pop()
    banklinkedList.fakePrint()
    banklinkedList.pop()
    banklinkedList.fakePrint()
    banklinkedList.pop()
    banklinkedList.fakePrint()
    banklinkedList.pop()

    print("\n\n _____________________________________________________________________________________ \n\n")
    banklinkedList.isEmpty()
    print("\n\n _____________________________________________________________________________________ \n\n")
    
    # banklinkedList.fakePrint()