FROM nginx:alpine
RUN apk add --no-cache curl
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl -fsS http://localhost/health || exit 1

EXPOSE 80
