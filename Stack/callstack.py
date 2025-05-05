"""
Callstack
"""

text = "hello there!"

def make_upper(tet: str) -> str:
    text.upper()
    return text

print(len(make_upper(text)))
 