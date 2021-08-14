FROM python:3.9-alpine3.13

LABEL maintainer="dev@hrshadhin.me"

EXPOSE 9000
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol

COPY ./requirements.txt /requirements.txt

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps

COPY ./scripts /scripts
RUN chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

COPY ./app /app
WORKDIR /app

USER app
CMD ["run.sh"]