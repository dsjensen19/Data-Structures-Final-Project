class LinkedList: #First we must define the class

    class Node: #this will allow us to create a node of information.

        def __init__(self, name): #Here we set up each node. Each has the person's name, who they give to, and who they get from.

            self.name = name
            self.next = None # who they give to
            self.prev = None # who they get from

    def __init__(self): # Here we set up the node for Tommy, the organizer

        self.creator = self.LinkedList.Node("Tommy")

    def insert(self, giver, reciever): # Now we can begin to add the other members using the knowledge of who they are getting a gift from.
        new_person = LinkedList.Node(reciever) # We make the new person into a node
        new_person.prev = giver # We set up who they will be giving to
        new_person.next = self.creator #We set Tommy as the default next person to close out the loop

    def read(self, person):
    # this function looks for the name you chose
        curr = self.creator # start searching with Tommy
        while curr is not None: # repeat until you find the name
            if person == curr.name:
                print(f"{curr.name} is getting a gift from {curr.prev} and giving a gift to {curr.next}")
                curr = None
            else: # If you haven't found the name yet, move on
                curr = curr.next
