class BasicConfig:
    TESTING = False


class DevelopmentConfig(BasicConfig):
    pass


class TestingConfig(BasicConfig):
    TESTING = False


class ProductionConfig(BasicConfig):
    pass
