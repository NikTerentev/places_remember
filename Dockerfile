FROM python:3.12.3

SHELL ["/bin/bash", "-c"]

# set virtual environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip
RUN pip install --upgrade pip

# update packages
RUN apt update
RUN apt install -y gdal-bin libpq-dev

# create new user
RUN useradd -rms /bin/bash mainuser && chmod 777 /opt /run

# create directory
WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/
# install all dependencies for pip
RUN pip install -r requirements.txt

# copy the project files to the image directory
COPY --chown=mainuser:mainuser . /code/

RUN chmod +x ./wait-for-it.sh
RUN chmod -R 777 /code

# switch to the created user
USER mainuser

# listening on a specified port
EXPOSE 8000