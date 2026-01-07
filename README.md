# coding_test

코딩테스트 문제 풀이를 **사이트 → 난이도 → 문제** 순으로 정리하는 레포지토리.

---

## 📁 Directory Structure

문제는 아래 규칙으로 폴더를 구성한다.

- `코딩테스트사이트/난이도/문제폴더/`

예시:
- `boj/silver/1000_a+b/`
- `programmers/lv2/12345_problem-name/`

---

## 🏷️ Problem Folder Naming Rule

문제 폴더 이름은 기본적으로 다음 형식이다.

- `문제번호_문제이름`

그리고 **중요하거나 나중에 다시 볼 필요가 있는 문제**는 문제번호 앞에 `*`를 붙여 표시한다.

- `*문제번호_문제이름`

예시:
- `12345_problem-name`
- `*12345_problem-name`  ← 복습 필요/중요 표시

---

## 🧩 Files Inside Each Problem Folder

각 문제 디렉토리에는 아래 파일들이 존재한다.

- `solve.py` **(필수)**
  - 내가 직접 풀이를 작성하고 디버깅하는 메인 코드

- `solution_byGPT.py`
  - 문제를 푼 뒤 GPT로부터 얻은 **최적 풀이/개선 풀이**를 저장

- `review.md`
  - 문제를 푼 뒤 self-review

- `other_solution.py` *(선택)*
  - 다른 사람의 풀이 중 참고할 가치가 높은 코드를 저장

---

## 🔁 Workflow

1. 문제를 풀기 전, 문제 디렉토리를 먼저 생성  
2. `solve.py`로 풀이 작성 + 디버깅  
3. 풀이 완료 후 `solution_byGPT.py` 정리  
4. 좋은 참고 코드가 있으면 `other_solution.py`로 추가  
5. GitHub에 커밋 & 푸시

---

## ✅ Commit Message Example (Optional)

- `boj/12345: solve`
- `boj/12345: add gpt solution`
- `boj/12345: add other solution`
