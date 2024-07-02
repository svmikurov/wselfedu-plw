FROM python:3.12-bookworm
WORKDIR /tests
RUN pip install --upgrade pip && \
    pip install playwright && \
    playwright install && \
    playwright install-deps
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
    pip install --upgrade pip
COPY .env /tests/.env
COPY /tests /tests
CMD ["pytest"]