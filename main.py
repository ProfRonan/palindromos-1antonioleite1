"""Main functions"""

import re

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    n = string
    n2 = n[::1]
    n2 = n2.replace(" ", "")
    n2 = re.sub(r'[^\w\s]','',n2)

    if n == n2:
        return True
    else:
        return False
