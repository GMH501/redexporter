FROM python:3.6-alpine
COPY . /redexporter
WORKDIR /redexporter
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
