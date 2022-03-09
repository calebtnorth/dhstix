# Imports
from sys import exit, argv as args
# Create data and pointer
data = [0]
p = 0
# Create quit function
def quit(msg:str=""):
    print(f"ERROR at pointer index {p}\n{msg}")
    exit(1)
# File loading function
def load(path:str=None):
    # Open file
    try:
        with open(path,"r") as file:
            return file.read()
    except FileNotFoundError:
        quit("No such file")
# Code interpreting function
def interpret(r_code:str, tokens:tuple=["|"," "]):
    # Filter out unrecognized tokens
    code = "".join([c if c in tokens else "" for c in r_code])
    # Check length of file
    if len(code) % 5 != 0:
        quit("Incomplete script!")
    # Split into 5s
    cmds = []
    index = 0
    while index < len(code):
        cmds.append(code[index:index+5])
        index += 5
    # Return
    return cmds
# Main function
def main():
    # Get globals
    global data, p
    # Load file
    if len(args) > 1:
        r_code = load(args[1])
    # No file path provided
    else:
        quit("Please provide a file")
    # Interpret r_code
    cmds = interpret(r_code, [" ","|"])
    # Process commands
    cmd_i, loop_i = 0, -1
    while cmd_i < len(cmds):
        # Get Command
        cmd = cmds[cmd_i]
        # Pointer right
        if cmd == "|  ||":
            p += 1
            # If pointer index surpasses list
            if p > len(data) - 1:
                data.append(0)
        # Pointer Left
        elif cmd == "||  |":
            p -= 1
            # If pointer goes below 0
            if p < 0:
                p = 0
        # Increment / decrement current value
        elif cmd == "| |||": data[p]+=1
        elif cmd == "||| |": data[p]-=1
        # IO pointer value
        elif cmd == "  |||": print(data[p])
        elif cmd == " ||||": print(chr(data[p]))
        elif cmd == "|||  ":
            try:
                data[p] = int(input(""))
            except TypeError:
                exit("Not an integer")
        # If command
        elif cmd == "|| ||":
            # If first || ||
            if loop_i == -1:
                loop_i = cmd_i
            # If || || ended
            elif data[p] == 0:
                loop_i = -1
            # Loop back
            else:
                cmd_i = loop_i
        cmd_i+=1
    # Wait for quit
    print(f"FINISHED at pointer index {p}")
    input("Press enter to kill the terminal")
# Run Main
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit("Program killed by interrupt")