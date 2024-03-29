# 큐(Queue): FIFO - 선입선출
* 큐는 스택과 동일하게 가장 최근에 저장된 값 다음에 새로운 값이 저장되지만 가장 오래전에 저장된 값부터 나간다는 차이가 있다. - FIFO(First In First Out, 선착순) 원칙
* 스택과 마찬가지로 리스트는 큐의 모든 연산을 지원하지만, 리스트는 동적 배열로 구현되어 큐의 연산을 수행하기엔 효율적이지 않다. 따라서 파이썬에서 큐를 구현할 땐 후술할 덱을 사용한다.

# 덱(Dequeue): Stack + Queue
* 덱은 스택과 큐의 연산을 모두 지원하는 자료구조이다.
* 왼쪽과 오른쪽에서 모두 삽입과 삭제가 가능한 큐다.
* 파이썬에선 collections라는 모듈에 deque란 클래스로 덱이 이미 구현되어 있다.

## 모듈