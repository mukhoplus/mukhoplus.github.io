---
layout: post
title: Queue와 Deque
date: 2022-03-15 11:41 +0000
last_modified_at: 2022-03-15 11:41 +0000
tags: [코딩테스트, Python]
toc:  true
---

알고리즘을 짜다보면 stack이나 queue를 사용해야 하는 경우가 있습니다.<br>
그때 익숙하지 않은 Python의 queue 사용을 위해 내용을 기록합니다.

```python
from queue import Queue
from collections import deque

'''
Queue: 선입선출, 너비우선탐색(BFS)에 사용
    1. List: append(x), pop(0) 또는 insert(0, x), pop()으로 구현 가능. 단, 전자의 pop과 후자의 insert는 O(N)이기 때문에 지양해야함.
    2. Deque: Double-Ended Queue로, data를 양쪽에서 추가하고 제거할 수 있다. 단, 무작위 접근시 O(N)이다.
    3. Queue: 큐다.
'''
q = Queue()
print(q.empty()) # 비어있으면 True, 아니면 False를 반환
q.put(1) # 값 삽입.
q.put(2)
q.put(3)
print(q.get()) # q에서 선입 데이터를 삭제하면서 반환
print(q.qsize()) # q의 사이즈를 반환
'''
True # []
# [1, 2, 3]
1 # [2, 3]
2 # [2, 3]
'''
print('--------')
'''
Deque: 앞과 뒤, 양쪽 모두에서 데이터를 추가하고 삭제할 수 있다.
'''
dq = deque()
dq.append(1) # dq의 뒤에 data 삽입
dq.appendleft(2) # dq의 앞에 data 삽입
dq.insert(1, 3) # dq의 1번째 위치에 data 3 삽입
dq.reverse() # dq 내부의 값의 순서를 뒤집는다
print(dq.count(1)) # dq 안에 있는 data 갯수 반환
print(dq.popleft()) # dq의 앞 데이터 삭제하면서 반환
print(dq.pop()) # dq의 뒤 데이터를 삭제하면서 반환
dq.remove(3) # dq에서 data 3을 삭제. (★삭제하려는 값이 없을 시 오류 반환)

'''
# [2, 3, 1]
# [1, 3, 2]
1 # [1, 3, 2]
1 # [3, 2]
2 # [3]
# []
'''
```
