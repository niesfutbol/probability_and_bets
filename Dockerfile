FROM python:3.8
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    jinja2 \
    mutmut \
    pydantic \
    pylint \
    pytest \
    pytest-cov \
    pytest-mock \
    rope \
    typer
CMD make