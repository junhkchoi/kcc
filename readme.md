# kcc 홈페이지 제작 레포

## 1. 개발 계획
| App Name | Feature |
|------|---|
| post | 공지 | 
| ranking  | 출석 점수, 과제 점수, 참여 점수 관리 |
| home | 기본 홈페이지, 네비게이션 |
### Design -> home -> post -> ranking -> Deploy

## 2. 커밋 컨벤션
 타입     | 설명                                              |
|----------|--------------------------------------------------|
| **feat** | 새로운 기능 추가                                 |
| **fix**  | 버그 수정                                       |
| **docs** | 문서 추가 및 수정 (README, 문서 수정 등)        |
| **style** | 코드 스타일 변경 (포맷팅, 세미콜론 추가 등)    |
| **refactor** | 코드 리팩토링 (기능 변경 없이 구조 개선)    |
| **perf** | 성능 개선                                       |
| **test** | 테스트 코드 추가 또는 수정                      |
| **chore** | 기타 변경 사항 (빌드 설정, 패키지 매니저 설정) |
| **ci** | CI/CD 관련 설정 수정                             |

## 3. HTML/CSS 네이밍 컨벤션
### 3-1. 클래스(Class) 및 아이디(ID) 네이밍 규칙

| 규칙 | 설명 |
|------|---------------------------------------------------|
| **소문자 사용** | `class="button-primary"`|
| **단어 구분은 `-`(하이픈) 사용** | `class="main-header"`  |
| **아이디는 특수한 경우에만 사용** | `id="user-profile"` (✔) - 특정 요소에만 적용 |
| **의미를 알기 쉽게 작성** | `class="btn-submit"` |
| **BEM(Block Element Modifier) 방식 권장** | `block__element--modifier` |

### 3-2. BEM(Block Element Modifier) 네이밍 규칙

| 네이밍 | 설명 | 예제 |
|--------|----------------------------------|---------------------|
| **Block (`block`)** | 재사용 가능한 독립적인 요소 | `.button {}` |
| **Element (`block__element`)** | Block 내부의 구성 요소 | `.button__icon {}` |
| **Modifier (`block--modifier`)** | Block 또는 Element의 변형 | `.button--primary {}` |

**📌 예제**
```html
<div class="card">
    <h2 class="card__title">제목</h2>
    <p class="card__description">설명</p>
    <button class="card__button card__button--active">클릭</button>
</div>