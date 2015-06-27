import os
import sys

def mainloop(tokens, bracket_map):
    pc = 0
    tape = Tape()

    while pc < len(tokens):
        token = tokens[pc]

        if token == "Ook. Ook?":
            tape.advance()

        elif token == "Ook? Ook.":
            tape.devance()

        elif token == "Ook. Ook.":
            tape.inc()

        elif token == "Ook! Ook!":
            tape.dec()

        elif token == "Ook! Ook.":
            # print
            os.write(1, chr(tape.get()))

        elif token == "Ook. Ook!":
            # read from stdin
            tape.set(ord(os.read(0, 1)[0]))

        elif token == "Ook! Ook?" and tape.get() == 0:
            # Skip forward to the matching ]
            pc = bracket_map[pc]

        elif token == "Ook? Ook!" and tape.get() != 0:
            # Skip back to the matching [
            pc = bracket_map[pc]

        pc += 1

class Tape(object):
    def __init__(self):
        self.thetape = [0]
        self.position = 0

    def get(self):
        return self.thetape[self.position]
    def set(self, val):
        self.thetape[self.position] = val
    def inc(self):
        self.thetape[self.position] += 1
    def dec(self):
        self.thetape[self.position] -= 1
    def advance(self):
        self.position += 1
        if len(self.thetape) <= self.position:
            self.thetape.append(0)
    def devance(self):
        self.position -= 1

def split(program):
    tokens = []
    fragments = program.split(' ')
    length = len(fragments)

    for i in range(0, length, 2):
        tokens.append(fragments[i] + " " + fragments[i+1])

    return tokens

def parse(program):
    tokens = split(program)

    parsed = []
    bracket_map = {}
    leftstack = []

    pc = 0
    for token in tokens:
        if token in ('Ook! Ook?', 'Ook? Ook!', 'Ook? Ook.', 'Ook. Ook?', 'Ook. Ook.', 'Ook! Ook!', 'Ook. Ook!', 'Ook! Ook.'):
            parsed.append(token)

            if token == 'Ook! Ook?':
                leftstack.append(pc)
            elif token == 'Ook? Ook!':
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1

    return parsed, bracket_map

def run(fp):
    program_contents = ""
    while True:
        read = os.read(fp, 4096)
        if len(read) == 0:
            break
        program_contents += read
    os.close(fp)
    tokens, bm = parse(program_contents)
    mainloop(tokens, bm)

def entry_point(argv):
    try:
        filename = argv[1]
    except IndexError:
        print "You must supply a filename"
        return 1

    run(os.open(filename, os.O_RDONLY, 0777))
    return 0

def target(*args):
    return entry_point, None

if __name__ == "__main__":
    entry_point(sys.argv)
