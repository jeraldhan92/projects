FROM python

RUN apt-get update && apt-get install -y \
	python3-pip \
        && apt-get clean && rm -rf /tmp/* /var/tmp/*

WORKDIR /app

COPY requirements.txt /app/
COPY main.py /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]