FROM python:3.10
COPY . .
RUN python3 -m unittest 
RUN python3 -m pip install --upgrade pip setuptools wheel build
RUN python3 -m build
RUN python3 -m pip install dist/*.tar.gz