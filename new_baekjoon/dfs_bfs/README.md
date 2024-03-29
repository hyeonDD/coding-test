# 깊이 우선 탐색 (DFS, Depth-First Search)의 개념

- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법

1. 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 이곳으로부터 다른 방향으로 다시 탐색을 진행하는 방법과 유사함

2. 즉 넓게(wide) 탐색하기 전에 깊게(deep) 탐색함 

3. 모든 노드를 방문하고자 하는 경우에 이 방법을 선택함

4. 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 좀 더 간단함

5. 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느림

# 깊이 우선 탐색의 특징

- 자기 자신을 호출하는 순환 알고리즘의 형태를 지님

- 이 알고리즘을 구현할 때 가장 큰 차이점은 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사해야한다는 것 (이를 검사하지 않을 경우 무한루프에 빠질 위험이 있음)

# 너비 우선 탐색 (BFS, Breadth-First Search)

- 루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 먼저 탐색하는 방법

1. 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법
2. 즉 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것
3. 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택함
ex) 지구 상에 존재하는 모든 친구 관계를 그래프로 표현한 후 Ash 와 Vanessa 사이에 존재하는 경로를 찾는 경우

* 깊이 우선 탐색의 경우 - 모든 친구 관계를 다 살펴봐야할지도 모름

* 너비 우선 탐색의 경우 - Ash와 가까운 관계부터 탐색

# 너비 우선 탐색(BFS)의 특징

- BFS 는 재귀적으로 동작하지 않는다.
- 이 알고리즘을 구현할 때 가장 큰 차이점은 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사해야한다는 것이다 이를 검사하지 않을 경우 무한 루프에 빠질 위험이 있다.
- BFS 는 방문한 노드들을 차례로 저장한 후 꺼낼 수 있는 자료 구조인 큐(Queue)를 사용함 
- 즉 선입선출(FIFO) 원칙으로 탐색