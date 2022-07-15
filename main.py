def func(wrd):
    wrd = list(s[::-1])
    done = 0
    for i in range(1,len(s)):
        if s[i-1] > s[i]:
            for j in range(i):
                if s[j] > s[i]:
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    return("".join(s[::-1]))
            break
    else:
        print("no answer")

for _ in range(len(input())):
    w = input()
    
print(func(w))