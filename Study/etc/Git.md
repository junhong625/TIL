## Git(분산 버전 관리 프로그램)

- 코드의 히스토리(버전)을 관리하는 도구
- 개발되어온 과정 파악 가능
- 이전 버전과의 변경사항 비교 및 분석
- 효과적인 버전관리를 위해 사용(ex : google docs)
- 날짜를 통해 변경일자 기록 가능
    - Git이 변경사항을 기록해줌
- 맨 나중 파일과, 이전 변경사한만 남겨 효율적으로 파일 관리
<br>

## Github

- 포트폴리오 용도로 사용( 🌱 심기)
- 개발자의 SNS💬
<br>

## Git 기본기

- **README.md**
    - 프로젝트에 대한 설명 문서
    - Github 프로젝트에서 가장 먼저 보는 문서
    - 일반적으로 소프트웨어와 함께 배포
    - 작성 형식은 따로 없으나, 일반적으로 마크다운을 이용해 작성
    
- **Repository** : 특정 디렉토리를 버전 관리하는 저장소
    - **git init** 명령어로 로컬 저장소를 생성(`.git/` 이라는 숨김 디렉토리 생성)
        - **루트 디렉토리 or Home 폴더에서 절대 사용 금지!!**
    - git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음
    
- README.MD
    - 새 폴더를 만들고 [README.md](http://README.md) 파일을 생성해 주세요.
    - 이 파일을 버전 관리하며 Git을 사용해 봅시다.
        - 특정 버전으로 남긴다 = 커밋(`Commit`)한다.(3가지 영역을 바탕으로 동작)
            1. `Working Directory` - 내가 작업하고 있는 실제 디렉토리 
                - 파일 위치 상태 - `untracked` → 수정 될 경우 - `modified`
                - `git add` → `Staging Area`
            2. `Staging Area` - 커밋(`Commit`)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
                - 파일 위치 상태 - `staged`
                - `git commit` → `Repostiory`
                    - `git commit -m(message를 의미) ‘남길 message’`
            3. `Repository` - 커밋(`Commit`)들이 저장되는 곳
                - 파일 위치 상태 - `committed`
<br>

## **.gitignore**

- 민감한 정보를 보호하기 위해 사용
- `Repository` 생성 후 가장 먼저 생성해줘야 하는 것
- [[toptal]](https://www.notion.so/%5B%5D()) 사이트를 통해 운영체제, 개발환경, 언어에 맞는 gitignore 생성 가능
- `.gitignore`에 디렉토리, 파일 경로를 저장해 보호
- **git이 한 번 관리하기 시작한 파일은 gitignore로 보호할 수가 없다.**
<br>

## Git 명령어

- **git init** : 명령어로 로컬 저장소를 생성(`.git/` 이라는 숨김 디렉토리 생성)
- **git config —global [user.email](http://user.email) “exam@exam.com”** : 이메일 설정
- **git config —global [user.name](http://user.name) “hong-gil-dong”** : 이름 설정
- **git status** : 상태 창 확인
- **git add <파일명 or . >** : `Staging area`에 올려 `staged` 상태로 변환
- **git commit -m “남길 message”** : `commit`을 통해 github에 올리기
- **git log —oneline** : git commit history 한줄로 간단하게 보기
- **git diff** : 두 `commit`의 차이 보기
<br>

## **Remote Repository 연결하기**

### **Github**

1. 기본 브랜치 이름 `master`로 변경하기
2. `new Repo` 생성 버튼 클릭
    1. 이름 설정
    2. 만들기!

### **Local**

1. 새로운 디렉토리 생성 :
    1. `mkdir(make directory)`
    2. `cd(change directory)`
    3. `git init`
    4. `git remote add origin(repo 별명) {생성한 remote_repo의 url}`
    5. `git remote` : origin 이름으로 remote 된 것 확인
    6. `touch README.md`
2. 버전 남기기
    1. `git add` (파일명.확장자)
        - `git add .` (pwd에 위치한 모든 수정 사항)
    2. `git commit -m "남길 message"`
3. `git push origin master`
    - `git push -u origin master`
        - `git push`
<br>

## **협업과 복구 및 백업**

### **원격 저장소 연결**

1. github에 원격 저장소를 생성합니다.
2. 로컬 저장소(`Repository`) 생성합니다.
3. **원격 저장소에 Push 하기 전에 반드시 최소 하나 이상의 Commit을 가져야한다.**
<br>

### **원격 저장소 연결 명령어**

1. `git remote add origin (Repository url)`
2. `git remote -v` : origin(url) : 등록한 Remote Repository 정보 확인
3. `git push -u origin master` : 로컬에서 생긴 커밋 내역을 업로드
    - `git push`
4. `git pull origin master` : 원격 저장소의 변화 사항을 다운로드
5. `git clone (gir Repository url)` : 원격 저장소를 복제해온다. (원격 → 로컬) : 다운로드
<br>

### Pull과 Clone

- `Coflict` 상황을 방지하기 위해 **push 이전에 pull은 필수**
<br>

## GUI(Graphic User Interface) & CLI(Command-Line Interface)

- **GUI**
    - 그래픽을 통해 사용자와 컴퓨터가 상호 작용
- **CLI**
    - 명령어를 통해 사용자와 컴퓨터가 상호 작용
<br>
    
## Why CLI

- `GUI`는 `CLI`에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모
- 수 많은 서버/개발 시스템이 `CLI`를 통한 조작 환경을 제공
<br>

## LINUX 명령어

| touch | 파일을 생성 |
| --- | --- |
| mkdir | 폴더를 생성 |
| ls | 현재 작업중인 디렉토리의 폴더/파일 목록을 보여주는 |
| ls -a | 숨겨진 파일까지 모두 보여주는 명령어 |
| ls -l | 파일을 열로 정렬하여 보여주는 명령어 |
| cd | 현재 작업중인 디렉토리를 변경 |
| pwd | 현재 작업중인 디렉토리의 절대 경로 |
| rm | 파일을 삭제
-r 을 추가하면 폴더 삭제 |