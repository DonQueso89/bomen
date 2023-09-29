FROM python:3.11.4-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
COPY dev-requirements.txt dev-requirements.txt
RUN pip install -r requirements.txt -r dev-requirements.txt --no-warn-script-location --no-cache-dir
EXPOSE 8000
RUN mkdir bomen
COPY bomen ./bomen/
CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "bomen.main:app"]
