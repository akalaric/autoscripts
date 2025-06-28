# Tools Overview

This repository includes various scripts and tools for system setup, container management, and benchmarking.

- `dev_tools/Dockerfile`
Sets up a Docker container with tools for development and testing, including curl, sudo, vim, git, python3, nmap, and others.

- `dev_tools/Dockerfile.ext`
A more extended development environment based on Ubuntu 22.04 with multiverse/universe enabled, for more specialized packages.

- `dev_tools/install_docker`
Script to install Docker on an Ubuntu system using Docker's official GPG key and repository.

- `dev_tools/min_sys`
Installs a minimal system toolkit, including Docker, Python, GDB, GCC, networking tools (nmap, dnsmap), and penetration testing utilities (john, whois).

- `dev_tools/encdcp`
Bash script for file encryption and decryption. <br>
Usage:
```bash
./encdcp enc|dec input_file output_file.
```

- `scripts/cpu_bench`
A benchmarking script to test CPU core performance using taskset. Runs dd to write data per core and logs results.


- `sysAPI/`
A lightweight FastAPI-based REST API for system diagnostics and basic shell command execution.

- `sysAPI/Dockerfile`
Builds a Python 3.11-based image with FastAPI and Uvicorn for serving the app.

- `sysAPI/docker-compose.yaml`
Launches three containers (fastapi1, fastapi2, fastapi3) with the same API app, each on a different port (8001–8003) and IP within the vsnet network (a custom Docker subnet).
