FROM python:3.13

WORKDIR /Entrega-Atividade-Full-Stack-main

COPY Entrega-Atividade-Full-Stack-main/ .

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r /tmp/requirements.txt


EXPOSE 5000

CMD ["python","App.py"]