FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_api_build

LABEL maintainer="Boris Orekhov <borekhov@hse.ru>"

RUN mkdir /dependencies
COPY ./hseling-api-poem-generator/requirements.txt /dependencies/requirements.txt
COPY ./hseling-api-poem-generator/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=hseling_api_build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=hseling_api_build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=hseling_api_build /dependencies /dependencies

COPY ./hseling-lib-poem-generator /dependencies/hseling-lib-poem-generator
RUN pip install /dependencies/hseling-lib-poem-generator

COPY ./hseling-api-poem-generator/hseling_api_poem_generator /app/hseling_api_poem_generator
COPY ./hseling-api-poem-generator/main.py /app/main.py

RUN mkdir -p /data

ENV HSELING_API_POEM_GENERATOR_SETTINGS="/app/hseling_api_poem_generator/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost:5000/api/healthz || exit 1

