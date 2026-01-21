# 듣보잡 (BOJ 1764) review

## 1) 이 문제에서 습득해야 하는 기술/방법

### 핵심 자료구조: set (해시 집합)
- 이름 “존재 여부” 확인을 빠르게 하려고 `set`을 사용한다.
- 평균 시간복잡도:
  - `name in set` : O(1)
- N, M이 최대 500,000이라서 리스트로 비교하면 O(N*M)로 터진다.

### 핵심 연산 2가지 중 선택
1) 교집합 방식(간단)
- `heard & seen` 또는 `heard.intersection(seen)`
- 둘 다 set을 만들어야 함

2) 스트리밍 방식(극단 케이스에 유리)
- 한쪽만 set으로 만들고, 다른 쪽은 입력을 읽으면서 `in`으로 체크해 결과 리스트에 담는다.
- “x=1, y=50만” 같은 케이스에서 불필요한 set 생성(50만)을 피할 수 있어서 메모리/시간에 유리할 수 있음.

### 출력 최적화
- 결과가 많을 수 있으므로 `print` 여러 번보다
  `sys.stdout.write("\n".join(...))` 형태가 안정적이다.

---

## 2) 내 코드 리뷰

### 잘한 점
- 교집합 문제라는 걸 파악하고 `set` + `intersection`으로 해결한 접근은 정석이다.
- 결과를 `sorted()`로 정렬해서 “사전순 출력” 조건을 충족했다.
- 출력도 `sys.stdout.write("\n".join(res))`로 빠르게 처리했다.

### 아쉬운 점 / 개선 포인트
- `len(x) >= len(y)` 비교 후 인자를 바꿔주는 최적화는 체감 효과가 거의 없다.
  - 어차피 `set(y)` 생성 비용이 큰 순간, 순서 최적화 의미가 작아진다.
- 함수 `compare` 내부에서 다시 `set(x)`, `set(y)`로 바꾸는 구조는 불필요하게 복잡하다.
  - 처음부터 set으로 읽고 처리하면 더 깔끔하다.

### 추천 “코테용 베스트” 풀이 2가지

#### A) 가장 단순한 정석(교집합)
```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

heard = {input().strip() for _ in range(n)}
seen  = {input().strip() for _ in range(m)}

res = sorted(heard & seen)

sys.stdout.write(str(len(res)) + "\n" + "\n".join(res))
