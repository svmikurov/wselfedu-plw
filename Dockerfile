FROM python:3.12-bookworm
RUN pip install --upgrade pip && \
    pip install playwright && \
    pip install pytest==8.2.2 && \
    pip install pytest-playwright==0.5.0 && \
    playwright install && \
    playwright install-deps
COPY requirements.txt   /temp/requirements.txt
RUN pip install -r      /temp/requirements.txt
WORKDIR                 /src
COPY pytest.ini         /src/pytest.ini
COPY .env               /src/.env
COPY /src               /src
CMD ["pytest"]
