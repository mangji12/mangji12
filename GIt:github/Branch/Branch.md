# Branch

![git의 작업 흐릅.png](Branch%208fcc4fbb19c243568116704b18d633ef/git%25EC%259D%2598_%25EC%259E%2591%25EC%2597%2585_%25ED%259D%2590%25EB%25A6%2585.png)

![Untitled](Branch%208fcc4fbb19c243568116704b18d633ef/Untitled.png)

- 독립적인 작업 흐름을 만들고 관리할 수 있다.
    
    ![Untitled](Branch%208fcc4fbb19c243568116704b18d633ef/Untitled%201.png)
    

**브랜치 주요 명령어**

```bash
1. 브랜치 생성
		git branch <브랜치 이름>
		* -b 옵션을 추가하면 생성과 동시에 브랜치 이동까지 하게 된다. (없으면 생성)
2. 브랜치 이동
		git checkout <브랜치 이름>
3. 브랜치 생성 및 이동 
		git branch -b <브랜치 이름>
4. 브랜치 목록
		git branch
5. 브랜치 삭제
		git branch d <브랜치 이름>
```

**merge**

- 각 브랜치에서 작업을 한 이후 이력을 합치기 위해 `merge` 명령어를 사용
- 병합을 진행할 때, 서로 다른 이력(commit)에서
    - 동일한 파일을 수정한 경우 → 충돌 발생
        - 이 경우, 반드시 직접 해당 파일을 확인하고 적절하게 수정
        - 수정한 이후에 직접 커밋 실행
    - 다른 파일을 수정한 경우
        - 충돌 없이 자동으로  Merge Commit이 생성됨

1) merge - fast forward

- 기존 master 브랜치에 변경사항이 없어 단순히 앞으로 이동
    
    ![Untitled](Branch%208fcc4fbb19c243568116704b18d633ef/Untitled%202.png)
    

2) merge -merge commit

![Untitled](Branch%208fcc4fbb19c243568116704b18d633ef/Untitled%203.png)

**브랜치 병합 시나리오**

- 브랜치 관련된 명령어는 간단하다.
    - 다양한 시나리오 속에서 어떤 상황인지 파악하고 자유롭게 활용할 수 있어야 한다.

**상황 1. fast-foward**

- fast-foward는 feature 브랜치가 생성된 이후 master 브랜치에 변경상황이 없는 상황

```bash
1. feature/home branch 생성 및 이동

   ```bash
		git branch -b feature/home
   ```

2. 작업 완료 후 commit

   ```bash
   (feature/home) $ touch home.txt
   (feature/home) $ git add .
   (feature/home) $ git commit -m 'Add home.txt'
   ```

3. master 이동

   ```bash
		git checkout master
   ```

4. master에 병합

   ```bash
		git merge feature/home
   ```

5. 결과 : fast-foward
		```bash
   (master) $ git log --oneline
   b534a34 (HEAD -> master, feature/home) Complete Home!!!!
   e89616a Init
		```
   
6. branch 삭제

   ```bash
		git branch -d feature/home
   ```
```

**상황 2. merge commit**

- 서로 다른 이력(commit)을 병합 하는 과정에서 **다른 파일이 수정** 되어 있는 상황
    - git이 auto merging을 진행하고 **commit이 발생한다**
    
    ```bash
    1. feature/about branch 생성 및 이동
    
       ```bash
    		git branch -b feature/about branch
       ```
    
    2. 작업 완료 후 commit
    
       ```bash
       (feature/about) $ touch about.txt
       (feature/about) $ git add .
       (feature/about) $ git commit -m 'Add about.txt'
       ```
    
    3. master 이동
    
       ```bash
    		git checkout master
       ```
      
    4. master에 추가 commit 발생시키기
    
    	  - 다른 파일을 수정 혹은 생성하기
    
       ```bash
       (master) $ touch master.txt
       (master) $ git add .
       (master) $ git commit -m 'Add master.txt'
       ```
       
    
    5. master에 병합
    
       ```bash
    		git merge feature/about
       ```
    
    6. 결과 -> 자동으로 *merge commit 발생*
    
       * vim 편집기 화면이 나타납니다. 
    
         * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
           * `w` : write
           * `q` : quit
    
    7. 커밋 및 그래프 확인하기
    
       ```bash
       $ git log --onelie --graph
       ```
    
    8. branch 삭제
    
       ```bash
    		git branch -d feature/about
       ```
    ```
    

**상황 3. merge commit 충돌**

[git Conflict(충돌)는 왜 일어날까? 과정 알아보기](https://chaeyoung2.tistory.com/61)

- 서로 다른 이력(commit)을 병합(merge)하는 과정에서 **같은 파일의 동일한 부분이 수정**되어 있는 상황
    - git이 auto merging을 하지 못하고, 충돌 메시지가 뜬다.
    - 해당 파일의 위치에 표준형식에 따라 표시 해준다.
    - 원하는 형태의 코드로 직접 수정을 하고 직접 commit을 발생 시켜야 한다.
    
    ```bash
    1. feature/test branch 생성 및 이동
    
       ```bash
    		git checkout -b feature/test
       ```
       
    2. 작업 완료 후 commit
    
       ```bash
       # README.md 파일 열어서 수정
       (feature/test) $ touch test.txt
       (feature/test) $ git add .
       (feature/test) $ git commit -m 'Add test.txt'
    	 95fad1c (HEAD -> feature/test) README 수정하고 test 작성하고
       582902d (master) **Merge branch** 'feature/about'
       98c5528 마스터 작업....
       5e1f6de 자기소개 페이지 완료!
       b534a34 Complete Home!!!!
       e89616a Init
       ```
    
    3. master 이동
    
       ```bash
    		git checkout master
       ```
       
    4. master에 추가 commit 발생시키기
    
       - 동일 파일을 수정 혹은 생성하기
    
       ```bash
       # README.md 파일 열어서 수정
       (master) $ git add README.md
       (master) $ git commit -m 'Update README.md'
       ```
    
    5. master에 병합
    
       ```bash
    		git merge feature/test
       ```
       
    6. 결과 -> *merge conflict발생*
    
       > git status 명령어로 충돌 파일을 확인할 수 있음.
    		```bash
    		(master|MERGING) $ git status
       On branch master
       You have unmerged paths.
         (fix conflicts and run "git commit")        
         (use "git merge --abort" to abort the merge)
       
       Changes to be committed:
               new file:   test-1.txt
               new file:   test-2.txt
               new file:   test.txt
       
       Unmerged paths:
         (use "git add <file>..." to mark resolution)
               both modified:   README.md
    		```
    
    7. 충돌 확인 및 해결
      ```
       <<<<<<< HEAD
       # 마스터에서 작업함...
       =======
       # 테스트에서 작성
       >>>>>>> feature/test
       ```
    
    8. merge commit 진행
    
       ```bash
    	   git add .
    	   git commit
       ```
    
       * vim 편집기 화면이 나타납니다.
    
         * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
    
         * `w` : write
    
         * `q` : quit
    
    9. 커밋 및 확인하기
    
       ```bash
       $ git log --oneline --graph
       ```
    
    10. branch 삭제
    
        ```bash
    			git branch -d feature/test
        ```
    ```