import sys

sys.path.insert(1, ".")

from gachapy import *

def main():
    program = "2 * 3 + 1"
    rarity = 0
    ast = parse(program)
    result = interpret(ast, rarity)
    print(result)

main()