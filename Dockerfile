FROM python:3.12-bookworm
WORKDIR /wselfedu-plw

RUN pip install --upgrade pip && \
    pip install playwright && \
    pip install pytest==8.2.2 && \
    pip install pytest-playwright==0.5.0 && \
    playwright install && \
    playwright install-deps

COPY requirements.txt ./temp/requirements.txt
RUN pip install --no-cache-dir -r ./temp/requirements.txt

COPY . .

CMD ["pytest"]
