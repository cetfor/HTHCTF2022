_input = input
_eval = eval
_print = print

# let's make this script hacker proof!
goodbye = ['__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
for seeya in goodbye[::-1]:
    __builtins__.__dict__.pop(seeya)
goodbye = None

_print("Get a shell - The flag is in ./flag")

# some really annoying Goonies quotes that help no one
try_count = 0
quotes = [
    "I'm not afraid of the dark. I like the dark. I love the dark, but I hate nature. I hate nature.",
    "Wait a sec! Hold on!",
    "Stop! I'm just a kid!",
    "What seems to be the problem?",
    "Look, mister, I need a ride. My friends and I just had a run-in with these really disgusting people; you might have heard of them: the Fratellis. Well, we found their hideout, and could you please, please take me to the sheriff station. I can describe all three of 'em.",
    "Nim bob iyo qi verenya de Mario...",
    "Itro la vista di vitro la vista la mama.",
]

while 1:
    try:
        inp = _input() + "\n"
        if not inp:
            continue
        inp = inp.split()[0][:1900]
        _print(_eval(inp))
    except(().__class__.__bases__[0].__subclasses__()[85].__subclasses__()[0]) as e: # 85 is base exception.
        quote = try_count % 7
        try_count += 1
        if e.__str__().startswith('EOF'):
            raise e
        else:
            _print(f"({quotes[quote]})")
            if e.__str__() != "list index out of range":
                _print(e)
