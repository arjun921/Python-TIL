# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3
# failed

q = int(input())

for _ in range(q):
    s = input()
    signatures = {}

    # iterate over all substrings of s
    for start in range(len(s)):
        for finish in range(start, len(s)):
            # initialize substring signature
            # 26 for 26 letters
            signature = [0 for _ in range(26)]
            # print(s[start:finish+1])
            for letter in s[start:finish+1]:
                signature[ord(letter)-ord('a')] += 1
            # tuples are hashable in contrast to lists
            signature = tuple(signature)
            # print(s[start:finish+1],signature)
            signatures[signature] = signatures.get(signature, 0) + 1

    # print(signatures)
    res = 0
    for count in signatures.values():
        # print(count)
        res += count*(count-1)/2
    # print(res)
    print(int(res))
