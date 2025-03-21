# KCC 동아리 홈페이지 제작

KCC 동아리의 공식 홈페이지를 제작하는 프로젝트입니다.  
이 프로젝트의 주요 목적은 **동아리 소개**와 **랭킹 시스템**입니다.  
추가로 "post" 앱은 **방명록 기능**으로 운영됩니다.

---

## 프로젝트 개요

### 주요 기능
- **home:** 동아리 소개 및 기본 홈페이지, 네비게이션 제공
- **ranking:** 출석, 과제, 참여 점수를 관리하는 랭킹 시스템
- **post:** 방문자들이 메시지를 남길 수 있는 방명록 기능

### 개발 순서
Design ➡️ Home ➡️ Post (방명록) ➡️ Ranking ➡️ Deploy

---

## 사용 기술

| 분야       | 기술 스택                          |
|------------|------------------------------------|
| **Frontend** | HTML, CSS, JavaScript             |
| **Backend**  | Django, Python                    |
| **Database** | SQLite (개발), PostgreSQL (배포)  |
| **Deployment** | AWS EC2, Nginx, Gunicorn         |

---

## 설치 및 실행 방법

1. **프로젝트 클론**
   ```bash
   git clone https://github.com/your-repo/kcc-homepage.git
   cd kcc-homepage