from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

with open("market_data.json", "r") as f:
    market_data = json.load(f)


@app.get("/")
def home():
    return {"message": "SnapReport API Running"}


@app.get("/zipcodes")
def get_zipcodes():
    return {
        "available_zipcodes": list(market_data.keys())
    }


@app.get("/report/{zipcode}")
def generate_report(zipcode: str):
    data = market_data.get(zipcode)

    if not data:
        return {
            "error": "ZIP code not found",
            "available_zipcodes": list(market_data.keys())
        }

    prompt = f"""
    Write a professional monthly real estate market report.

    City: {data['city']}, {data['state']}
    Median Price: {data['median_price']}
    Days on Market: {data['days_on_market']}
    List-to-Sale Ratio: {data['list_to_sale_ratio']}
    New Listings: {data['new_listings']}
    Inventory: {data['inventory']}
    Trend: {data['trend']}

    Include:
    1. Market Summary
    2. What This Means For Sellers

    Keep it under 250 words.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=400
        )

        narrative = response.choices[0].message.content

    except Exception as e:
        print("Groq Error:", e)

        narrative = f"""
Market Summary:
{data['city']}, {data['state']} currently has a median home price of {data['median_price']}.
Homes stay on the market for approximately {data['days_on_market']} days, with a list-to-sale ratio of {data['list_to_sale_ratio']}.

What This Means For Sellers:
Current inventory is {data['inventory']} with {data['new_listings']} new listings.
Sellers can benefit from understanding local market conditions before listing.

Why Contact a Snaphomz Agent:
Snaphomz provides local expertise, pricing guidance, and marketing support
to help homeowners maximize property value.
"""

    return {
        "zipcode": zipcode,
        "data": data,
        "narrative": narrative
    }