FROM python:3.12-slim

ARG UID=10001
ARG GID=10001

RUN groupadd -g ${GID} appgroup \
 && useradd -m -u ${UID} -g ${GID} -s /usr/sbin/nologin appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p /app/logs && chown -R appuser:appgroup /app
ENV LOG_DIR=/app/logs

USER appuser
EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
