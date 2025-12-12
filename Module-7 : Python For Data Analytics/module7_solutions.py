
# Module 7  DA: Introduction to Python 

               
from __future__ import annotations
from collections import Counter, defaultdict
from typing import List, Tuple, Dict, Any, Iterable, Optional
import math
import random




# Q1) What are the types of Applications?
Q1_ANS  = """
Common types of applications (not exhaustive):
• Desktop (native GUI apps)
• Web (server-side, client-side, full‑stack)
• Mobile (Android, iOS, cross‑platform)
• Command-line / scripting utilities
• Data / Scientific computing (EDA, ML, DL, simulation)
• Embedded / IoT
• Games & Graphics
• Enterprise & Cloud services / APIs / Microservices
• Automation / RPA / ETL
• AI/Agents & Chatbots
"""

# Q2) What is programming?
Q2_ANS  = """
Programming is the process of defining instructions a computer can execute
to automate tasks and solve problems. It includes designing algorithms,
representing data, and implementing, testing, and maintaining code.
"""

# Q3) What is Python?
Q3_ANS  = """
Python is a high-level, general-purpose, interpreted programming language.
Key features: readable syntax, dynamic typing, large standard library,
cross‑platform, and rich ecosystems for web, data, AI/ML, automation, etc.
"""

# Q4) Number sign detection
def number_sign(n: float) -> str:
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    return "zero"


# Q5) Factorial
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# Q6) Fibonacci series of given range (n terms or up to max value)
def fibonacci_n_terms(n: int) -> List[int]:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def fibonacci_upto(max_value: int) -> List[int]:
    seq = [0, 1]
    while seq[-1] + seq[-2] <= max_value:
        seq.append(seq[-1] + seq[-2])
    return seq


# Q7) How memory is managed in Python?
Q7_ANS  = """
Python uses automatic memory management:
• Reference counting plus generational garbage collection for cyclic refs.
• Private heap managed by the Python memory manager (PyMalloc).
• The user does not manually allocate/free; objects are deallocated when unreachable.
"""

# Q8) Purpose of 'continue' statement
Q8_ANS  = """
'continue' skips the rest of the current loop iteration and moves to the next
iteration. Useful to ignore specific cases without breaking the entire loop.
"""

# Q9) Swap two numbers (with and without temp)
def swap_with_temp(a: Any, b: Any) -> Tuple[Any, Any]:
    temp = a
    a = b
    b = temp
    return a, b

def swap_pythonic(a: Any, b: Any) -> Tuple[Any, Any]:
    a, b = b, a
    return a, b


# Q10) Even or odd
def is_even(n: int) -> bool:
    return n % 2 == 0

# Q11) Vowel test
def is_vowel(ch: str) -> bool:
    return ch.lo () in "aeiou"

# Q12) Sum of three integers; if any two are equal -> sum is 0
def sum_three_with_rule(a: int, b: int, c: int) -> int:
    if a == b or b == c or a == c:
        return 0
    return a + b + c


# Q13) Return true if two ints equal or sum/diff == 5
def rule_equal_or_five(a: int, b: int) -> bool:
    return a == b or abs(a - b) == 5 or (a + b) == 5


