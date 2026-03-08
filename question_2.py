class stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")


    def removeDuplicates(stack):
        seen = set()
        result = []
        while stack:
            num = stack.pop()
            if num not in seen:
                seen.add(num)
                result.append(num)
        while result:
            stack.append(result.pop())
        return stack

    def findUnmatch(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    return ')'
        return '(' if stack else None

    def equalStacks(stack1, stack2):
        return sorted(stack1) == sorted(stack2)

    def compressStr(s):
        if not s:
            return ""
        compressed = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                compressed.append(f"{count}{s[i - 1]}")
                count = 1
        compressed.append(f"{count}{s[-1]}")
        return ''.join(compressed)

    def compressStr(s):
        if not s:
            return ""
        compressed = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                compressed.append(f"{count}{s[i - 1]}")
                count = 1
        compressed.append(f"{count}{s[-1]}")
        return ''.join(compressed)

    def reverseSentence(sentence):
        words = sentence.split()
        reversed_words = [''.join(reversed(word)) for word in words]
        return ' '.join(reversed_words)


