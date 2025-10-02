import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("AMADEUS_CLIENT_ID")
client_secret = os.getenv("AMADEUS_CLIENT_SECRET")

if not client_id or not client_secret:
    print("AMADEUS_CLIENT_ID and AMADEUS_CLIENT_SECRET not set. Cannot proceed.")
    exit()

origin = input("Enter origin airport code (e.g., WAW): ").upper()
destination = input("Enter destination airport code (e.g., BCN): ").upper()
depart_date = input("Enter departure date (YYYY-MM-DD): ")
currency = input("Enter currency code (e.g., USD): ").upper()

token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
offers_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}
token_response = requests.post(token_url, data=token_data)

if token_response.status_code != 200:
    print("Failed to get token:", token_response.text)
    exit()

access_token = token_response.json().get("access_token")

headers = {
    "Authorization": f"Bearer {access_token}"
}

params = {
    "originLocationCode": origin,
    "destinationLocationCode": destination,
    "departureDate": depart_date,
    "adults": 1,
    "currencyCode": currency,
    "max": 10  # istədiyin qədər təklif gətirə bilər
}

offers_response = requests.get(offers_url, headers=headers, params=params)

if offers_response.status_code != 200:
    print("Failed to get offers:", offers_response.text)
    exit()

offers = offers_response.json()
def get_cheapest_flight(offers, currency):
    flights = []

    for offer in offers.get("data", []):
        price = float(offer["price"]["total"])
        segments_list = []

        for itinerary in offer["itineraries"]:
            for segment in itinerary["segments"]:
                carrier_code = segment["carrierCode"]
                carrier = offers["dictionaries"]["carriers"].get(carrier_code, carrier_code)
                departure = segment["departure"]["iataCode"]
                arrival = segment["arrival"]["iataCode"]

                segments_list.append({
                    "carrier": carrier,
                    "route": f"{departure} -> {arrival}"
                })

        flights.append({
            "price": price,
            "segments": segments_list
        })

    if flights:
        cheapest = min(flights, key=lambda x: x["price"])
        print(f"Cheapest flight: {cheapest['price']} {currency}")

        # bütün seqmentləri göstərir burada
        for seg in cheapest["segments"]:
            print(f"  Carrier: {seg['carrier']}, Route: {seg['route']}")
    else:
        print("No offers found.")

get_cheapest_flight(offers, currency)

