FROM python

RUN apt-get update && apt-get install -y \
	python3-pip \
        && apt-get clean 

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY app.py config.py /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py"]