num = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
freq = {}
for n in num:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq)
print(type(freq))

str = "abcaadefdffbebb"
freq_str = {}
for c in str:
    if c in freq_str:
        freq_str[c] += 1
    else:
        freq_str[c] = 1

print(freq_str)
print(type(freq_str))
