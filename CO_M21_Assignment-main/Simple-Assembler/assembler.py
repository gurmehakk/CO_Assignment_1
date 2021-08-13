import math


def error():
    b = False
    for i in statements.keys():
        b = error1(statements[i][0])
        if (b == False):
            continue
        else:
            return b
    return b


def error1(l):
    if (l[0] != "var" and l[0] not in op.keys()):
        print("Typo in instruction")

        return True
    elif ((l[0] == 'jmp' or l[0] == 'jlt' or l[0] == 'jgt' or l[0] == 'je') and (
            l[1] in v.keys() or l[1] in reg.keys())):
        print("Illegal memory address")
        return True
    elif (l[0] == "add" or l[0] == "sub" or l[0] == "mul" or l[0] == "xor" or l[0] == "or" or l[0] == "and"):
        if (len(l) != 4):
            print("Wrong syntax used for instructions")
            return True
        elif (l[1] not in reg.keys() or l[2] not in reg.keys() or l[3] not in reg.keys()):
            print("Typos in register name")
            return True
    elif(l[0]=="mov"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions")
            return True
        elif (l[1] not in reg.keys()):
            print("Typos in register name")
            return True
        elif(l[2][0:1]=="R"):
            if(l[2] not in reg.keys()):
                print("Invalid register name")
                return True
        elif(l[2][0:1]=="$"):
            if (int(l[2][1:],10)<0 and int(l[2][1:],10)>255):
                print("Invalid immidiete")
                return True
        else:
            print("Wrong move instruction type")
            return True
    # b
    elif ( l[0] == "rs" or l[0] == "ls"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions")
            return True
        elif (l[1] not in reg.keys()):
            print("Typos in register name")
            return True
        elif (l[2] not in reg.keys() and l[2] not in v.keys()):
            print("invalid register/variable name/immidiete")
    elif (l[0] == "div" or l[0] == "not" or l[0] == "cmp"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions")
            return True
        elif (l[2] not in reg.keys()):
            print("Typos in register name")
            return True
        elif (l[1] not in reg.keys()):
            print("Typo in register name")
    # d
    elif (l[0] == "ld" or l[0] == "st"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions")
            return True
        if (l[1] not in reg.keys()):
            print("Typo in register name")
            return True
        if l[2] not in v.keys():
            print("Typo in memory address")
            return True
    # e
    elif (l[0] == "jmp" or l[0] == "jlt" or l[0] == "jgt" or l[0] == "je"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions")
            return True
        if l[2] not in v.keys():
            print("Typo in memory address")
            return True
    # f
    elif (l[0] == "hlt"):
        if (len(l) != 1):
            print("Wrong syntax used for instructions")
            return True


def convert1(a):
    # convert integer to 16 bit binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return bnr


def convert(a):
    # convert integer to 8 bit binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr


def mov1(l):
    s = "00010"
    s = s + reg[l[1]][0]
    s = s + convert(int(l[2][1:]))
    return s


def mov2(l):
    s = "0001100000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def add(l):
    s = "0000000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def sub(l):
    s = "0000100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def mul(l):
    s = "0011000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def div(l):
    s = "0011100000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def left_shift(l):
    s = "01001"
    s = s + reg[l[1]][0]
    s = s + convert(int(l[2][1:]))
    return s


def right_shift(l):
    s = "01000"
    s = s + reg[l[1]][0]
    s = s + convert(int(l[2][1:]))
    return s


def xor_fnc(l):
    s = "0101000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def or_fnc(l):
    s = "0101100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def and_fnc(l):
    s = "0110000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    return s


def not_fnc(l):
    s = "0110100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def load(l):
    s = "00100"
    s = s + reg[l[1]][0]
    s = s + v[l[2]][0]
    return s


def store(l):
    s = "00101"
    s = s + reg[l[1]][0]
    s = s + v[l[2]][0]
    return s


def compare(l):
    s = "0111000000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    return s


def jump_uncond(l):
    s = "01111000"
    s = s + labels[l[1]]
    return s


def jump_if_less(l):
    s = "10000000"
    s = s + labels[l[1]]
    return s


def jump_if_greater(l):
    s = "10001000"
    s = s + labels[l[1]]
    return s


def jump_if_equal(l):
    s = "10010000"
    s = s + labels[l[1]]
    return s


def halt(l):
    return "1001100000000000"


def main(line):
    if (line[0][0] in op.keys()):
        if (line[0][0] == 'mov'):
            if (line[0][2] in reg.keys()):
                ret.append(mov2(line[0]))
            else:
                ret.append(mov1(line[0]))
        elif (line[0][0] == "add"):
            if (len(line[0]) != 4):
                print("Wrong syntax used for instructions")
                # raise error
                pass
            if (line[0][1] not in reg or line[0][2] not in reg or line[0][3] not in reg):
                # raise error
                pass
            else:
                ret.append(add(line[0]))
        elif (line[0][0] == "sub"):
            if (len(line[0]) != 4):
                print("Wrong syntax used for instructions")
            if (line[0][1] not in reg or line[0][2] not in reg or line[0][3] not in reg):
                # raise error
                pass

            else:
                ret.append(sub(line[0]))
        elif (line[0][0] == "mul"):
            if (line[0][1] not in reg or line[0][2] not in reg or line[0][3] not in reg):
                # raise error
                pass
            else:
                ret.append(mul(line[0]))
        elif (line[0][0] == "div"):
            if (line[0][1] not in reg or line[0][2] not in reg):
                # raise error
                pass
            else:
                ret.append(div(line[0]))
        elif (line[0][0] == "ld"):
            if (line[0][1] not in reg or line[0][2] not in v):
                # raise error
                pass
            else:
                ret.append(load(line[0]))
        elif (line[0][0] == "st"):
            if (line[0][1] not in reg or line[0][2] not in v):
                # raise error
                pass
            else:
                ret.append(store(line[0]))
        elif (line[0][0] == "rs"):
            if (line[0][1] not in reg or int(line[0][2][1:]) < 0 or int(line[0][2][1:]) > 255):
                # raise error
                pass
            else:
                ret.append(right_shift(line[0]))
        elif (line[0][0] == "ls"):
            if (line[0][1] not in reg or int(line[0][2][1:]) < 0 or int(line[0][2][1:]) > 255):
                # raise error
                pass
            else:
                ret.append(left_shift(line[0]))
        elif (line[0][0] == "or"):
            if (line[0][1] not in reg or line[0][2] not in reg or line[0][3] not in reg):
                # raise error
                pass
            else:
                ret.append(or_fnc(line[0]))
        elif (line[0][0] == "xor"):
            if (line[0][1] not in reg or line[0][2] not in reg or line[0][3] not in reg):
                # raise error
                pass
            else:
                ret.append(xor_fnc(line[0]))
        elif (line[0][0] == "and"):
            if (line[0][1] not in reg or line[0][2] not in reg or line[0][3] not in reg):
                # raise error
                pass
            else:
                ret.append(and_fnc(line[0]))
        elif (line[0][0] == "not"):
            if (line[0][1] not in reg or line[0][2] not in reg):
                # raise error
                pass
            else:
                ret.append(not_fnc(line[0]))
        elif (line[0][0] == "cmp"):
            if (line[0][1] not in reg or line[0][2] not in reg):
                # raise error
                pass
            else:
                ret.append(compare(line[0]))
        elif (line[0][0] == "jmp"):
            if (line[0][1] not in labels):
                # raise error
                pass
            else:
                ret.append(jump_uncond(line[0]))
        elif (line[0][0] == "jlt"):
            if (line[0][1] not in labels):
                # raise error
                pass
            else:
                ret.append(jump_if_less(line[0]))
        elif (line[0][0] == "jgt"):
            if (line[0][1] not in labels):
                # raise error
                pass
            else:
                ret.append(jump_if_greater(line[0]))
        elif (line[0][0] == "je"):
            if (line[0][1] not in labels):
                # raise error
                pass
            else:
                ret.append(jump_if_equal(line[0]))
        elif (line[0][0] == "hlt"):
            ret.append(halt(line[0]))
    else:
        # raise error
        pass


ret = []
statements = {}
op = {"add": '00000', "sub": '00000',
      "mov": '0001100000', "ld": '00000', "st": '00000', "mul": '00000',
      "div": '00000', "rs": '00000', "ls": '00000', "xor": '00000',
      "or": '00000', "and": '00000', "not": '00000', "cmp": '00000',
      "jmp": '00000', "jlt": '00000', "jgt": '00000', "je": '00000',
      "hlt": '00000'}
v = {}
reg = {'R0': ['000', 0], 'R1': ['001', 0], 'R2': ['010', 0], 'R3': ['011', 0], 'R4': ['100', 0],
       'R5': ['101', 0], 'R6': ['110', 0], 'FLAGS': ['111', 0]}
var = 0
labels = {}
line = ""
# while (line!="hlt"):
#         line = input()
#         if (line.split(" ")[0]!= "hlt" and (len(line.split(" ")) == 1)) :
#             print("Invalid Instruction")
#             exit(0)
#         statements[var]=[line.split(" "),var]
#         var+=1
while (1):
    try:
        line = input()
        if (line != ""):
            if (line.split(" ")[0] != "hlt" and (len(line.split(" ")) == 1)):
                print("Invalid Instruction")
                exit(0)
            statements[var] = [line.split(" "), var]
            var += 1
    except EOFError:
        break
for i in statements.keys():
    if (statements[i][0][0] == 'var'):
        if (len(statements[i][0]) == 1):
            print("Invalid Instruction")
            exit(0)
        v[statements[i][0][1]] = 0
    elif (statements[i][0][0][-1:] == ':'):
        if (statements[i][0][0][:-1] in labels):
            print("Two labels with same name -> Invalid Instruction")
            exit(0)
        # binary conversion
        labels[statements[i][0][0][:-1]] = convert(int(i) - len(v))
        del statements[i][0][0]

k = 0
for i in v.keys():
    # binary
    v[i] = [convert(len(statements) - len(v) + k), ""]
    k += 1
for i in statements.keys():
    if (statements[i][0][0] == "hlt" and statements[i][1] != len(statements) - 1):
        print("More than one hlt statement")
        exit(0)
if (error()):
    exit()
else:
    sk = 0
    while (len(v) + sk in statements.keys()):
        main(statements[len(v) + sk])
        sk += 1
    for i in range(len(ret)):
        print(ret[i])

