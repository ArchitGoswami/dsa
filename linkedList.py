# global outString
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CuslinkedList: 
    # one points to next
    def __init__(self):
        self.head = None

    # def traverseTillEnd(self):

    #     for 
        
    #     return # retuns node location which is the key for the dict.
    
    # def traverse(self):
    #     return 0
    
    # def traverse(self, steps):
    #     return 0
    
    def pushAtFront(self, data):
        if(self.head==None):
            # just place
            self.head = node(data)
            print(data + " has been added as first element of new linkedList")
        else:
            # point head to new node and new node points to old node, rest can stay the same.
            oldHeadNode = self.head
            newNode=node(data)
            self.head=newNode
            self.head.next=oldHeadNode
            print(data + " has been added as first element of linkedList and "+ self.head.next.data +" has been moved back")


    # def pushAtBack (self, data):
    #     if(self.head==):
    #         self.store.update(data, null)
    #         print(data + " has been added to linkedList")
    #     else:
    #         traverseTillEnd
    #         # update previous node with next address

    #         self.store.update( , null) #update next node with null address as it is last node

    # def push (self, data, index):
    #     print(data + " has been added to linkedList at index")
    
    # def pop (self):
    #     print("The linkedList is empty, unable to pop")

    # def pop (self, index):
    #     print("The linkedList is empty, unable to pop")

    # def search(self, data):
    #     print("The linkedList is empty, unable to pop")
    
    # def clear (self):
    #     print("The linkedList has been cleared")
    
    # def isEmpty (self):
    #     print("linkedList is not empty")
        
    def fakePrint(self):
        global outString
        if(self.head==None):
            print("Linked List is currently empty")
        else:
            lastNode, outString=self.whilePrint() # returns string, we start from hea
            #lastNode, outString=self.recursivePrint(self.head,""") # returns string, we start from hea
            print("the linkedList currently looks like: ", outString)
        return None

    # def recursiveFunnyPrint(self,node,outString):
    #     # look at next value of given node
    #     # base statement: if next value is null then return nothing, 
    #     if (node.next == None):
    #         outString=outString,node.data
    #         print(outString)
    #         return None, outString
    #     # else recursivePrint(node), add data value to outString.
    #     else:
    #         outString=outString,node.data
    #         return self.recursivePrint(node.next,outString)

    def whilePrint(self):
        considerationNode=self.head
        outString=""
        while (considerationNode.next!=None):
            dataToPrint = considerationNode.data
            outString=outString+dataToPrint
        return outString

    

if __name__ == "__main__":
    travelLinkedList = CuslinkedList()

    travelLinkedList.pushAtFront("Dwight")
    travelLinkedList.pushAtFront("Andy")
    # travelLinkedList.pushAtFront("Angela")
    # travelLinkedList.pushAtFront("Jim")
    travelLinkedList.fakePrint()
    
    # travelLinkedList.pop()
    # travelLinkedList.fakePrint()