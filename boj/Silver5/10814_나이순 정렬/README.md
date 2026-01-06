heapq.heappush(q, ((age, i), name))

힙은 첫 번째 원소부터 비교해서 작은 게 먼저 나와.

너는 원소를 ((age, i), name) 형태로 넣었지?

비교는 이렇게 진행돼:

먼저 (age, i)끼리 비교

age가 작은 게 먼저

age가 같으면 i(입력 순서)가 작은 게 먼저

즉, 안정 정렬(stable sort) 효과를 i로 만든 거야.

a = heapq.heappop(q)

가장 작은 우선순위(=나이 가장 적고, 동률이면 먼저 들어온 것)가 튀어나옴.

a의 형태는 ((age, i), name) 이고

a[0][0] = age

a[1] = name

그래서 출력이:

print(a[0][0], a[1])

여기서 중요한 포인트 2개
1) 굳이 i를 넣는 이유

파이썬 힙은 “안정성”이 보장되는 정렬이 아니야.
그래서 나이가 같을 때 입력 순서 유지하려면 i 같은 tie-breaker가 필요해.

(근데 이 문제는 사실 sort 쓰면 파이썬 정렬이 안정 정렬이라 i 없이도 됨.)

2) 시간복잡도

heappush를 N번: N log N

heappop을 N번: N log N
→ 총 O(N log N) (정렬과 같은 급)