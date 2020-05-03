FROM python:3.7.3-slim-stretch

WORKDIR /app

COPY . .

RUN pip install numpy==1.18.3 pandas==1.0.3 jupyter==1.0.0 

VOLUME [ ":/app" ]

EXPOSE 8888

CMD ["jupyter","notebook","--ip=0.0.0.0","--no-browser","--allow-root"]