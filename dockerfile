FROM python:3.13

WORKDIR /Entrega-Atividade-Full-Stack-main

COPY requirements.txt .

RUN 

EXPOSE 5000

CMD ["python","-m","App"]