from collections import Counter
cnt = Counter()
for word in ["red", 'blue', "red", 'blue', "red", 'yellow']:
    cnt[word] +=1
print(cnt)

from collections import OrderedDict
s = OrderedDict()
s['a'] = 'A'
s['b'] = "B"
s['c'] = 'C'

for key,value in s.items():
    print(key,value)