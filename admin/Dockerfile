FROM python:3.14
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requeirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python3 manage.py runserver 0.0.0.0:8000