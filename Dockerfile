# latest base image
FROM ubuntu:latest
# tools update

RUN apt-get update && apt-get install -y --no-install-recommends \
python3 \
python3-pip \
python3-venv \
vim \
build-essential \
gcc \
g++ \
make \
curl \
wget \
git \
python3-flask \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

# python3 link

RUN ln -sf /usr/bin/python3 /usr/bin/python && ln -sf /usr/bin/pip3 /usr/bin/pip

# work dir set, and enter into app dir

WORKDIR /app
RUN chmod 777 /app
# download code

# RUN git clone   https://github.com/yifanCandy/data_demo.git
RUN git clone   https://github.com/hxh-persistence/openshift.git

RUN  cp  -r /app/openshift/*    /app
# RUN  cp  -r /app/openshift/* /appenv

RUN ls -l /app

# 添加镜像默认命令

CMD ["python", "./app.py"]
