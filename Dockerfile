FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    git \
    wget \
    python3 \
    neofetch \
    speedtest-cli \
    bat \
    nmap \
    linkchecker \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

CMD ["bash"]

