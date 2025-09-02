# Backend/routes.py

from flask import Blueprint, request, jsonify
from models import db, Donor, Center

# ✅ rename blueprint from "api" → "main"
main = Blueprint("main", __name__)

# Save donor info
@main.route("/donors", methods=["POST"])
def add_donor():
    data = request.json
    donor = Donor(
        name=data.get("name"),
        email=data.get("email"),
        phone=data.get("phone"),
        health_condition=data.get("health_condition"),
        location=data.get("location"),
    )
    db.session.add(donor)
    db.session.commit()
    return jsonify({"message": "Donor info saved successfully"}), 201


# Find nearby centers (basic version – filter by city for now)
@main.route("/centers", methods=["GET"])
def centers():
    city = request.args.get("city", "")
    if city:
        centers = Center.query.filter_by(city=city).all()
    else:
        centers = Center.query.all()

    return jsonify([c.to_dict() for c in centers])
