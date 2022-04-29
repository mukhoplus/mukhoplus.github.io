---
layout: post
title: itertools
date: 2022-03-15 12:23 +0000
last_modified_at: 2022-04-29 23:09:22 +0000
tags: [코딩테스트, Python]
toc:  true
---

알고리즘을 풀다 조합 또는 수열을 만들거나, 그것 형식의 결과값을 만들어야 하는 문제를 만났습니다.<br>
Backtracking을 통해 풀 수 있으나, itertools를 사용하면 쉽게 해결할 수 있다기에 공부해보았습니다.<br>

```python
'''
itertools 라이브러리로 조합과 수열을 구해보겠습니다.
반환되는 모든 '조합과 순열'은 tuple로 주어지나, list로 변환하여 출력했습니다.
정렬
    조합: combinations
    중복조합: combinations_with_replacement
짝지어지는 경우
    순열: permutations
    중복순열: product
'''
from itertools import combinations, combinations_with_replacement, permutations, product

lst = [1, 2]

# combinations(iterable, r): iterable에서 원소 개수가 r개인 조합 뽑기(중복x)
for n in range(1, len(lst)+1):
    if n == 2:
        print('-----------')
    for i in combinations(lst, n):
        i = list(i)
        print(i)

print('===========')
# combinations_with_replacement(iterable, r): iterable에서 원소 개수가 r개인 중복조합 뽑기
for n in range(1, len(lst)+1):
    if n == 2:
        print('-----------')
    for i in combinations_with_replacement(lst, n):
        i = list(i)
        print(i)

print('===========')
# permutations(iterable, r): iterable에서 원소 개수가 r개인 순열 뽑기(중복x)
for n in range(1, len(lst)+1):
    if n == 2:
        print('-----------')
    for i in permutations(lst, n):
        i = list(i)
        print(i)

print('===========')
# product(*iterables, repeat=1): 여러 iterable을 넣어줄 수 있고, repeat의 인자만큼 그것들의 모든 짝을 지어서 반환함
for n in range(1, len(lst)+1):
    if n == 2:
        print('-----------')
    for i in product(lst, repeat=n):
        i = list(i)
        print(i)

'''
itertools
    combinations: [1] [2] [1, 2]
    combinations_with_replacement: [1] [2] [1, 1] [1, 2] [2, 1]
    permutations: [1] [2] [1, 2] [2, 1]
    product: [1] [2] [1, 1] [1, 2] [2, 1] [2, 2]
'''
```
