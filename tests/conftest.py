import pytest

from server import create_app


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("project.server.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here
