"""Main functions"""

import re

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    n = string
    n = n.lower()
    n2 = n[::1]
    n2 = n2.replace(" ", "")
    n2 = re.sub(r'[^\w\s]','',n2)
    n2 = n2.lower()

    if n == n2:
        return True
    else:
        return False
