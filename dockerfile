FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
COPY ./app /app

ENV PORT 9001
ENV REDIS_HOST redis-17215.c61.us-east-1-3.ec2.cloud.redislabs.com
ENV REDIS_PORT 17215
ENV REDIS_PASSWORD Wb4HuzcHitEj6ZDUqMKGBcOlyVGkj5vJ

EXPOSE 9001

CMD ["python", "/app/server.py"]