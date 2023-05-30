# 1. 이슈 생성

1. github Issues 탭에 가기
  
2. 우측 New issue 버튼 클릭
  
3. 문제 상황에 맞게 Get started 클릭
  
4. 이슈 생성
  

# 2. 작업 환경 setting

1. repo 상단의 Fork 버튼으로 Fork 생성
  
2. vscode에서 fork한 repo를 clone
  
  * git clone {fork한 repo url}
    
3. 환경 세팅Visual Studio Code에서 깃헙계정 로그인 후 터미널에 아래와 같이 명령어 입력 (최초 1회만 수행)
  
  1. upstream remote 추가
    
    * git remote add upstream https://github.com/dustjr1565/intern.git
      
  2. pre-commit setting
    
    * pip install pre-commit
      
    * pre-commit install
      
  

# 3. 분기 생성

1. 작업 branch 생성
  
  터미널에 아래의 명령어 입력
  
  * git checkout upstream/dev
    
  * git checkout -b {your branch name}
    
2. 코드 구현 후 좌측 source control 탭을 통해서 gui상으로 쉽게 commit 가능
  
  1. chages 목록에서 변경할 파일들 + 버튼 클릭
    
  2. message에 간단하게 작업내용 적고 commit 버튼 클릭
    
    * 이때 pre-commit의 설정에 맞지 않으면 commit이 안되거나 내용이 변경됨
      
    * pre-commit의 설정에 맞게 수정하여 다시 commit을 하면 됨
      
3. push
  
  터미널에 아래의 명령어 입력
  
  * git push origin {your branch name}
    

# 4. PR

* push를 날린 후 github의 Pull requests 탭에서 PR를 보내면 됨.
  
  * 꼭 dev branch 로 보내기
    
    * base repository : dev <- {fork한 레포}: {작업한 branch 명}
      
* 리뷰어에 dustjr1565 추가
  
  * 추후 회사에서 작업할 시는 zeroact(희재님) 까지 추가하시면 됩니다.
