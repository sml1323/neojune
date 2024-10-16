FROM namugach/ubuntu-basic:24.04-kor
WORKDIR /root

RUN apt-get install -y software-properties-common \
&& add-apt-repository ppa:ondrej/php \
&& apt-get update \
&& apt-get install -y apache2 mysql-server php8.3

# apahe local 설정
# /etc/apache2/apache2.conf 파일 마지막에 ServerName localhost 문자열 추가
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf


#### 여기부터 SSH 
RUN mkdir /var/run/sshd

# root password 변경, $PASSWORD를 변경한다.
RUN echo 'root:$PASSWORD' |  chpasswd

# ssh 설정 변경
# root 계정으로의 로그인을 허용한다. 아래 명령을 추가하지 않으면 root 계정으로 로그인이 불가능하다. 
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
# 응용 프로그램이 password 파일을 읽어 오는 대신 PAM이 직접 인증을 수행 하도록 하는 PAM 인증을 활성화
# RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN sed -ri 's/^#Port 22/Port 22/' /etc/ssh/sshd_config

RUN sed -ri 's/^#ListenAddress 0.0.0.0/ListenAddress 0.0.0.0/' /etc/ssh/sshd_config



# SSH 키 생성
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -q -N ""

# SSH 설정
RUN mkdir -p /root/.ssh && \
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/authorized_keys && \
    chmod 700 /root/.ssh

# ssh 최초 접속시 yes 생략
RUN echo "Host server*\n \
 StrictHostKeyChecking no\n \
 UserKnownHostsFile=/dev/null" >> /root/.ssh/config


# MySQL 초기화 설정
RUN chown -R mysql:mysql /var/run/mysqld
RUN chmod 755 /var/run/mysqld

RUN sed -ri 's/^#.+port.+= 3306/port = 3306/' /etc/mysql/mysql.conf.d/mysqld.cnf
RUN sed -ri 's/^bind-address.+= 127.0.0.1/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf

RUN service mysql start && \
    mysql -e "CREATE DATABASE IF NOT EXISTS mydatabase; \
    CREATE USER 'ubuntu'@'%' IDENTIFIED BY '1234'; \
    GRANT ALL PRIVILEGES ON *.* TO 'ubuntu'@'%' WITH GRANT OPTION; \
    FLUSH PRIVILEGES;"

RUN echo "[mysqld]\n \
    character-set-server=utf8\n \
    collation-server=utf8_general_ci\n \
    \n \
    [client]\n \
    default-character-set=utf8\n \
    \n \
    [mysql]\n \
    default-character-set=utf8" >> /etc/mysql/mysql.conf.d/mysqld.cnf
    


# apahe, SSH, MySQL 동시에 실행하기 위한 커맨드
CMD [ \
  "/bin/bash", "-c", \
  "service apache2 start && service mysql start && /usr/sbin/sshd -D" \
]