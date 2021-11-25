def alphabet_position(text):
    ans = []
    pos = {chr(i+96):i for i in range(1,27)}
    for letter in text:
        if letter.lower() in pos:
            ans.append(str(pos.get(letter.lower())))
    return ' '.join(ans)

print(alphabet_position("aBc DEf"))