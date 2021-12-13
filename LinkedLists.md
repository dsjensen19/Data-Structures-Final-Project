# Linked Lists

Linked lists allow people working with data structres a new way to approach the problem of memeory. Things like stacks and queues oraginize all of the data in one spot as memory. While this is easy to access, it requires you to keep your stacks and queues using dynamically allocated memory. Furthermore, for extrememly large data sets (and multiplication of large integers), using this form of data storage just won't do.

Linked lists get around these data storage problems by enabling the user to put a set of data into memory, all in different spots. Instead of grouping the list together by keeping them in the same place, linked lists group information together by linking each piece of information to the next in line, like a group of friends that draw each other's names for a secret santa activity. 

This is done by giving each piece of the linked list (called a node) information about where the next node is and where the last one was.  This way, you can follow the trail of nodes from one element to another until you find what you are looking for. Because of the way this is done, linked lists have O(n) notation, as you need to follow the list n times.

## Example

For our example, we will take a look at the secret santa gift exchange. Tommy must organize a group of 4 people (Tommy, Tony, Timmy, Terry, and Todd), with each person getting the name of another person in the group. He will organize these five people in a linked list so that he can easily find who is getting a gift for whom.

```python
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

```

In this way, we can now populate the list of gift givers with the names of each person.

## Practice

Though the code above allows Tommy to make a list of who is giving and getting gifts, it doesn't give him a way to access the information late. For your practice, add a function that takes a person's name as a parameter and tells you who they are getting a gift from and who they are giving a gift to. 

For a solution, click [here](unfinished.com)        



    


