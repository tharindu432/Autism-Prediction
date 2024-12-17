from flask import Flask


def create_app(config_name='development'):
    """
    Create and configure the Flask application

    :param config_name: Configuration environment (development/production)
    :return: Configured Flask application
    """
    app = Flask(__name__)

    # Load configuration
    if config_name == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    # Register blueprints
    from .routes.prediction import prediction_bp
    app.register_blueprint(prediction_bp, url_prefix='/api')

    return app