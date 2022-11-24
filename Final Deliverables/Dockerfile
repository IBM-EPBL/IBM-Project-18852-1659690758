FROM python:3.10.8-bullseye
LABEL maintainer="Harshaa Vardaan"

RUN mkdir /app
COPY . /app
WORKDIR /app

ENV POETRY_VERSION=1.2.2
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

# Install all dependencies
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root

#Run application
EXPOSE 5000
ENTRYPOINT [ "./entrypoint.sh" ]

