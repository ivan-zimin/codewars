import string as strlib

def to_jaden_case(string):
    return strlib.capwords(string)

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
# Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"