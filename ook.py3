import os
import sys
from dataclasses import dataclass


@dataclass
class TokenSet:
      delimiter: str
      advance: str
      devance: str
      increment: str
      decrement: str
      set: str
      print: str
      jump_forward: str
      jump_back: str


def mainloop(token_set, tokens, bracket_map):
    pc = 0
    tape = Tape()

    while pc < len(tokens):
        token = tokens[pc]

        if token == token_set.advance:
            tape.advance()

        elif token == token_set.devance:
            tape.devance()

        elif token == token_set.increment:
            tape.inc()

        elif token == token_set.decrement:
            tape.dec()

        elif token == token_set.print:
            # print
            sys.stdout.write(chr(tape.get()))

        elif token == token_set.jump_forward:
            # read from stdin
            tape.set(ord(os.read(0, 1)[0]))

        elif token == token_set.jump_back and tape.get() == 0:
            # Skip forward to the matching ]
            pc = bracket_map[pc]

        elif token == token_set.jump_back and tape.get() != 0:
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

def split(token_delimiter, program):
    tokens = []
    fragments = program.split(token_delimiter)
    length = len(fragments)

    for i in range(0, length, 2):
        tokens.append(fragments[i] + " " + fragments[i+1])

    return tokens

def parse(token_set, program):
    tokens = split(token_set.delimiter, program)

    parsed = []
    bracket_map = {}
    leftstack = []

    instructions = set([
        token_set.advance,
        token_set.devance,
        token_set.increment,
        token_set.decrement,
        token_set.set,
        token_set.print,
        token_set.jump_forward,
        token_set.jump_back,
    ])
    
    pc = 0
    for token in tokens:
        if token in instructions:
            parsed.append(token)

            if token == token_set.jump_forward:
                leftstack.append(pc)
            elif token == token_set.jump_back:
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1

    return parsed, bracket_map

def run(fp):
    program_contents = ""
    token_set = TokenSet(
        delimiter=" ",
        advance="Ook. Ook?",
        devance="Ook? Ook.",
        increment="Ook. Ook.",
        decrement="Ook! Ook!",
        set="Ook. Ook!",
        print="Ook! Ook.",
        jump_forward="Ook! Ook?",
        jump_back="Ook? Ook!",
    )
    while True:
        read = os.read(fp, 4096)
        if len(read) == 0:
            break
        program_contents += read.decode()
    os.close(fp)
    tokens, bm = parse(token_set, program_contents)
    mainloop(token_set, tokens, bm)

def entry_point(argv):
    try:
        filename = argv[1]
    except IndexError:
        print("You must supply a filename")
        return 1

    run(os.open(filename, os.O_RDONLY))
    return 0

def target(*args):
    return entry_point, None

if __name__ == "__main__":
    entry_point(sys.argv)
