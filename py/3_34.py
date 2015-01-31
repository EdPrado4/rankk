message = '1,12,3,3,17,5,2,22,24,10,10,11,19,13,8,6,22,14,14,12,27,6,9,24,2,22,4,9,17,5,14,22,30,19,23,4,9,2'
message_bin = [int(i) for i in message.split(',')]
words = ['the', 'of']


def decrypt(message_bin, key):
    i, result = 0, []
    for c in message_bin:
        result.append(c ^ key[i])
        i = (i + 1) % len(key)
    return result


def valid(message):
    for word in words:
        if word not in message:
            return False
    return True


def to_str(a):
    return ''.join([chr(i) for i in a])


key = [103, 101, 109]
print(to_str(key))
print(to_str(decrypt(message_bin, key)))

for a in range(ord('a'), ord('z') + 1):
    for b in range(ord('a'), ord('z') + 1):
        for c in range(ord('a'), ord('z') + 1):
            key = [a, b, c]
            original = to_str(decrypt(message_bin, key))
            if valid(original):
                print(original)
                print(to_str(key))

original = 'findthesumoftheasciivaluesinthisstring'
sum = 0
for s in original:
    sum += ord(s)
print(sum)



  