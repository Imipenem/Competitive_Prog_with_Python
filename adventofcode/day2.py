def opcodeI() -> int:
    with open("/home/thelichking/Desktop/adventOfCode/Day2/Opcodes",'r' ) as file:
        lines = list(map(int,file.readline().replace("\n","").split(",")))

        lines[1],lines[2] = 1,0

        idx = 0

        while idx < len(lines):
            cur_opcode = lines[idx]
            if cur_opcode == 99: return lines[0]

            else:
                if cur_opcode == 1: lines[lines[idx+3]] = lines[lines[idx+1]] + lines[lines[idx+2]]
                elif cur_opcode == 2: lines[lines[idx+3]] = lines[lines[idx+1]] * lines[lines[idx+2]]
                idx += 4
        return lines[0]


def opcodeII(noun, verb) -> int:
    with open("/home/thelichking/Desktop/adventOfCode/Day2/Opcodes",'r' ) as file:
        lines = list(map(int,file.readline().replace("\n","").split(",")))

        lines[1],lines[2] = noun,verb

        idx = 0

        while idx < len(lines):
            cur_opcode = lines[idx]
            if cur_opcode == 99: return lines[0]

            else:
                if cur_opcode == 1: lines[lines[idx+3]] = lines[lines[idx+1]] + lines[lines[idx+2]]
                elif cur_opcode == 2: lines[lines[idx+3]] = lines[lines[idx+1]] * lines[lines[idx+2]]
                idx += 4
        return lines[0]

def inputII() -> int:
    for i in range(100):
        for j in range(100):
            if opcodeII(j,i) == 19690720:
                return 100*j + i

if __name__=="__main__":
    print(inputII())