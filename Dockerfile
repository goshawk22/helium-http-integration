FROM python:3.9-slim

WORKDIR /workdir

ENV PATH /root/.local/bin:${PATH}

COPY ./requirements.txt /workdir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /workdir/requirements.txt

EXPOSE 80

COPY ./app /workdir/app

ENTRYPOINT ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]