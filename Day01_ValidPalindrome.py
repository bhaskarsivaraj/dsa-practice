def isPalindrome(s): 
        onlyAlphaNumValues = ""
        for c in s:
            if c.isalnum():
                onlyAlphaNumValues+=c.lower()
        left,right = 0,len(onlyAlphaNumValues)-1
        while left<right:
            if onlyAlphaNumValues[left]!=onlyAlphaNumValues[right]:
                return False
            left+=1
            right-=1
        return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))