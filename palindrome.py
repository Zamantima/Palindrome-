def is_palindrome(s):
    s = s.lower()
    start_index = 0
    end_index = len(s)-1
    flag = True

    while start_index < end_index:
       if s[start_index] != s[end_index]:
           flag = False
       break
       start_index += 1
       end_index -= 1

    if flag:
        return True
    else:
        return False




