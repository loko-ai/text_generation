FROM lokoai/python_transformers
EXPOSE 8080
ADD ./requirements.lock /
RUN pip install -r /requirements.lock
RUN echo "ciao"
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin
# CMD python services.py
CMD uvicorn services.services:app --port 8080 --host  0.0.0.0
