from python:3.7.4-slim
workdir /build
env LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    TZ=America/Denver
run apt-get update && apt-get install -y \
    build-essential \
    vim \
    wget \
    curl \
    htop \
    git && \
    curl -sL https://deb.nodesource.com/setup_16.x | bash -- && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /build
workdir /mnt
copy requirements.txt /mnt/requirements.txt
run pip install -r requirements.txt
