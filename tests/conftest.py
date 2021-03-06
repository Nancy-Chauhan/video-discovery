import os
import time

import flask_migrate
import pytest
from testcontainers.postgres import PostgresContainer

from video_discovery.app import create_app


@pytest.fixture(scope="session", autouse=True)
def app():
    with PostgresContainer('postgres:13') as postgres:
        os.environ['DATABASE_URI'] = postgres.get_connection_url()
    time.sleep(5)
    flask_app = create_app()
    flask_app.config['TESTING'] = True

    with flask_app.app_context():
        flask_migrate.upgrade()

    yield flask_app
