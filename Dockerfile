FROM python:3.7.3-slim-stretch

 
WORKDIR /app

COPY . . 

RUN apt-get update &&\
    apt-get -y upgrade &&\
    apt-get -y install gcc&&\
    apt -y autoremove

RUN  pip install psutil==5.7.0 numpy==1.18.3 pandas==1.0.3 jupyter==1.0.0 jupyterlab==2.1.0

VOLUME [ ":/app" ]

EXPOSE 8888

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]    