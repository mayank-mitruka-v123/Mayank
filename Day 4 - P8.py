def roman_to_int(s):
    d={'I':1,'V':5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    i=0
    while i< len(s):
        if i+1<len(s) and d[s[i]] < d[s[i+1]]:
            total+=d[s[i+1]]-d[s[i]]
            i+=2
        else:
            total += d[s[i]]
            i+=1
        return total
print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))
print(roman_to_int("LV"))
