# 오창인 | Backend Engineer

> **AI 모델을 운영 가능한 서비스로 만드는 개발자입니다.**  
> Django/FastAPI로 실제 사용자를 위한 프로덕션 서비스를 만들고,  
> Jenkins CI/CD로 배포 프로세스를 자동화합니다.

<a href="https://www.wise-pick.co.kr" target="_blank"><img src="https://img.shields.io/badge/🌐_Live_Service-와이즈픽-4A90E2?style=for-the-badge"/></a>
<a href="https://kukurubbing.tistory.com/" target="_blank"><img src="https://img.shields.io/badge/Blog-EB531F?style=for-the-badge&logo=Tistory&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/chvn9in/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:dhckddls12@naver.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>

-----

## 🏆 Featured Projects

### 1️⃣ 와이즈픽 - 합리적 소비 분석 플랫폼

> **[🔗 서비스 바로가기](https://www.wise-pick.co.kr)** | 한국소비자원 공공데이터 기반 제품 비교 서비스

**Tech Stack:** `Django` `PostgreSQL (JSONB)` `Docker Compose` `Nginx`

**핵심 구현 내용:**

- 📊 **1,200+ 개 소비자 리포트 데이터 수집 및 정제**
- 🔧 **PostgreSQL JSONB 활용**, 리포트별 상이한 필드 구조 대응
  - 마이그레이션 없이 신규 리포트 타입 추가 가능 (개발 시간 70% 단축)
- ⚡ **검색 API 평균 응답속도 200ms** 이하 달성 (JSONB 인덱싱 활용)
- 🎨 Django Admin 커스터마이징으로 비개발자도 데이터 관리 가능

**기술적 의사결정:**

- 정형 DB만으로는 리포트마다 다른 50+ 필드를 관리 불가 → JSONB 하이브리드 스키마 도입
- 비정형 데이터의 검색 성능 문제 → GIN 인덱스 + ORM 쿼리 최적화로 해결

-----

### 2️⃣ 실시간 랜덤 채팅 서비스

> WebSocket 기반 익명 채팅 & Jenkins CI/CD 무중단 배포

**Tech Stack:** `FastAPI` `WebSocket` `Jenkins` `AWS EC2` `Docker`

**핵심 구현 내용:**

- 💬 **WebSocket 양방향 통신**으로 실시간 메시지 전송 (지연 50ms 이하)
- 🚀 **Jenkins 파이프라인 구축**
  - GitHub Push → 자동 빌드 → Docker 이미지 생성 → EC2 배포
  - 배포 시간 15분 → 3분으로 단축
- 📈 **3개월간 무장애 운영** (MAU 500+)

**기술적 의사결정:**

- Django Channels 대신 FastAPI 선택 → 비동기 I/O 효율성 (동시접속자 2배↑)
- Blue-Green 배포 전략으로 서비스 중단 시간 0초 달성

-----

### 3️⃣ C언어 포켓몬 게임

> 메모리 관리 훈련을 위한 자료구조 구현 프로젝트

**Tech Stack:** `C` `Linked List` `Dynamic Memory Management`

**학습 목표:**

- ⚙️ Pwnable(System Hacking) 학습 기초 다지기
- 🧠 **메모리 누수 없는 코드 작성** (Valgrind로 검증)
- 📚 포인터/구조체/동적 할당 직접 제어

**구현 내용:**

- 연결 리스트 기반 포켓몬 인벤토리 시스템
- malloc/free 수동 관리로 메모리 최적화
- 스택/힙 메모리 흐름 이해 → 웹 서비스 성능 튜닝 시 활용

-----

## 🛠 Tech Stack

**Backend Framework**  
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)

**Database**  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![JSONB](https://img.shields.io/badge/JSONB-Hybrid_Schema-orange?style=flat)

**DevOps & Infrastructure**  
![AWS](https://img.shields.io/badge/AWS_EC2-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)

**Language**  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat&logo=c&logoColor=black)

-----

## 💡 Development Philosophy

**1. Production-First Mindset**  
코드는 배포되어야 가치가 있습니다. 실제 사용자를 위한 안정적인 서비스를 만듭니다.

**2. Security Awareness**  
Pwnable 학습으로 메모리 취약점을 이해하고, 공격자 관점에서 방어적으로 설계합니다.

**3. Data-Driven Service**  
비정형 공공데이터를 수집·가공하여 사용자에게 유의미한 가치로 전환합니다.

-----

## 📫 Contact

- **Email:** dhckddls12@naver.com
- **Blog:** [kukurubbing.tistory.com](https://kukurubbing.tistory.com/)
- **LinkedIn:** [linkedin.com/in/chvn9in](https://www.linkedin.com/in/chvn9in/)
- **Portfolio:** [qwerty12.notion.site](https://qwerty12.notion.site)

-----

<div align="center">

**“메모리부터 배포까지, 전체 스택을 이해하는 백엔드 엔지니어”**

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fyour-username&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>