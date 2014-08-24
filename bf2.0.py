import sys

def main():
    tape = [0]*30000
    pot = 0
    counter = 0
    command = ""
    
    character = ""
    program = str(input("Please enter your code: "))
    braces = makemap(program)

    
    while counter < len(program):
        command = program[counter]
        if command == "+": tape[pot] += 1
        elif command == "-" and tape[pot] != 0: tape[pot] -= 1
        elif command == ">" and pot < 30000: pot += 1
        elif command == "<" and pot > 0: pot -= 1
        elif command == "[" and tape[pot] == 0: counter = braces[counter]
        elif command == "]" and tape[pot] != 0: counter = braces[counter]
        elif command == ".": print(chr(tape[pot]))
        elif command == ",": tape[pot] = ord(sys.stdin.read(1))
        else: pass

        counter += 1

def makemap(prog):
    temporaily_map, real_map = [], {}
    
    for number,search in enumerate(prog):
        if search == "[": temporaily_map.append(number)
        if search == "]":
            startpos = temporaily_map.pop()
            real_map[startpos] = number
            real_map[number] = startpos        
    return real_map
                
if __name__ == "__main__":
    main()
