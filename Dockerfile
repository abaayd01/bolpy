FROM python:3.7
RUN pip install pipenv
RUN mkdir /app
COPY Pipfile* /app/
RUN cd /app && pipenv lock --requirements > requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
EXPOSE 50051
CMD python /app/main.py