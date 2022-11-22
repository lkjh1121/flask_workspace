import os

from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    #설정 
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="adslkfajewiofjnxvd",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #파일업로드 준비하기 
    UPLOAD_FOLDER = r"C:\flask_workspace\hello\hello\upload"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    #파일업로드 위치값을 config라는 dict타입에 위칟값 저장하기 
    app.config["MAX_CONTENT_LENGTH"]= 20 * 1024 * 1024 #20MB까지만

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/")
    def index():
        return "Hello, Flask !!!"

    #블루프린트 
    from . import board 
    app.register_blueprint(board.bp) 

    from . import calc 
    app.register_blueprint(calc.cp) 

    # /calc/add/4/5 -> 9 


    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app





