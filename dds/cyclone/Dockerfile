FROM python:3.10

RUN apt update && apt install -y \
    cmake git build-essential libasio-dev libtinyxml2-dev

WORKDIR /thirdparty
RUN git clone https://github.com/eclipse-cyclonedds/cyclonedds.git
WORKDIR /thirdparty/cyclonedds/build
RUN cmake ..
RUN cmake .. -DENABLE_TYPELIB=1 -DCMAKE_INSTALL_PREFIX=/usr/local 
RUN cmake --build . --config RelWithDebInfo --target install

ENV CYCLONEDDS_HOME=/usr/local

# WORKDIR /thirdparty
# RUN git clone https://github.com/eclipse-cyclonedds/cyclonedds-python
WORKDIR /app
RUN pip install cyclonedds --no-build cyclonedds
