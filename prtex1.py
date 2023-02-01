def check(s):
    if len(s)==0:
        return s
    if s[0]=="p" and s[1]=="i":
        return "3.14"+check(s[2:])
    if s[0]=="p":
        return "p"+check(s[1:])
    else: return s[0]+check(s[1:])
s="piayaanpipi"
ab=check(s)
print(ab)