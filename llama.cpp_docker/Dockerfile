FROM ubuntu:22.04

# Install core packages with Ubuntu-specific enhancements
RUN apt-get update && apt-get install -y \
    build-essential cmake ninja-build ccache \
    git wget curl sudo pkg-config \
    python3.10 python3-dev python3-pip \
    libssl-dev libstdc++-12-dev libopenblas-dev libzstd-dev \
    ocl-icd-opencl-dev libclblast-dev \
    nvidia-opencl-dev libcurl4-openssl-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Build llama.cpp with Ubuntu-specific optimizations
WORKDIR /opt
RUN git clone https://github.com/ggml-org/llama.cpp && \
    cd llama.cpp && mkdir -p build && cd build && \
    cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLAMA_BLAS=ON \
    -DLLAMA_CLBLAST=ON \
    -DLLAMA_NATIVE=ON \
    -DCMAKE_CUDA_ARCHITECTURES=native \
    && make -j$(nproc) install && ldconfig

# Configure non-root user with GPU access
RUN useradd -m -s /bin/bash myuser && \
    usermod -aG video myuser && \
    echo 'myuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /app
USER myuser

CMD ["bash"]

