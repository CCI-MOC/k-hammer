FROM ghcr.io/cci-moc/hammerdb:master

RUN apt install -y python3
RUN apt install -y wget
RUN apt install -y python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip install pexpect PyYaml
