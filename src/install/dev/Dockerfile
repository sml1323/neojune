FROM namugach/ubuntu-basic:24.04-kor
WORKDIR /root

# 파일 복사
COPY . /root/work

RUN apt-get update

# Nginx, MySQL 서버, 및 MySQL 개발 라이브러리 설치
RUN apt-get install -y nginx mysql-server pkg-config libmysqlclient-dev

# # Python 라이브러리 설치
RUN pip install -r /root/work/src/install/dev/requirements.txt

RUN /root/work/src/install/dev/setup.sh

# #### 여기부터 SSH 
RUN mkdir /var/run/sshd

# root password 변경, $PASSWORD를 변경한다.
RUN echo 'root:$PASSWORD' |  chpasswd

# ssh 설정 변경
# root 계정으로의 로그인을 허용한다.
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
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

# MySQL 포트 설정 변경
RUN sed -ri 's/^#.+port.+= 3306/port = 3306/' /etc/mysql/mysql.conf.d/mysqld.cnf

# MySQL 바인딩 주소 변경
RUN sed -ri 's/^bind-address.+= 127.0.0.1/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf

# MySQL 서비스 시작 및 데이터베이스 설정
RUN service mysql start && \
    # 데이터베이스 생성 및 사용자 권한 설정
    mysql -e "CREATE DATABASE IF NOT EXISTS kipris; \
    CREATE USER 'ubuntu'@'%' IDENTIFIED BY '1234'; \
    GRANT ALL PRIVILEGES ON *.* TO 'ubuntu'@'%' WITH GRANT OPTION; \
    FLUSH PRIVILEGES;" && \
    # SQL 파일 실행
    mysql -u root kipris < /root/work/res/sql/create_table.sql && \
    mysql -u root kipris < /root/work/res/sql/data/kipris_tb24_100_2024-11-11_211316.sql && \
    mysql -u root kipris < /root/work/res/sql/data/kipris_tb24_200_2024-11-11_211323.sql && \
    mysql -u root kipris < /root/work/res/sql/data/kipris_tb24_110_2024-11-11_211054.sql && \
    mysql -u root kipris < /root/work/res/sql/data/kipris_tb24_210_2024-11-11_211329.sql && \
    # SQL 파일 삭제
    rm -rf /root/work


RUN echo "[mysqld]\n \
    character-set-server=utf8\n \
    collation-server=utf8_general_ci\n \
    \n \
    [client]\n \
    default-character-set=utf8\n \
    \n \
    [mysql]\n \
    default-character-set=utf8" >> /etc/mysql/mysql.conf.d/mysqld.cnf
    


# .bashrc에 메시지 추가
RUN echo "echo \n" >> /root/.bashrc && \
    echo "echo '=================================='" >> /root/.bashrc && \
    echo "echo 'id: admin'" >> /root/.bashrc && \
    echo "echo 'password: admin'" >> /root/.bashrc && \
    echo "echo '=================================='" >> /root/.bashrc && \
    echo "echo 'airflow: http://localhost:8080'" >> /root/.bashrc && \
    echo "echo 'grafana: http://localhost:3000'" >> /root/.bashrc && \
    echo "echo 'prometheus: http://localhost:9090'" >> /root/.bashrc && \
    echo "echo 'pushgateway: http://localhost:9091'" >> /root/.bashrc && \
    echo "echo 'flask: http://localhost:5000'" >> /root/.bashrc && \
    echo "echo 'streamlit: http://localhost:8501'" >> /root/.bashrc && \
    echo "echo '=================================='" >> /root/.bashrc

# nginx, SSH, MySQL 동시에 실행하기 위한 커맨드
CMD [ \
  "/bin/bash", "-c", \
  "/root/work/run/dashboard/start.sh && \
  service nginx start && \
  service mysql start && \
  /usr/sbin/sshd -D" \
]
