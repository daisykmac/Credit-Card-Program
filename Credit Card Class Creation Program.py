#class program
class card:
    attr1 = "Daisy"
    attr2 = "1234 5678 9012 3456"
    attr3 = "0123"
    attr4 = "123"
    attr5 = "012345"
    attr6 = "100"
    attr7 = "1000"
#Print 
    def card(self):
        print ("Name: ", self.attr1)
        print ("Card Number: ", self.attr2)
        print ("Experation Date (MMYY): ", self.attr3)
        print ("CVC: ", self.attr4)
#Driver code
Card = card()
#Access
print(Card.attr1)
Card.card()