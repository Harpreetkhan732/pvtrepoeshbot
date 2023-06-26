FROM nikolaik/python-nodejs:python3.9-nodejs18-bullseye
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    && curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    && apt-get install nodejs
RUN apt-get
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD bash start
