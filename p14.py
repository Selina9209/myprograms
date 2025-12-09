def jkgsgj(text):
    u = 0
    l = 0
    for x in text:
        if x.isalpha():
            if x.isupper():
                u += 1
            if x.islower():
                l += 1
        else:
            u += 0
            l += 0
    if u > l:
        return 1
    elif l > u:
        return -1
    elif l == u:
        return 0


print(jkgsgj("39hkejhfsjdfhJKHJHKJHKHEOUIFH920e      "))