FROM debian:10

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# install Python3.7
RUN apt update && \
    apt install -y python3.7 python3-pip 

# Install production dependencies.
RUN pip3 install --no-cache-dir -r requirements.txt

# install java 8
RUN apt install -y wget software-properties-common apt-transport-https gnupg && \
    wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | apt-key add - && \
    add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ && \
    apt update && \
    apt install -y adoptopenjdk-8-hotspot


# embulk download
RUN apt install -y curl
RUN curl --create-dirs -o /usr/local/bin/embulk -L "https://dl.embulk.org/embulk-latest.jar" && \
    chmod +x /usr/local/bin/embulk

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app