FROM python:3.11.1-alpine3.16

COPY config.yml /code/config.yml
ADD docl.power_aggregator /code/
WORKDIR /code

RUN pip3 --no-cache-dir install -e .

ENTRYPOINT ["python", "-m", "docl.power_aggregator.main"]
CMD ["--from", "01-01-2023", "--to", "02-01-2023", "--format", "json"]