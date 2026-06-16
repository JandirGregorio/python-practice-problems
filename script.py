# Python Functional Programming Exercises
# Background: JavaScript analogues are noted where helpful.
# Fill in each function body. Run with: python3 script.py

from functools import reduce, partial


# ── Exercise 1: map() ──────────────────────────────────────────────────────────
# Like JS: [1, 2, 3].map(x => x ** 2)
# Return a list of each number squared.
def square_all(numbers):
    return list(map(lambda x: x ** 2, numbers))  # hint: use map() and wrap in list()


# ── Exercise 2: filter() ───────────────────────────────────────────────────────
# Like JS: arr.filter(x => x % 2 === 0)
# Return only the even numbers from the list.
def keep_evens(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))  # hint: use filter() and wrap in list()


# ── Exercise 3: reduce() ───────────────────────────────────────────────────────
# Like JS: arr.reduce((acc, x) => acc + x, 0)
# Return the sum of all numbers using reduce (no sum() built-in allowed).
def sum_all(numbers):
    return reduce(lambda a, b: a + b, numbers)  # hint: from functools import reduce


# ── Exercise 4: List comprehension ────────────────────────────────────────────
# Python's idiomatic alternative to map+filter in one expression.
# Return words longer than 3 characters, uppercased.
# e.g. ["hi", "world", "foo", "python"] → ["WORLD", "PYTHON"]
def long_words_upper(words):
    return [word.upper() for word in words if len(word) > 3]  # hint: [expr for x in iterable if condition]


# ── Exercise 5: Lambda + sorted() ─────────────────────────────────────────────
# Like JS: arr.sort((a, b) => a.age - b.age)
# Sort a list of dicts by the "age" key using a lambda as the key argument.
def sort_by_age(people):
    return sorted(people, key=lambda person: person['age'])  # hint: sorted(people, key=lambda p: ...)


# ── Exercise 6: zip() ─────────────────────────────────────────────────────────
# Like JS: names.map((name, i) => ({ name, score: scores[i] }))
# Pair two lists into a list of tuples: (name, score).
def pair_names_scores(names, scores):
    return list(zip(names, scores))  # hint: list(zip(...))


# ── Exercise 7: Closure / function factory ────────────────────────────────────
# Like JS: const makeMultiplier = n => x => x * n
# Return a function that multiplies its argument by `factor`.
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply


# ── Exercise 8: functools.partial ─────────────────────────────────────────────
# Like JS: const double = multiply.bind(null, 2)
# Use partial() to create a `double` function from a generic multiply(a, b).
def multiply(a, b):
    return a * b

double = partial(multiply, 2)  # replace None with partial(multiply, 2)


# ── Exercise 9: Chaining map + filter + reduce ────────────────────────────────
# No JS analogy needed — you know this pattern.
# From a list of numbers: keep positives, square them, then return their sum.
def sum_of_squared_positives(numbers):
    return reduce(lambda a, b: a + b, [num ** 2 for num in numbers if num >= 0])  # chain filter → map → reduce (or a comprehension + sum())


# ── Exercise 10: Higher-order function ────────────────────────────────────────
# Like JS: function pipe(...fns) { return x => fns.reduce((v, f) => f(v), x) }
# Implement pipe(fns, value): apply a list of single-arg functions left-to-right.
# e.g. pipe([double, lambda x: x + 1], 3) → double(3)=6 → 6+1=7
def pipe(fns, value):
    return reduce(lambda v, f: f(v), fns, value)


# ── Tests ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert square_all([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert keep_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert sum_all([1, 2, 3, 4, 5]) == 15
    assert long_words_upper(["hi", "world", "foo", "python"]) == ["WORLD", "PYTHON"]
    assert sort_by_age([{"name": "B", "age": 30}, {"name": "A", "age": 25}]) == [{"name": "A", "age": 25}, {"name": "B", "age": 30}]
    assert pair_names_scores(["Alice", "Bob"], [95, 87]) == [("Alice", 95), ("Bob", 87)]
    triple = make_multiplier(3)
    assert triple(5) == 15
    assert double(4) == 8
    assert sum_of_squared_positives([-1, 2, -3, 4]) == 20  # 2²+4² = 4+16
    assert pipe([lambda x: x * 2, lambda x: x + 1], 3) == 7

    print("All tests passed!")
