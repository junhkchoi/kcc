# KCC 동아리 홈페이지 제작

국민대학교 KCC 학술동아리의 공식 홈페이지 제작 프로젝트 레포입니다.  
프로젝트의 주요 목적은 **동아리 소개**와 **랭킹 시스템**입니다.  
추가로 "post" 앱은 **방명록 기능**으로 운영됩니다.

---

## 프로젝트 개요

### 주요 기능
- **home:** 동아리 소개 및 기본 홈페이지, 네비게이션 제공
- **ranking:** 출석, 과제, 참여 점수를 관리하는 랭킹 시스템
- **post:** 방문자들이 메시지를 남길 수 있는 방명록 기능

### 개발 순서
Design ➡️ Home ➡️ Post ➡️ Ranking ➡️ Deploy

---

## 기술 스텍

<div align="center">

### FrontEnd  
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />

### BackEnd
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />

### DataBase  
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />

## Deploy Architecture

</div>

## Deploy Architecture
<img width="835" alt="architecture" src="https://github.com/user-attachments/assets/bd375239-e97b-44c1-ad4d-48a1ef828e80" />


---

## 커밋 컨벤션

| **타입**   | **설명**                                           | **예시** |
|------------|--------------------------------------------------|----------|
| **feat**   | 새로운 기능 추가                                 | `feat: 로그인 기능 추가` |
| **fix**    | 버그 수정                                       | `fix: 회원가입 시 비밀번호 검증 오류 수정` |
| **docs**   | 문서 추가 및 수정 (README, 문서 수정 등)        | `docs: README.md 업데이트` |
| **style**  | 코드 스타일 변경 (포맷팅, 세미콜론 추가 등)    | `style: 코드 포맷 정리` |
| **refactor** | 기능 변경 없이 코드 구조 개선                 | `refactor: CSS 클래스 구조 개선` |
| **perf**   | 성능 개선                                       | `perf: 이미지 로딩 최적화` |
| **test**   | 테스트 코드 추가 또는 수정                      | `test: API 테스트 추가` |
| **chore**  | 기타 변경 사항 (빌드 설정, 패키지 매니저 설정) | `chore: ESLint 설정 업데이트` |
| **ci**     | CI/CD 관련 설정 수정                            | `ci: GitHub Actions 수정` |

---

## BEM 네이밍 방법론

| **요소**   | **설명**                                           | **예시** |
|------------|--------------------------------------------------|----------|
| **Block**  | 독립적인 UI 요소 (큰 단위)                        | `.card {}` |
| **Element** | Block 내부의 구성 요소                           | `.card__title {}` |
| **Modifier** | Block 또는 Element의 변형                        | `.card__button--active {}` |

---

## 🛠 BEM 네이밍 예제

```html
<div class="card">
    <h2 class="card__title">제목</h2>
    <p class="card__description">설명</p>
    <button class="card__button card__button--active">클릭</button>
</div>
