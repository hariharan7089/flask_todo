from flask import Flask
from extension import mongo
from main.routes import main

def create_app():
    app = Flask(__name__)

    # MongoDB URI - replace with your actual MongoDB URI
    app.config["MONGO_URI"]  ="mongodb+srv://hariharank:HARIHARANK@cluster0.7njml.mongodb.net/todo?tls=true&authSource=website&authMechanism=SCRAM-SHA-1"

    
    # Initialize PyMongo with the Flask app
    mongo.init_app(app)

    # Register blueprint
    app.register_blueprint(main)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5000 ,debug=True)
