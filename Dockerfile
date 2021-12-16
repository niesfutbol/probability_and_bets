FROM python:3.8
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    jinja2 \
    mutmut \
    pandas \
    pydantic \
    pylint \
    pytest \
    pytest-cov \
    pytest-mock \
    rope \
    typer
RUN curl -fsSL https://get.deta.dev/cli.sh | sh
CMD make