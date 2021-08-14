FROM nginxinc/nginx-unprivileged:1-alpine

LABEL maintainer="dev@hrshadhin.me"

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

COPY default.conf.tpl uwsgi_params /etc/nginx/
COPY ./run.sh /run.sh

USER root
RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx
CMD ["/run.sh"]