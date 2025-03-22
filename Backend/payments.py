import razorpay
import os
from dotenv import load_dotenv

load_dotenv()

razorpay_client = razorpay.Client(auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET")))

def create_payment(amount, currency="INR"):
    order_data = {
        "amount": amount * 100,  # Convert to paise
        "currency": currency,
        "payment_capture": 1  # Auto-capture payment
    }
    return razorpay_client.order.create(order_data)
