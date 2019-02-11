FROM python:3

WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir pipenv

COPY . .

RUN pipenv install --system --deploy

CMD ["python", "./helloworld.py"]

