import collections
# 문자열을 받아 애너그램단위로 그룹핑 하라


strs = ["eat","tea","tan", "ate", "nat", "bat"]

# 그룹핑 후 담을 변수
anagrams = collections.defaultdict(list)

for word in strs:

    anagrams[''.join(sorted(word))].append(word)

print(anagrams.values())
