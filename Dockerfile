FROM python:3.6-alpine
COPY . /prinquest
WORKDIR /prinquest
RUN pip install flask
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
