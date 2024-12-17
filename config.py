class Config:
    """Base configuration class"""
    DEBUG = False
    TESTING = False
    MODEL_PATH = 'app/models/model.pkl'
    ENCODERS_PATH = 'app/encoders/encoders.pkl'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False