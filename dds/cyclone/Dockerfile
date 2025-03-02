FROM ubuntu:24.04

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt update && apt install -y \
    cmake git build-essential libasio-dev libtinyxml2-dev

WORKDIR /thirdparty
RUN git clone https://github.com/eclipse-cyclonedds/cyclonedds.git
WORKDIR /thirdparty/cyclonedds/build
RUN cmake ..
RUN cmake .. -DENABLE_TYPELIB=1 -DCMAKE_INSTALL_PREFIX=/usr/local 
RUN cmake --build . --config RelWithDebInfo --target install

ENV CYCLONEDDS_HOME=/usr/local
ENV CMAKE_PREFIX_PATH=/usr/local

WORKDIR /thirdparty
RUN git clone https://github.com/eclipse-cyclonedds/cyclonedds-python
WORKDIR /app
RUN uv venv
RUN uv pip install /thirdparty/cyclonedds-python
# COPY subscriber.py .
# 
# CMD ["uv", "run", "subscriber.py"]