# Q14) Sum of first n positive integers
def sum_first_n(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (n + 1) // 2


# Q15) Length of a string
def string_length(s: str) -> int:
    return len(s)

# -----------------------------
# Q16) Character frequency in a string
def char_frequency(s: str) -> Dict[str, int]:
    return dict(Counter(s))

# -----------------------------
# Q17) Negative indexes
Q17_ANS  = """
Negative indexing lets you access elements from the end of a sequence.
Example: s[-1] is last char; lst[-2] is second last element. Useful when
you need relative positions from the tail without computing length.
"""
# -----------------------------
# Q18) Count occurrences of a substring
def count_substring(s: str, sub: str) -> int:
    return s.count(sub)

# -----------------------------
# Q19) Count occurrences of each word in a sentence
def word_frequency(sentence: str) -> Dict[str, int]:
    words = sentence.split()
    return dict(Counter(words))

# -----------------------------
# Q20) Single string from two strings with first two chars swapped
def swap_prefix_two(a: str, b: str) -> str:
    def swap2(x: str, y: str) -> Tuple[str, str]:
        if len(x) < 2 or len(y) < 2:
            return x, y
        return y[:2] + x[2:], x[:2] + y[2:]
    a2, b2 = swap2(a, b)
    return f"{a2} {b2}"

# -----------------------------
# Q21) Add 'in' or 'ly' rules
def add_ing_ly(s: str) -> str:
    if len(s) < 3:
        return s
    if s.endswith("ing"):
        return s + "ly"
    return s + "ing"

# -----------------------------
# Q22) Reverse string if length multiple of 4
def reverse_if_multiple_of_4(s: str) -> str:
    return s[::-1] if len(s) % 4 == 0 else s

# -----------------------------
# Q23) First 2 and last 2 chars (else empty)
def first2_last2(s: str) -> str:
    return s[:2] + s[-2:] if len(s) >= 2 else ""

# -----------------------------
# Q24) Insert a string in the middle of another
def insert_middle(host: str, insert: str) -> str:
    mid = len(host)//2
    return host[:mid] + insert + host[mid:]

# -----------------------------
# Q25) What is List? How to reverse?
Q25_ANS  = """
A list is a mutable ordered collection. Reverse via:
• in-place: lst.reverse()
• slicing: lst[::-1]
"""
def reverse_list(lst: List[Any]) -> List[Any]:
    return lst[::-1]

# -----------------------------
# Q26) Remove last object from a list
def pop_last(lst: List[Any]) -> Any:
    return lst.pop()  # raises IndexError if empty

# -----------------------------
# Q27) list1[-1]
def last_element(lst: List[Any]) -> Any:
    return lst[-1]

# -----------------------------
# Q28) append vs extend
Q28_ANS  = """
append(x) adds x as a single element at the end.
extend(iterable) iterates and appends each element of iterable.
"""
# -----------------------------
# Q29) largest, smallest, sum of list
def list_stats(lst: List[float]) -> Tuple[float, float, float]:
    return max(lst), min(lst), sum(lst)

# -----------------------------
# Q30) Compare two lists (content & order)
def lists_equal(a: List[Any], b: List[Any]) -> bool:
    return a == b

# -----------------------------
# Q31) Count strings with len>=2 and same first & last char
def count_special_strings(strings: List[str]) -> int:
    return sum(1 for s in strings if len(s) >= 2 and s[0] == s[-1])

# -----------------------------
# Q32) Remove duplicates from a list (preserve order)
def dedupe(lst: List[Any]) -> List[Any]:
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

# -----------------------------
# Q33) Check if list is empty
def is_empty(lst: List[Any]) -> bool:
    return len(lst) == 0

# -----------------------------
# Q34) Two lists share at least one common member
def have_common_member(a: Iterable[Any], b: Iterable[Any]) -> bool:
    set_b = set(b)
    return any(x in set_b for x in a)

# -----------------------------
# Q35) Squares from 1..30, print first/last 5
def first_last_5_square_list() -> Tuple[List[int], List[int]]:
    squares = [i*i for i in range(1, 31)]
    return squares[:5], squares[-5:]

# -----------------------------
# Q36) Unique elements of a list
def unique_list(lst: List[Any]) -> List[Any]:
    return list(set(lst))

# -----------------------------
# Q37) Convert list of characters into a string
def chars_to_string(chars: List[str]) -> str:
    return "".join(chars)

# -----------------------------
# Q38) Random item from a list
def random_choice(lst: List[Any]) -> Any:
    if not lst:
        raise ValueError("List is empty")
    return random.choice(lst)

# -----------------------------
# Q39) Second smallest number
def second_smallest(lst: List[float]) -> float:
    if len(lst) < 2:
        raise ValueError("Need at least two elements")
    uniq = sorted(set(lst))
    if len(uniq) < 2:
        raise ValueError("All elements equal")
    return uniq[1]

# -----------------------------
# Q40) Unique values from a list
def unique_values(lst: List[Any]) -> List[Any]:
    return list(set(lst))

# -----------------------------
# Q41) List contains a sub list
def contains_sublist(lst: List[Any], sub: List[Any]) -> bool:
    if not sub:
        return True
    for i in range(len(lst) - len(sub) + 1):
        if lst[i:i+len(sub)] == sub:
            return True
    return False

# -----------------------------
# Q42) Split list into different variables (unpacking)
def split_list(lst: List[Any]) -> Tuple[Any, ...]:
    return tuple(lst)

# -----------------------------
# Q43) Tuple vs List
Q43_ANS  = """
Tuple: immutable, fixed-size; List: mutable, dynamic-size.
Tuples can be used as dict keys if elements are hashable.
"""
# -----------------------------
# Q44) Tuple with different data types
def mixed_tuple() -> tuple:
    return (1, "two", 3.0, True)

# -----------------------------
# Q45) Unzip list of tuples
def unzip_tuples(lst: List[Tuple[Any, Any]]) -> Tuple[List[Any], List[Any]]:
    return list(map(list, zip(*lst)))

# -----------------------------
# Q46) Convert list of tuples into dictionary
def tuples_to_dict(pairs: List[Tuple[Any, Any]]) -> Dict[Any, Any]:
    return dict(pairs)

# -----------------------------
# Q47) Create dict using tuples
def dict_from_tuples(keys: Tuple[Any, ...], values: Tuple[Any, ...]) -> Dict[Any, Any]:
    return dict(zip(keys, values))

# -----------------------------
# Q48) Sort dictionary by value
def sort_dict_by_value(d: Dict[Any, Any], reverse: bool=False) -> List[Tuple[Any, Any]]:
    return sorted(d.items(), key=lambda kv: kv[1], reverse=reverse)

# -----------------------------
# Q49) Concatenate dictionaries
def concat_dicts(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    out: Dict[Any, Any] = {}
    for d in dicts:
        out.update(d)
    return out

# -----------------------------
# Q50) Check if key exists
def has_key(d: Dict[Any, Any], key: Any) -> bool:
    return key in d

# -----------------------------
# Q51) Traverse dictionary
def traverse_dict(d: Dict[Any, Any]) -> List[Tuple[Any, Any]]:
    return list(d.items())

# -----------------------------
# Q52) Check presence of a key
def key_present(d: Dict[Any, Any], key: Any) -> bool:
    return key in d

# -----------------------------
# Q53) Dict where keys 1..15
def dict_1_to_15() -> Dict[int, int]:
    return {i: i for i in range(1, 16)}

# -----------------------------
# Q54) Check multiple keys exist
def multiple_keys_exist(d: Dict[Any, Any], keys: Iterable[Any]) -> bool:
    s = set(d.keys())
    return set(keys).issubset(s)

# -----------------------------
# Q55) Merge two dictionaries
def merge_two_dicts(a: Dict[Any, Any], b: Dict[Any, Any]) -> Dict[Any, Any]:
    return {**a, **b}

# -----------------------------
# Q56) Map two lists into a dictionary
def map_two_lists(keys: List[Any], values: List[Any]) -> Dict[Any, Any]:
    return dict(zip(keys, values))

# -----------------------------
# Q57) Highest 3 values in a dict
def top3_values(d: Dict[Any, float]) -> List[Tuple[Any, float]]:
    return sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:3]

# -----------------------------
# Q58) Combine values in list of dicts by 'item'
def combine_amounts(rows: List[Dict[str, Any]]) -> Counter:
    c = Counter()
    for r in rows:
        c[r['item']] += r['amount']
    return c

# -----------------------------
# Q59-60) Dictionary from string counting letters
def dict_from_string_counts(s: str) -> Dict[str, int]:
    return dict(Counter(s))

# -----------------------------
# Q61) Factorial (function version)
def factorial_func(n: int) -> int:
    return factorial(n)

# -----------------------------
# Q62) Number in range
def in_range(n: float, start: float, end: float) -> bool:
    return start <= n <= end

# -----------------------------
# Q63) Perfect number check
def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    div_sum = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            div_sum += p
            if p != n // p:
                div_sum += n // p
        p += 1
    return div_sum == n

# -----------------------------
# Q64) Palindrome string check
def is_palindrome(s: str) -> bool:
    t = ''.join(ch.lo () for ch in s if ch.isalnum())
    return t == t[::-1]

# -----------------------------
# Q65) Basic types of functions
Q65_ANS  = """
Built-in functions, User-defined functions, Anonymous (lambda) functions,
Generator functions (yield), Recursive functions, Higher-order functions.
"""
# -----------------------------
# Q66) Random item from list or tuple
def random_from_seq(seq: Iterable[Any]) -> Any:
    seq = list(seq)
    if not seq:
        raise ValueError("Empty sequence")
    return random.choice(seq)

# -----------------------------
# Q67) Random item from a range
def random_from_range(start: int, stop: int) -> int:
    return random.randrange(start, stop)

# -----------------------------
# Q68) Random number in python
def random_float_0_1() -> float:
    return random.random()

# -----------------------------
# Q69) Set starting value (seed)
def set_random_seed(seed: int) -> None:
    random.seed(seed)

# -----------------------------
# Q70) Randomize items of a list in place
def shuffle_in_place(lst: List[Any]) -> None:
    random.shuffle(lst)

# -----------------------------
# Q71) File function, keywords to create/write file
Q71_ANS  = """
Use built-in open(file, mode, encoding). Common write modes: 'w' (write),
'a' (append), 'x' (exclusive create), 'b' (binary), 't' (text default), '+' (update).
Use context manager: with open(path, 'w', encoding='utf-8') as f: ...
"""
# -----------------------------
# Q72) Read entire text file
def read_all(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# -----------------------------
# Q73) Append text to file and display
def append_and_read(path: str, text: str) -> str:
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text)
    return read_all(path)

# -----------------------------
# Q74) Read first n lines
def read_first_n_lines(path: str, n: int) -> List[str]:
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line.rstrip('\n'))
    return lines

