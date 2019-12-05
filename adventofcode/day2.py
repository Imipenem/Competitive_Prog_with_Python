def opcodeI() -> int:
    with open("/home/thelichking/Desktop/adventOfCode/Day2/Opcodes",'r' ) as file:
        lines = list(map(int,file.readline().replace("\n","").split(",")))

        lines[1],lines[2] = 12,2

        idx = 0

        while idx < len(lines):
            cur_opcode = lines[idx]
            if cur_opcode == 99: return lines[0]

            else:
                if cur_opcode == 1: lines[lines[idx+3]] = lines[lines[idx+1]] + lines[lines[idx+2]]
                elif cur_opcode == 2: lines[lines[idx+3]] = lines[lines[idx+1]] * lines[lines[idx+2]]
                idx += 4
        return lines[0]


if __name__=="__main__":
    print(opcodeI())