FROM python:3.11
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
COPY "django_project/manage_local.pex" "/code/app"
CMD ["python /code/app runserver 0:8000"]
