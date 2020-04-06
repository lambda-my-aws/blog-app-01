FROM python:3.8.2-slim
RUN groupadd -r app -g 1042 && useradd -u 1042 -r -g app -m -d /app -s /sbin/nologin -c "App user" app && chmod 755 /app

USER app
ENV PATH=$PATH:/app/.local/bin

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --user
ENV FLASK_APP=app01

COPY app01 app01
COPY config.py config.py
COPY supervisord.config supervisord.config

EXPOSE 5000
CMD ["supervisord", "-n", "-c", "supervisord.config"]
