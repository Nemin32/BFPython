class BFInterpreter:

        #global tape
        #global pot
        def __init__(self,bf):
                self.bf = bf
                self.tape = [0]*30000
                self.pot = 0 #Position On Tape - POT
                self.commands = {}
                self.should_iterate = True

        def toRight(self):
                if self.pot != 30000:
                        self.pot = pot+1

        def toLeft(self):
                if self.pot > 0:
                        self.pot = pot-1

        def increase(self):
                self.tape[self.pot] = self.tape[self.pot]+1

        def decrease(self):
                self.tape[self.pot] = self.tape[self.pot]-1

        def printout(self):
                print(str(self.tape[self.pot]))

        def inputchar(self):
                while True:
                        character = input("Enter character:")
                        if type(character) is str and len(character) == 1:
                                self.tape[self.pot] = ord(character)
                                break
                        else:
                                print("This is not a character!")
                                continue
        def loopBegin(self):
                end = 0
                should_iterate = False
                if self.tape[self.pot] == "0":
                        for search in self.bf:
                                if search == "]":
                                        self.pot = end + 1
                                        self.should_iterate = True
                                end += 1
                else:
                        pass

                        
        def loopEnd(self):
                print("TO-DO")
                
        
        def exec(self):
                self.commands = {
                        ">" : self.toRight,
                        "<" : self.toLeft,
                        "+" : self.increase,
                        "-" : self.decrease,
                        "." : self.printout,
                        "," : self.inputchar,
                        "[" : self.loopBegin,
                        "]" : self.loopEnd
                        }
                for c in self.bf:
                        if self.should_iterate == True:
                                #print("Iterate")
                                self.commands[c]()

##                for m in range(1,10):
##                        self.pot = m
##                        print(str(self.tape[self.pot]))                                         

