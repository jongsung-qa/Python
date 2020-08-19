# regular express import
import re 

# compile
p = re.compile("ca.e") 

# function declaration
def print_match(m):
    if m:
        print("m.group() : ", m.group()) # Returns a matching string
        print("m.string() : ", m.string) # Returns the entered string
        print("m.start() : ", m.start()) # Start index of matching string
        print("m.end() : ", m.end())  # end index of matching string
        print("m.span() : ", m.span())  # Start and end index of matching string
    else:
        print("Not matching")

# Verify that a given string matches from the beginning
# If you input a string "thecasestudy", an error will be provided.
m = p.match("casestudy") 
print_match(m)

# Verify that it matches a given string
m = p.search("thecasestudy") 
print_match(m)

# Return all matches to list
lst = p.findall("careless cafe") 
print(lst)


# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 처음부터 일치하는지 확인
# 3. m = p.serach("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cage, case...
# ^ (^de) : 문자열의 시작 > desk, destination ...
# $ (se&) : 문자열의 끝 > case, base ...