FROM python:3.12.3

SHELL ["/bin/bash", "-c"]

# set virtual environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip
RUN pip install --upgrade pip

# update packages
RUN apt update

# create new user
RUN useradd -rms /bin/bash mainuser && chmod 777 /opt /run

# create directory
WORKDIR /code

# copy the project files to the image directory
COPY --chown=mainuser:mainuser . .

# install all dependencies for pip
RUN pip install -r requirements.txt

# switch to the created user
USER mainuser

# listening on a specified port
EXPOSE 8000

# start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]