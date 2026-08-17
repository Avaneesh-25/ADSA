def Check_Palindrome(n: int, s: str) -> bool:
    left, right = 0, n - 1
    
    while left < right:
        if s[left] != s[right]:
            # Try skipping the left character or the right character
            skip_left = s[left + 1 : right + 1]
            skip_right = s[left:right]
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
        left += 1
        right -= 1
        
    return True


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))