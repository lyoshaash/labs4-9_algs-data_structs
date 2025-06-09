def generate_psp(n, s='', open=0, close=0):
    if len(s) == 2 * n:
        print(s)
        return
    if open < n:
        generate_psp(n, s + '(', open + 1, close)
    if close < open:
        generate_psp(n, s + ')', open, close + 1)

n = int(input())
generate_psp(n)
