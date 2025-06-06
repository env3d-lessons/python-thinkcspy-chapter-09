import pytest
from main import *

def test_print_names(monkeypatch):
    printed = []
    monkeypatch.setattr("builtins.print", lambda x: printed.append(x))
    print_names()
    assert 'Jack' in printed
    assert 'Ouack' in printed
    assert 'Quack' in printed

def test_print_12x12_num_lines(capsys):
    print_12x12()
    out = capsys.readouterr().out
    lengths = [len(l) for l in out.split('\n') if len(l) > 0]
    assert len(lengths) == 12, "Need to output the correct number of lines"

def test_print_12x12_lengths(capsys):
    print_12x12()
    out = capsys.readouterr().out
    lengths = [len(l) for l in out.split('\n') if len(l) > 0]
    assert max(lengths) == min(lengths), "Every line needs to be the same length"

def test_print_12x12_spacing(monkeypatch):
    calls = []
    def fake_print(*args, **kwargs):
        calls.append((args, kwargs))
    monkeypatch.setattr("builtins.print", fake_print)
    print_12x12()
    params = [(c[0][0], c[1].get('end', '\n')) for c in calls if len(str(c[0][0])) > 0]
    num_spaces = len(str(params[0][0])) + len(params[0][1])
    for p in params:
        assert len(str(p[0])) + len(p[1]) == num_spaces

def test_reverse():
    assert reverse('hello') == 'olleh'
    assert reverse('abcde fg') == 'gf edcba'

def test_palindromes():
    assert palindromes('pap')
    assert not palindromes('papa')

def test_remove_dups():
    assert remove_dup('abcde abcde') == 'abcde '
    assert remove_dup('abcde ddddd') == 'abcde '
    assert remove_dup('abcde ddddd eeeee') == 'abcde '

def test_lengthOfLastWord():
    assert lengthOfLastWord("Hello World") == 5
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert lengthOfLastWord("luffy is still joyboy") == 6

def test_canConstruct():
    assert not canConstruct('a', 'b')
    assert not canConstruct('aa', 'ab')
    assert canConstruct('aa', 'aab')