"""Main functions"""

import re

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    n = string
    n = n.lower()
    n = n.replace(" ", "")
    n = re.sub(r'[^\w\s]','',n)
    n2 = n[::-1]

    if n == n2:
        return True
    else:
        return False
    