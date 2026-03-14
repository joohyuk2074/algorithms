def is_alphanumetic(c):
    if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
        return True

    if(c >= '0' and c <= '9'):
        return True

    return False
    
def is_palindrome(s):
    # alphanumeric이 아닌 문자 제거 후 모두 소문자로 전환
    text = []
    for c in s:
        if is_alphanumetic(c):
            text.append(c.lower())
    text = ''.join(text)

    # 인덱스 초기화
    start = 0
    end = len(text) - 1

    while start < end:
        if text[start] != text[end]:
            return False

        start += 1
        end -= 1
        

    return True

  


letter = input("문자열을 입력해주세요.")
print(is_palindrome(letter))

