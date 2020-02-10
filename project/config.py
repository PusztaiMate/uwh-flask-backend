import os


class BasicConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # TODO:
    SECRET_KEY = "this shouldn't be here, please move it"


class DevelopmentConfig(BasicConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class TestingConfig(BasicConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_TEST_URL")


class ProductionConfig(BasicConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
