#!/bin/bash

# entrypoint.sh file of Dockerfile

# Section 1- Bash options
set -o errexit  
set -o pipefail  
set -o nounset

# Section 2: Health of dependent services  
postgres_ready() {  
    python <<-EOF
import sys

from psycopg2 import connect  
from psycopg2.errors import OperationalError

try:  
    connect(  
        dbname="${SQL_DATABASE}",  
        user="${SQL_USER}",  
        password="${SQL_PASSWORD}",  
        host="${SQL_HOST}",  
        port="${SQL_PORT}",  
    )  

except OperationalError: 
    sys.exit(-1)  
EOF
}

until postgres_ready; do  
  >&2 echo "Waiting for PostgreSQL to become available..."  
  sleep 5  
done  
>&2 echo "PostgreSQL is available"

# Section 3- Idempotent Django commands  
python manage.py collectstatic --noinput  
python manage.py makemigrations  
python manage.py migrate
python manage.py loaddata dev/data_sample.json

exec "$@"