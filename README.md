## Ubuntu 24.04 기반 LEMP 스택 개발 환경 (SSH 포함)

### 개요

이 Docker 이미지는 Ubuntu 24.04 (한국어 지원)를 기반으로 Nginx 웹 서버, MySQL 데이터베이스, SSH 서버를 포함하는 LEMP 스택 개발 환경을 제공합니다. 

### 주요 기능

* 웹 개발 필수 요소: Nginx, MySQL 기본 설치
* 한국어 지원: 한국어 로케일 및 글꼴 포함
* 원격 접속: SSH 서버를 통해 안전하게 컨테이너에 접속 및 관리 가능

### 설치 방법

1. Docker 이미지 빌드:

```bash
docker build -t ubuntu-neojune:24.04-kor-amp
```

2. Docker 컨테이너 실행:

```bash
docker run -d -p 8080:80 --name neojune ubuntu-neojune:24.04-kor-amp
```

- `-p 8080:80`: 호스트 시스템의 8080번 포트를 컨테이너의 80번 포트로 연결 (웹 서버 접속)

- `-p 3306:3306`: 호스트 시스템의 3306번 포트를 컨테이너의 3306번 포트로 연결 (MySQL 접속)
- `-p 22:22`: 호스트 시스템의 22번 포트를 컨테이너의 22번 포트로 연결 (SSH 접속)


### 사용 방법

* 웹 서버 접속: 브라우저에서 `http://localhost:8080` 로 접속합니다. 
* MySQL 접속:
- 호스트 시스템에서 MySQL 클라이언트를 사용하여 `localhost:3306`에 접속합니다.
- 사용자 이름: `ubuntu`, 비밀번호: `1234`
* SSH 접속: 터미널에서 `ssh root@localhost` 명령어를 사용하여 SSH로 접속합니다.
- 비밀번호: Dockerfile에서 설정한 `$PASSWORD` (Dockerfile 내 `echo 'root:$PASSWORD' | chpasswd` 부분에서 `$PASSWORD`를 원하는 비밀번호로 변경해야 합니다.)

### 환경 설정

* root 비밀번호: Dockerfile에서 `$PASSWORD`를 원하는 비밀번호로 변경합니다.
* MySQL 데이터베이스:  `mydatabase` 데이터베이스가 기본적으로 생성됩니다. 필요에 따라 추가 데이터베이스를 생성할 수 있습니다.
* MySQL 사용자:  `ubuntu` 사용자가 모든 권한을 가지고 생성됩니다. 필요에 따라 사용자를 추가하거나 권한을 수정할 수 있습니다.

### 추가 정보

* SSH 키 기반 인증:  Dockerfile에서 생성된 SSH 키를 사용하여 비밀번호 없이 SSH 접속을 설정할 수 있습니다.
* Nginx 설정: `/etc/nginx` 디렉토리에서 Nginx 설정 파일을 수정할 수 있습니다.
* MySQL 설정: `/etc/mysql/mysql.conf.d/mysqld.cnf` 파일에서 MySQL 설정을 변경할 수 있습니다.

### 라이선스

MIT License 