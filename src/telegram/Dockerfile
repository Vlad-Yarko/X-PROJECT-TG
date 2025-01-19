FROM python:3.12

WORKDIR /src/telegram

COPY . .

RUN pip install -r requirements.txt

WORKDIR /

CMD ["python", "-m", "src.telegram.main"]