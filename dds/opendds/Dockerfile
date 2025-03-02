FROM ubuntu:24.04

RUN apt update && apt install -y libasio-dev libssl-dev libboost-all-dev pybind11-dev libtinyxml2-dev libp11-dev softhsm2 libengine-pkcs11-openssl wget git cmake g++ gcc make
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /thirdparty
RUN wget https://github.com/OpenDDS/OpenDDS/archive/refs/tags/DDS-3.31.tar.gz 
RUN tar -xf DDS-3.31.tar.gz
WORKDIR /thirdparty/OpenDDS-DDS-3.31/build
RUN cmake ..
RUN make -j8

ENV DDS_ROOT=/thirdparty/OpenDDS-DDS-3.31/build/
ENV ACE_ROOT=$DDS_ROOT/ACE
ENV INSTALL_PREFIX=/usr/

RUN make install
