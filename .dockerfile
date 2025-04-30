FROM apache/airflow:3.0.0-python3.12

USER root

RUN apt update && apt install -y patch patchutils

RUN set -ex; \
    cd /home/airflow/.local/lib/python3.12/site-packages/airflow; \
    curl https://patch-diff.githubusercontent.com/raw/apache/airflow/pull/49721.patch \
    | filterdiff -p1 -i 'airflow-core/src/airflow/*' | patch -p4 -u --verbose; \
    curl https://patch-diff.githubusercontent.com/raw/apache/airflow/pull/49724.patch \
    | patch -p5 -u --verbose; \
    curl https://patch-diff.githubusercontent.com/raw/apache/airflow/pull/49581.patch \
    | filterdiff -p1 -i 'providers/fab/src/airflow/*' | patch -p5 -u --verbose

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt