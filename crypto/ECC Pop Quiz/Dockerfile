FROM ubuntu:latest
ENV PIP_BREAK_SYSTEM_PACKAGES 1
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update 
RUN apt-get install -y xinetd python3 python3-pip
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN pip3 install pycryptodome libnum
RUN useradd -U -m -s /bin/bash epq

WORKDIR /home/epq

COPY ./flag.txt .
COPY ./soal.py .
COPY ./run.sh ./run
COPY ./xinetd /etc/xinetd.d/xinetd
COPY ./startchall.sh /usr/bin/startchall

RUN chown -R root:epq /home/epq
RUN chmod -R 750 /home/epq && chmod 440 flag.txt 
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall

EXPOSE 13371

CMD ["/usr/bin/startchall"]
