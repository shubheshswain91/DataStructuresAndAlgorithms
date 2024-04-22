class PalindromeCheck:
    def isPalindrome(self, s):
        s = s.lower()
        new_s = ""

        for char in s:
            if char.isalnum():
                new_s += char

        return new_s == new_s[::-1]

check = PalindromeCheck()

case1 = "A man, a plan, a canal: Panama"
case2 = " "
case3 = "racecar"
case4 = "Abra kadabra"
case5 = "Ma1aya1am"

print(check.isPalindrome(case1))
print(check.isPalindrome(case2))
print(check.isPalindrome(case3))
print(check.isPalindrome(case4))
print(check.isPalindrome(case5))
