from flask import request, jsonify
from models import db, User, Campaign, Donation
from payments import create_payment

def register_routes(app):
    # ✅ Home Route
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Welcome to the Crowdfunding Platform!"})

    # ✅ User Registration
    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        if not data or "email" not in data or "username" not in data or "password" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if user exists
        existing_user = User.query.filter_by(email=data["email"]).first()
        if existing_user:
            return jsonify({"error": "User already exists"}), 400

        # Create user
        user = User(email=data["email"], username=data["username"])
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    # ✅ Create a Campaign
    @app.route("/create_campaign", methods=["POST"])
    def create_campaign():
        data = request.get_json()
        if not data or "title" not in data or "description" not in data or "goal_amount" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        campaign = Campaign(
            title=data["title"],
            description=data["description"],
            goal_amount=data["goal_amount"],
            user_id=1  # Hardcoded for now, replace with logged-in user ID
        )
        db.session.add(campaign)
        db.session.commit()

        return jsonify({"message": "Campaign created successfully!", "campaign_id": campaign.id}), 201

    # ✅ Make a Donation (Integrate Razorpay)
    @app.route("/donate", methods=["POST"])
    def donate():
        data = request.json
        if "amount" not in data or "campaign_id" not in data:
            return jsonify({"error": "Amount and campaign_id are required"}), 400

        order = create_payment(data["amount"])
        return jsonify(order)
