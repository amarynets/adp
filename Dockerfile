FROM python:3.9
WORKDIR /app
COPY requirements.txt requirement.txt

COPY adp .


CMD ["python", "manage.py", "runserver", "0:8000"]


