FROM ubuntu:22.04

# Install build dependencies and cleanup in one step
RUN apt-get update && apt-get install -y \
    build-essential cmake ninja-build ccache \
    git wget curl sudo pkg-config \
    python3.10 python3-dev python3-pip \
    libssl-dev libstdc++-12-dev libopenblas-dev libzstd-dev \
    ocl-icd-opencl-dev libclblast-dev \
    nvidia-opencl-dev libcurl4-openssl-dev \
    libgomp1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt

# Clone and build llama.cpp
RUN git clone https://github.com/ggml-org/llama.cpp && \
    cd llama.cpp && \
    pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt && \
    mkdir -p build && cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release -DLLAMA_BLAS=ON -DLLAMA_CLBLAST=ON -DLLAMA_NATIVE=ON -DCMAKE_CXX_FLAGS="-march=native" && \
    make -j$(nproc) install && \
    ldconfig && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create user and set permissions
RUN useradd -m -s /bin/bash myuser && \
    usermod -aG video myuser && \
    echo 'myuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER myuser

# Set working directory to /app
WORKDIR /app

# Set entrypoint to bash
ENTRYPOINT ["/bin/bash"]

