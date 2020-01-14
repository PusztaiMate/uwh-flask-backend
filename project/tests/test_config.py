import os


def test_development_config(test_app):
    test_app.config.from_object("project.config.DevelopmentConfig")
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")


def test_testing_config(test_app):
    test_app.config.from_object("project.config.TestingConfig")
    assert test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]


def test_production_config(test_app):
    test_app.config.from_object("project.config.ProductionConfig")
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
