if n > m:
    more_cookies = n - m
else:
    mod = m%n
    if mod == 0:
        more_cookies = 0
    else:
        q = int(m/n)
        more_cookies = m - q*n

print more_cookies
