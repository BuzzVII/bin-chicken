FROM ubuntu:24.04

RUN apt update && apt install -y libasio-dev libssl-dev libboost-all-dev pybind11-dev libtinyxml2-dev libp11-dev softhsm2 libengine-pkcs11-openssl
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /Fast-DDS
RUN apt install -y wget git cmake g++ gcc && wget https://raw.githubusercontent.com/eProsima/Fast-DDS/master/fastdds.repos
RUN mkdir src
RUN uv venv
RUN uv pip install colcon-common-extensions vcstool
RUN uv run vcs import src < fastdds.repos
RUN uv run colcon build --packages-up-to fastdds

WORKDIR /Fast-DDS-python
RUN wget https://raw.githubusercontent.com/eProsima/Fast-DDS-python/main/fastdds_python.repos
RUN mkdir src
RUN uv venv
RUN uv pip install colcon-common-extensions vcstool
RUN uv run vcs import src < fastdds_python.repos
RUN uv run colcon build


