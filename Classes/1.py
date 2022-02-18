class getString:
    a = input()
    
b = getString()
print(b.a.upper())
class new():
    def __init__(self):
        self.inputstr = ""

    def get_String(self):
        self.inputstr = input()

    def print_String(self):
        print(self.inputstr.upper())
        
str1 = new()
str1.get_String()
str1.print_String()

