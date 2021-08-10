import math


def convert1(a):
    # convert integer to 16 bit binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return bnr


def convert(a):
    # convert integer to 8 bit binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr


def mov1(l):
    s = "00010"
    s = s + reg[l[1]][0]
    reg[l[1]][1] = int(l[2][1:])
    s = s + convert(int(l[2][1:]))
    return s


def mov2(l):
    s = "0001100000"
    s = s + reg[l[1]][0]

    s = s = s + reg[l[2]][0]
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
    reg[l[1]][1] = (reg[l[2]][1] - reg[l[3]][1])
    s = s + reg[l[3]][0]
    return s


def mul(l):
    s = "0011100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    reg[l[1]][1] = (reg[l[2]][1] * reg[l[3]][1])
    return s


def div(l):
    s = "0011100000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    reg[l[0]][1] = int(math.floor((reg[l[3]][1] / reg[l[4]][1])))
    reg[l[1]][1] = int(math.floor((reg[l[3]][1] % reg[l[4]][1])))
    return s


def left_shift(l):
    s = "01001"
    s = s + reg[l[1]][0]
    reg[l[1]][1] <<= int(l[2][1:])
    s = s + convert(int(l[2][1:]))
    return s


def right_shift(l):
    s = "01000"
    s = s + reg[l[1]][0]
    reg[l[1]][1] >>= int(l[2][1:])
    s = s + convert(int(l[2][1:]))
    return s


def xor_fnc(l):
    s = "0101000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    reg[l[1]][1] = (reg[l[2]][1] ^ reg[l[3]][1])
    return s


def or_fnc(l):
    s = "0101100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    reg[l[1]][1] = (reg[l[2]][1] | reg[l[3]][1])
    return s


def and_fnc(l):
    s = "0110000"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    reg[l[1]][1] = (reg[l[2]][1] & reg[l[3]][1])
    return s


def not_fnc(l):
    s = "0110100"
    s = s + reg[l[1]][0]
    s = s + reg[l[2]][0]
    s = s + reg[l[3]][0]
    reg[l[1]][1] = ~(reg[l[2]][1])
    return s


def load(l):
    s = "00100"
    s = s + reg[l[1]][0]
    s = s + v[l[2]][0]
    reg[l[1]][1] = int(v[l[2]][0], 2)
    return s


def store(l):
    s = "00101"
    s = s + reg[l[1]][0]
    s = s + v[l[2]][0]
    v[l[2]][1] = convert1(int(reg[l[1]][1]))
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
            if (line[0][1] not in reg or line[0][2] not in reg or line[0][3] not in reg):
                # raise error
                pass
            else:
                ret.append(add(line[0]))
        elif (line[0][0] == "sub"):
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
# while (line!=None):
#         line = input()
#         statements[var]=[line.split(" "),var]
#         var+=1
while (1):
    try:
        line = input()
        if (line != " "):
            statements[var] = [line.split(" "), var]
            var += 1
    except EOFError:
        break;
for i in statements.keys():
    if (statements[i][0][0] == 'var'):
        v[statements[i][0][1]] = 0
    elif (statements[i][0][0][-1] == ':'):
        # binary conversion
        labels[statements[i][0][0][:-1]] = convert(int(i) - len(v))
        del statements[i][0][0]
k = 0
for i in v.keys():
    # binary
    v[i] = [convert(len(statements) - len(v) + k), ""]
    k += 1
sk = 0
while (len(v) + sk in statements.keys()):
    main(statements[len(v) + sk])
    sk += 1
count = 0
for i in range(len(ret)):
    print(ret[i])
    count += 1
# for i in v.keys():
#         print(v[i][1])
#         count+=1
# while(count<=256):
#      print("0000000000000000")
#      count+=1