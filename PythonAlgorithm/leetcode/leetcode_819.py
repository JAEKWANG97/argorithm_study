# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 
# 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.


import collections
import re
# 3107H#FBFB

paragraph = "Bob hit a ball, the hit BALL flew far after ,,it was hit"
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ',paragraph).lower().split()
            if word not in banned]

print(words)

counts = collections.Counter(words)
print(counts)
print(counts.most_common(2)[0])


# dddddddd

# print(counts.most_common(1)[0][0])

# 출력 ㅣ "ball"


#입력깂에는 대소문자가 섞여 있으며 쉼표 등 구두점이 존재한다.
# 따라서 데이터 클렌징이라 부르는 입력값에 대한 전처리 작업이 필요하다.
# 좀 더 편리하게 처리하기 위해 정규식을 섞어 쓰면 다음과 같이 처리할 수 있다.

# 정규식에서는 \w 는 단어 문자를 뜻하며 ^는 not을 의미한다.counts
# 따라서 위 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역활을 한다.

# 아울러 리스트 컴프리 헨션의 조건절에는 banned에 포함되지 않은 단어만을 대상으로 한다.

# 따라서 words에는 소문자, 구두점을 제외하고 banned를 제외한 단어 목록이 저장된다.

# counts = collections.defaultdict(int)
# for word in words:
#     counts[word] += 1

# 여기서 개수를 담아주는 변수는 딕셔너리를 사용하며 defaultdict()를 사용해 int기본값이 자동으로 부여되게 했다.

# 따라서 여기서는 키 존재 유무를 확인할 필요 없이 즉시 counts[word] += 1 을 수행할 수 있다.

# 딕셔너리 변수인 counts에서 값이 가장 큰 키를 가져온다. 즉 수학에서 argmax와 동일하다.

# 그런데 파이선의 기본 타입은 argmax를 지원하지 않는다. 과학 계산 라이브러리인 넘파이는 이를 잘 지원하지만,
# 아쉽게도 코딩 테스트에서는 어떠한 외부 라이브러리도 사용할 수 없다.

# 따라서 이처럼 max() 함수에 key를 지정해 argmax를 간접적으로 추출할 수 있다.

# 개수를 처리하는 부분은 Counter 모듈을 사용하면 좀 더 깔끔하게 처리할 수 있다.

# 다음 코드는 words에서 가장 한하게 등장하는 단어의 첫번째 값을 most_common(1)으로 추출한다.

# 문제의 입력값에서는 [('ball', 2)]며가 되며, 이값의 [0][0]을 추출해서 최정적으로 첫 번째 인덱스의 키를 추출하게 된다.

# 이렇게 추출한 키인 ball 은 가장 흔한 단어가 되므로, 이제 이 값을 리턴한다.

