"""
From 9.22.1

In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.

Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?
"""

def print_names():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for p in prefixes:
        print(p + suffix)

"""
Exercise 9.22.4

Print out a neatly formatted multiplication table, up to 12 x 12.

Right now, it prints a table that is not well formatted, like this:

1 2 3 4 5 6 7 8 9 10 11 12 
2 4 6 8 10 12 14 16 18 20 22 24 
3 6 9 12 15 18 21 24 27 30 33 36 
4 8 12 16 20 24 28 32 36 40 44 48 
5 10 15 20 25 30 35 40 45 50 55 60 
6 12 18 24 30 36 42 48 54 60 66 72 
7 14 21 28 35 42 49 56 63 70 77 84 
8 16 24 32 40 48 56 64 72 80 88 96 
9 18 27 36 45 54 63 72 81 90 99 108 
10 20 30 40 50 60 70 80 90 100 110 120 
11 22 33 44 55 66 77 88 99 110 121 132 
12 24 36 48 60 72 84 96 108 120 132 144 

I want the output to be like this:

  1   2   3   4   5   6   7   8   9  10  11  12 
  2   4   6   8  10  12  14  16  18  20  22  24 
  3   6   9  12  15  18  21  24  27  30  33  36 
  4   8  12  16  20  24  28  32  36  40  44  48 
  5  10  15  20  25  30  35  40  45  50  55  60 
  6  12  18  24  30  36  42  48  54  60  66  72 
  7  14  21  28  35  42  49  56  63  70  77  84 
  8  16  24  32  40  48  56  64  72  80  88  96 
  9  18  27  36  45  54  63  72  81  90  99 108 
 10  20  30  40  50  60  70  80  90 100 110 120 
 11  22  33  44  55  66  77  88  99 110 121 132 
 12  24  36  48  60  72  84  96 108 120 132 144 
 
"""
def print_12x12():
    for i in range(1,13):
        for j in range(1,13):
            # hint: you need an IF statement here to add padding
            # depending on the number of digits to print:
            # i.e. if the number to print has 3 digits, padding = 0
            #      if the number to print has 2 digits, padding = 1
            #      if the number to print has 1 digit, padding = 2            
            print(i*j, end=' ')
        print()

"""
Write a function that reverses its string argument.

> reverse('hello world')
'dlrow olleh'

HINT: use the acculumator pattern, create a variable that holds the output
and iterate over the input string in reverse.
"""
def reverse(s):
    return ''

"""
Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).

> palindromes('pap')
True
> palindromes('papa')
False 

Also, and more complicated version: https://leetcode.com/problems/valid-palindrome/ 
"""
def palindromes(s):
    return False


"""
https://leetcode.com/problems/remove-duplicate-letters/

Write a function called remove_dups that takes a string and creates a new string by only adding those characters that are not already present. In other words, there will never be a duplicate letter added to the new string.

> remove_dup('abcde abcde')
'abcde '
> remove_dup('abcde ddddd')
'abcde '
> remove_dup('abcde ddddd eeeee')
'abcde ' 
"""
def remove_dup(s):    
    return ''

"""
From https://leetcode.com/problems/length-of-last-word/

Test cases:
> lengthOfLastWord("Hello World")
5
> lengthOfLastWord("   fly me   to   the moon  ")
4
> lengthOfLastWord("luffy is still joyboy")
6
"""
def lengthOfLastWord(sentence):
    return 0


"""
https://leetcode.com/problems/ransom-note/ 

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

def canConstruct(ransomNote, magazine):
    return False


### DO NOT EDIT BELOW THIS LINE ###
### USER INTERFACE CODE BELOW ###

import gradio as gr

def gr_print_names():
    import io, sys
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    print_names()
    sys.stdout = old_stdout
    return mystdout.getvalue()

def gr_print_12x12():
    import io, sys
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    print_12x12()
    sys.stdout = old_stdout
    return mystdout.getvalue()

def gr_reverse(s):
    return reverse(s)

def gr_palindromes(s):
    return str(palindromes(s))

def gr_remove_dup(s):
    return remove_dup(s)

def gr_lengthOfLastWord(s):
    return lengthOfLastWord(s)

def gr_canConstruct(ransomNote, magazine):
    return str(canConstruct(ransomNote, magazine))


if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("## print_names")
        gr.Interface(fn=gr_print_names, inputs=None, outputs="text", flagging_mode="never")

        gr.Markdown("## print_12x12")
        gr.Interface(fn=gr_print_12x12, inputs=None, outputs="text", flagging_mode="never")

        gr.Markdown("## reverse")
        gr.Interface(fn=gr_reverse, inputs="text", outputs="text", flagging_mode="never")

        gr.Markdown("## palindromes")
        gr.Interface(fn=gr_palindromes, inputs="text", outputs="text", flagging_mode="never")

        gr.Markdown("## remove_dup")
        gr.Interface(fn=gr_remove_dup, inputs="text", outputs="text", flagging_mode="never")

        gr.Markdown("## lengthOfLastWord")
        gr.Interface(fn=gr_lengthOfLastWord, inputs="text", outputs="number", flagging_mode="never")

        gr.Markdown("## canConstruct")
        gr.Interface(
            fn=gr_canConstruct,
            inputs=[gr.Textbox(label="ransomNote"), gr.Textbox(label="magazine")],
            outputs="text", flagging_mode="never"
        )

    demo.launch()

