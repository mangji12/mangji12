# 안녕하세요, 견고한 백엔드를 설계하는 개발자 오창인입니다.

**Python (Django, FastAPI)** 생태계를 주력으로 다루며, 단순히 기능이 동작하는 것을 넘어 **'서비스가 실제 운영 환경에서 안전하고 효율적으로 돌아가는지'**를 고민합니다.

AI 전공을 통해 데이터의 흐름을 익혔고, 시스템 해킹(Pwnable) 학습을 통해 메모리와 프로세스의 작동 원리를 깊이 이해했습니다. 이러한 로우 레벨(Low-level) 지식을 바탕으로, **보안 취약점을 사전에 차단하고 성능을 고려한 코드**를 작성하는 것을 지향합니다.

<a href="https://kukurubbing.tistory.com/" target="_blank"><img src="https://img.shields.io/badge/Blog-EB531F?style=for-the-badge&logo=Tistory&logoColor=white"/></a>
<a href="https://qwerty12.notion.site" target="_blank"><img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/chvn9in/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:dhckddls12@naver.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.threads.net/@chvn9in" target="_blank"><img src="https://img.shields.io/badge/Threads-000000?style=for-the-badge&logo=threads&logoColor=white" alt="Threads"/></a>

<br/>

### 📌 Focus & Philosophy

**1. 배포 및 운영 자동화 (DevOps)**
- 코드는 배포되어야 비로소 가치를 가진다고 믿습니다. `FastAPI`와 `React` 서비스를 **AWS EC2** 에 직접 배포하고 운영해 본 경험이 있습니다.
- **Jenkins** CI/CD 파이프라인을 구축하여, 반복적인 배포 과정을 자동화하고 개발 생산성을 높이는 데 집중합니다.

**2. 보안을 고려한 아키텍처 (Security Awareness)**
- 웹 해킹과 **포너블(Pwnable)** 을 학습하며 스택/힙 메모리 구조와 취약점의 발생 원리를 파악했습니다.
- 프레임워크가 제공하는 기능에만 의존하지 않고, 공격자의 관점에서 시스템을 바라보며 **방어적인 설계(Defensive Programming)** 를 지향합니다.

**3. 데이터 가치 창출 (Data Engineering)**
- 비정형 공공데이터(한국소비자원 리포트)를 수집·가공하여 사용자에게 유의미한 정보로 변환하는 서비스를 개발 중입니다.
- 데이터의 구조적 한계를 해결하기 위해 **Hybrid DB 설계(RDBMS + NoSQL)** 를 도입하는 등 기술적 문제 해결을 즐깁니다.

<br/>

### 🛠 Tech Stack

**Languages**
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white">

**Backend**
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white">

**Infra & DevOps**
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white"> <img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">

**Database**
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">

<br/>

### 🚀 Featured Projects

**1. 한국소비자원 리포트 플랫폼 (KCA Report Platform)**
> *공공데이터 기반 합리적 소비 분석 플랫폼*
- **Role:** 1인 개발 (기획, 백엔드, DB 설계)
- **Key Tech:** `Django` `PostgreSQL` `JSONField` `Custom Admin`
- **Description:** 정형/비정형 데이터가 섞인 리포트 특성을 고려해 **Hybrid Schema** 를 설계하고, 운영 효율을 위해 Django Admin을 고도화했습니다.

**2. 실시간 랜덤 채팅 (Real-time Random Chat)**
> *비동기 통신 기반 익명 채팅 서비스*
- **Role:** 백엔드 리드, CI/CD 구축
- **Key Tech:** `FastAPI` `WebSocket` `Jenkins` `AWS EC2`
- **Description:** WebSocket을 활용해 저지연 양방향 통신을 구현했으며, Jenkins 파이프라인을 구축하여 **무중단 배포** 환경을 마련했습니다.

**3. C언어 포켓몬 게임 **
> *CS 기초 함양을 위한 자료구조 구현*
- **Role:** C 프로그래밍, 자료구조 설계
- **Key Tech:** `C` `Pointer` `Linked List` `Memory Management`
- **Description:** **포너블 학습의 기초** 를 다지기 위해 진행했습니다. 구조체와 동적 메모리 할당(malloc/free)을 직접 관리하며 **메모리 누수(Leak) 없는 안전한 코드** 작성을 훈련했습니다.
