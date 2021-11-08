map = {
    "Ook! Ook.": ".",
    "Ook. Ook?": ">",
    "Ook? Ook.": "<",
    "Ook. Ook.": "+",
    "Ook! Ook!": "-",
    "Ook. Ook!": ",",
    "Ook! Ook?": "[",
    "Ook? Ook!": "]",
    }

def convert(program):
    result = [map.get(char) for char in program if map.get(char)]
    return ' '.join(result)

def run(input):
    program = input.read()
    codes = convert(program)
    print codes

if __name__ == '__main__':
    import sys
    run(open(sys.argv[1], 'r'))
