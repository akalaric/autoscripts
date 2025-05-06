FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    curl \
    sudo \	
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

RUN useradd -m -s /bin/bash myuser \
    && usermod -aG sudo myuser \
    && echo 'myuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN usermod -aG sudo myuser
WORKDIR /app
USER myuser

CMD ["bash"]

