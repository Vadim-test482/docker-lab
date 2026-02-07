FROM ubuntu:24.04
RUN apt update && apt install -y curl
WORKDIR /data
RUN echo "Dockerfile practice" > info.txt
CMD ["cat", "info.txt"]
