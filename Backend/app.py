from flask import Flask
from database import db, create_app
from routes import register_routes

# Initialize Flask App
app = create_app()

# Register API routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
