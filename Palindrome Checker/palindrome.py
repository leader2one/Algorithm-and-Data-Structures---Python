def isPalindrome(s) :
    if (s == None || s.length() == 0)
        return True

    l = 0, r = s.length() - 1;
    while (l < r) :
        if (s.charAt(l) != s.charAt(r)):
            return False
        l++; r--;
    
	return True;