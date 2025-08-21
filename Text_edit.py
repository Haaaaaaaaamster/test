big_string = "이건   테스트   문자열   입니다   아주     깁니다"

# 1) 공백 단위로 split → 불필요한 공백 자동 제거
words = big_string.split()

# 2) 단어마다 줄바꿈으로 join
result = "\n".join(words)

print(result)
