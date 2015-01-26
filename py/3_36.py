import re

test_cases = []
ends = {'[passed]': True, '[failed]': False}
for line in open('3_36_test'):
    file, result = line.rstrip().split()
    test_cases.append((file, ends[result]))

regex = re.compile('(hello.*\.(jpg|gif|png))$|(a.jpg)$')
for file, result in test_cases:
    matched = regex.match(file) is not None
    if matched != result:
        print(file, result)


