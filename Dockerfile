FROM python:3.11
ENV PYTHONUNBUFFERED=1
RUN addgroup app && adduser --system --group app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
USER app
COPY . .
RUN python3 manage.py migrate
EXPOSE 8000
ENTRYPOINT python manage.py runserver 0.0.0.0:8000