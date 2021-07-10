"""
Reverse text without reversing individual words

Input:  We provide good material for Technical Interview preparation
 
Output: preparation Interview Technical for material good provide We

Input: hello
Output: elloh

"""

from s import Stack

def reverse(text: str, sentence: bool = False) -> str:
    stack = Stack()

    # I know, i know
    if sentence:
        word_list = text.split()

        for word in word_list:
            stack.push(word)
        
        res = ""

        while stack.get_size() > 0:
            res += stack.pop() + " "

        return res
    else:
        for ch in text:
            stack.push(ch)
        
        res = ""

        while stack.get_size() > 0:
            res += stack.pop()

        return res


print(reverse("We provide good material for Technical Interview preparation", True)) # preparation Interview Technical for material good provide We

print(reverse("sentence reversed a am I", True)) # I am a reversed sentence

print(reverse("Hello"))

print(reverse("Lorem ipsum dolor sit amet consectetur adipiscing elit..."))