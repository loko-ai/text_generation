FROM lokoai/python_transformers
EXPOSE 8080
ADD ./requirements.lock /
RUN pip install -r /requirements.lock
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
# CMD python services.py
CMD uvicorn services:app --port 8080 --host  0.0.0.0
