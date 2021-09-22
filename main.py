
class Stack:
    def __init__(self):
        self.sequence_string = []


    def isEmpty(self):
        return self.sequence_string == 0

    def push(self, item):
        self.sequence_string.append(item)

    def pop(self):
        return self.sequence_string.pop()

    def peek(self):
        return self.sequence_string[len(self.sequence_string)-1]

    def size(self):
        return len(self.sequence_string)


stack = Stack()

def check_string(input_string):
    pattern_opens = set('({[')
    pattern_closed = set(')}]')
    pattern = set([('{', '}'), ('(', ')'), ('[', ']')])

    if input_string[0] in pattern_closed:
        print("Несбалансированно")
        return False

    if len(input_string) % 2 == 1:
        print("Несбалансированно")
        return False

    for bracket in input_string:
        if bracket in pattern_opens:
            stack.push(bracket)
        else:
            if stack.size() == 0:
                return False

            last_in_string = stack.pop()
            if (last_in_string, bracket) not in pattern:
                print("Несбалансированно")
                return False

    return print('Сбалансированно')


check_string('[([])((([[[]]])))]{()}')
