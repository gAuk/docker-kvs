From python:3.10.0a2-slim
RUN pip install pytest==6.1.2 requests==2.25.0
WORKDIR /src
COPY ./src/test_app.py /src/test_app.py
ENV APP_HOST 127.0.0.1
ENV APP_PORT 80
CMD ["tail", "-f", "/dev/null"]
