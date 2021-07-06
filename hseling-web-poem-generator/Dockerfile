FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_web_build

LABEL maintainer="Boris Orekhov <borekhov@hse.ru>"

RUN mkdir /dependencies
COPY ./hseling-web-poem-generator/requirements.txt /dependencies/requirements.txt
COPY ./hseling-web-poem-generator/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_web_production

COPY --from=hseling_web_build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=hseling_web_build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=hseling_web_build /dependencies /dependencies

COPY ./hseling-web-poem-generator/hseling_web_poem_generator /app/hseling_web_poem_generator
COPY ./hseling-web-poem-generator/hseling_web_poem_generator/static /app/static
COPY ./hseling-web-poem-generator/main.py /app/main.py

ENV HSELING_WEB_POEM_GENERATOR_SETTINGS="/app/hseling_web_poem_generator/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost:8000/web/healthz || exit 1

EXPOSE 8000
