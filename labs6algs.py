def is_correct_bracket_seq(seq):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in seq:
        if char in '([{':
            stack.append(char)
        elif not stack or stack.pop() != mapping[char]:
            return False
    return not stack

print(is_correct_bracket_seq(input()))
