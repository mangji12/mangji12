# Git Flow

- Git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략을 의마한다.
- 가장 대표적으로 활용되는 전략은 다음과 같다.
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled.png)
    

| branch | 주요 특징 | 예시 |
| --- | --- | --- |
| master
(main) | 배포 가능한 상태의 코드 | LOL 클라이언트 라이브 버전(9.23.231.1231) |
| develop
(main) | - feature branch로 나뉘어지거나, 발생된 버그 수정 등 개발 진행
- 개발 이후 release branch로 분기 | 다음 패치를 위한 개발(9.24) |
| feature branches | - 기능별 개발 브랜치(topic branch)
- 기능이 반영되거나 드랍되는 경우 브랜치 삭제 | 개발시 기능별
예)챔피언, 몬스터 등 |
| release branches | 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 minor bug fix 등 반영 | 9.24a,0.24b |
| hotfixes | - 긴급하게 반영 해야하는 bug fix
- release branch는 다음 버전을 위한 것이라면, hotfix branch는 현재 버전을 위한것 | 긴급 패치를 위한 작업 |

**GitHub Flow 기본 원칙**

- Github Flow는 Github에서 제안하는 브랜치 전략으로 다음과 같은 기본 원칙을 가지고 있다.
    1. master branch는 반드시 배포 가능한 상태여야 한다.
    2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
    3. Commit message는 매우 중요하며, 명확하게 작성한다.
    4. Pull Request를 통해 협업을 진행한다.
    5. 변경사항을 반영하고 싶다면, master branch에 병합한다.
    

**GitHub Flow Models**

- 앞서 설명된 기본 원칙 아래 Github에서 제시하는 방법이 2가지가 있다.
    - shared Repository Model
    - Fork & Pull Model

**Shared Repository Model**

- Shared Repository Model은 동일한 저장소를 공유하여 활용하는 방식
- 예시는 작업 흐름을 master + feture 브랜치로 구성하여 진행합니다.
- 🧙‍♀️ : repository owner (project manager)
🧟‍♂️ : collaborator

---

### 팀원 초대 및 저장소 Clone

1. 팀원 초대 및 저장소 clone
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%201.png)
    

1. 이메일을 통한 초대 수락
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%202.png)
    
2. Clone 이후 작업에 맞춘 작업환경 설정을 마무리 한다.
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%203.png)
    

---

### 브랜치에서 작업 및 GitHub Push

1. 브랜치에서 작업 및 GitHub Push
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%204.png)
    
2. Commit으로 작업의 이력(history)을 남긴다.
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%205.png)
    
3. 완성된 코드는 원격 저장소에 push를 한다.
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%206.png)
    

---

### Pull Request 생성

1. Github에 들어가서 Pull Request 버튼을 누른다.
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%207.png)
    

1. PR과 관련된 설정을 진행한 후 요청을 생성한다.
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%208.png)
    

---

### Review 및 Merge

1. 작성된 코드를 확인 후 병합
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%209.png)
    
    병합 확인
    

**병합 완료 후 개발을 한다면?**

1. 다음 작업 준비
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%2010.png)
    

---

### Fork & Pull Request Model

1. Fork & Clone
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%2011.png)
    
2. Clone을 하고 각 작업에 맞춘 작업 환격 설정을 마무리 한다.
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%2012.png)
    

**이후 작업(커밋,push,PR)은 Shared Repository Model과 동일함**

---

### while True : but, upstream

- 다음 작업 준비
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%2013.png)
    

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%20Flow/Git%20Flow/Untitled%2014.png)

**커밋 메세지를 잘못 넣었을 때**

→ `git commit —amend <잘못 커밋한 파일 이름>`

→ 이미 push 한 이후로 변경하게 되면 push confilct가 난다.

→ 되돌리는 행위는 push 이후에는 하지 말자