# -----------------------------
# Q75) Read last n lines (efficient for big files)
def read_last_n_lines(path: str, n: int) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f.readlines()[-n:]]

# -----------------------------
# Q76) Read file line by line into a list
def read_lines_to_list(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

# -----------------------------
# Q77) Read file line by line into a variable (single string)
def read_lines_to_string(path: str) -> str:
    return read_all(path)

# -----------------------------
# Q78) Find longest words in a file
def longest_words(path: str) -> List[str]:
    text = read_all(path)
    words = [w.strip(".,!?;:\"'()[]{}").lo () for w in text.split()]
    if not words:
        return []
    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]

# -----------------------------
# Q79) Count number of lines
def count_lines(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

# -----------------------------
# Q80) Count frequency of words in a file
def word_freq_in_file(path: str) -> Counter:
    text = read_all(path).lo ()
    tokens = [w.strip(".,!?;:\"'()[]{}") for w in text.split() if w.strip()]
    return Counter(tokens)

# -----------------------------
# Q81) Write a list to a file (one per line)
def write_list_to_file(path: str, items: Iterable[str]) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        for it in items:
            f.write(str(it) + '\n')

# -----------------------------
# Q82) Copy contents of a file to another
def copy_file(src: str, dst: str) -> None:
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
        fdst.write(fsrc.read())

# -----------------------------
# Q83) Exception handling explanation
Q83_ANS  = """
Exceptions represent runtime errors; handling uses try/except/else/finally.
try: code that may fail; except: handle specific errors; else: runs if no error;
finally: always runs (cleanup).
"""
# -----------------------------
# Q84) How many except statements? Name some exceptions
Q84_ANS  = """
A try-block can have multiple except clauses. Common built-ins:
ValueError, TypeError, KeyError, IndexError, ZeroDivisionError,
IOError/OSError, FileNotFoundError, AssertionError.
"""
# -----------------------------
# Q85) When is else executed?
Q85_ANS  = """
The else block executes only if no exception was raised in the try block.
"""
# -----------------------------
# Q86) Can one except handle multiple exceptions?
Q86_ANS  = """
Yes: `except (TypeError, ValueError) as e:`
"""
# -----------------------------
# Q87) When is finally executed?
Q87_ANS  = """
finally runs no matter what (after try/except), even if an exception occurred
or a return happened, typically for releasing resources.
"""
# -----------------------------
# Q88) What happens when '1' == 1 is executed?
Q88_ANS  = """
It evaluates to False because the operands have different types (str vs int).
Python does not coerce types for equality here.
"""
# -----------------------------
# Q89) Try/Except/Finally example
def divide(a: float, b: float) -> Optional[float]:
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    else:
        # ran only if no exception
        result = float(result)
    finally:
        # could log or cleanup here
        pass
    return result

# -----------------------------
# Q90) Enforce odd number input — raise exception on even
def ensure_odd(n: int) -> int:
    if n % 2 == 0:
        raise ValueError("Only odd numbers are allowed")
    return n

# -----------------------------
# Demonstration (quick samples for a subset)
def _demo():
    print("Q4 number_sign(0) ->", number_sign(0))
    print("Q5 factorial(5) ->", factorial(5))
    print("Q6 fibonacci_n_terms(7) ->", fibonacci_n_terms(7))
    print("Q10 is_even(8) ->", is_even(8))
    print("Q12 sum_three_with_rule(1, 2, 3) ->", sum_three_with_rule(1, 2, 3))
    print("Q13 rule_equal_or_five(2, 7) ->", rule_equal_or_five(2, 7))
    print("Q16 char_frequency('hello') ->", char_frequency('hello'))
    print("Q31 count_special_strings(['aba','xyz','aa','x','bbb']) ->",
          count_special_strings(['aba','xyz','aa','x','bbb']))
    print("Q39 second_smallest([5, 1, 2, 2, 3]) ->", second_smallest([5,1,2,2,3]))
    print("Q63 is_perfect(28) ->", is_perfect(28))
    print("Q64 is_palindrome('A man, a plan, a canal: Panama') ->",
          is_palindrome('A man, a plan, a canal: Panama'))
    print("Q89 divide(10, 0) ->", divide(10, 0))

if __name__ == "__main__":
    _demo()
