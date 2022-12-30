# Git 기초, GIt의 흐름

**분산버전 관리 시스템(DVCS)**

- 중앙집중식 버전관리 시스템
    - 로컬에서는 파일을 편집하고 서버에 반영
    - 중앙 서버에서만 버전을 관리
- 분산버전 관리 시스템(git)
    - 로컬에서도 버전을 기록하고 관리
    - 원격 저장소를 활용하여 협업

1. git add 보고서 .md
2. git coommit -m “버전 이름”

<aside>
💡 1. 작업을 하고
2 변경된 파일을 모아(add)
3.버전으로 남긴다. (commit)

</aside>

**버전을 기록하기 전에 항상 해야하는 것?**

Git 버전관리 기초 흐름

Git은 파일을 modified,staged,committed로 관리

- modified : 파일이 수저오딘 상태 (add 명령어를 통하여 staging area로)
- staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소)
- committed : 커밋이 된 상태

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled.png)

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%201.png)

**기본 명령어**

1. `git add <file>`
- working directory 상의 변경 내용을 staging area에 추가하기 위해 사용
    - untracked 상태의 파일을 staged로 변경
    - modified 상태의 파일을 staged로 변경
    
2. `git commit -m ‘<커밋메시지>’` 
- staged 상태의 파일들을 커밋을 통해 버전으로 기록 
- SHA-1 해시를 사용하여 40자 길이의 체크섬을 생성하여 고유한 커밋을 표기
- 커밋 메시지는 변경사항을 나타낼 수 있도록 명확하게 작성해야

git의 버전 관리

- git은 데이터를 파일 시스템의 스냅샷으로 관리하고 매우 크기가 작음
- 파일이 달라지지 않으면 성능을 위해 파일을 새로 저장하지 않음
- 기존의 데타 기반 버전 관리시스템과 가장 큰 차이를 가

현재 상태를 알고 싶을 때

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%202.png)

`git log`

- 현재 저장소에 기록된 커밋을 조회
- 다양한 옵션을 통해 로그를 조회할 수 있음
    - git log -1
    - git log —oneline
    - git log -2 —oneline

`git status` - 작업 완료 후 status

- git 저장소에 있는 파일의 상태를 확인하기 위하여 활용
    - 파일의 상태를 알 수 있음
- Noting to commit,working tree clean

## 실습

- `git init` - git 저장소 만들기

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%203.png)

(master) 구문이 추가된 것을 확인할 수 있다. 맥은 확인 안됨

- `touch`로 파일 만들어 보기
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%204.png)
    

- `git add` 로 변경된 파일 모으기

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%205.png)

- `git status` 로 상태 확인

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%206.png)

No commits yet : 아직 커밋되지 않음.

- `git commit -m ‘버전 이름’`

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%207.png)

- 계정정보가 등록되지 않아 해당 문구가 노출된다.

- 사용자 정보 등록
    - `git config —global [user.email](http://user.email) “이메일”`
    - `git config —global [user.name](http://user.name) “이름”`
    
    등록 후 커밋 화면 확인
    
    ![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%208.png)
    
    커밋한 계정 확인
    
    `git config --global -l`
    
    수정하고 싶으면 같은 명령어로 덮어쓰기
    

**파일 관리 상태 라이프 사이클** 

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%209.png)

![Untitled](https://github.com/mangji12/mangji12/blob/master/GIt%26github/Git%EA%B8%B0%EC%B4%88%2C%20Git%EC%9D%98%20%ED%9D%90%EB%A6%84/Git%20%EA%B8%B0%EC%B4%88%2C%20GIt%EC%9D%98%20%ED%9D%90%EB%A6%84/Untitled%2010.png)

변경사항이 생겼고, 버전으로 기록하고 싶다면 `add`, `commit`. 커밋까지 된 정보를 볼때 `log`.
