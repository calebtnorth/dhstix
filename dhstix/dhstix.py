from sys import argv,exit
data,p=[0],0
def quit(msg):
    print("ERROR > "+msg)
    exit()
def main():
    global data, p
    if len(argv)>1:
        try:
            with open(argv[1],"r") as f: r_code=f.read()
        except FileNotFoundError: quit("No such file")
    else: quit("Please provide a file")
    code, cmds, i, c = "", [], 0, argv[2] if len(argv)>2 else "|"
    for char in r_code:
        if char in [" ",c]: code += char
    print(code)
    while i < len(code):
        s,i=code[i:i+5],i+5 
        if len(s)==5:cmds.append(s)
    cmd_i, loop_i = 0,-1
    while cmd_i < len(cmds):
        cmd = cmds[cmd_i]
        if cmd == f"{c}  {c}{c}":
            p += 1
            if p > len(data) - 1: data.append(0)
        if cmd == f"{c}{c}  {c}":
            p -= 1
            if p < 0: p = 0
        if cmd == f"{c} {c}{c}{c}": data[p] += 1
        if cmd == f"{c}{c}{c} {c}": data[p] -= 1
        if cmd == f"  {c}{c}{c}": print(f"> {data[p]}")
        if cmd == f"{c}{c}{c}  ":
            try: data[p] = int(input("< "))
            except ValueError:quit("Not a number")
        if cmd == f"{c}{c} {c}{c}":
            if loop_i == -1: loop_i = cmd_i
            elif data[p] == 0: loop_i = -1
            else: cmd_i = loop_i
        cmd_i+=1
if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: quit("Program killed by interrupt")