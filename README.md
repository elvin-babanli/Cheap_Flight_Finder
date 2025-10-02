# Cheap Flight Finder

A Python-based CLI application that fetches **real-time flight offers** using the Amadeus API and automatically returns the **cheapest option** with complete segment details (airlines + routes).  

This project was built with a strong focus on **clean code**, **secure secret management**, and **practical problem-solving** for real-world scenarios.  

---

## ✨ Key Highlights

- **Real-time results**: always fetches live prices from the Amadeus API  
- **Cheapest flight detection**: compares multiple offers and selects the lowest fare  
- **Readable output**: shows carriers and routes in a human-friendly way  
- **Security-first**: credentials stored in `.env` (ignored by Git)  
- **Clear structure**: concise, functional, and extensible Python code  

---

## 🧠 Skills Demonstrated

- **OAuth2 Client Credentials Flow** implementation  
- **REST API consumption** with `POST` (for access tokens) and `GET` (for flight offers)  
- **JSON parsing & dictionary lookups** (carrier codes → airline names)  
- **Algorithmic filtering**: using Python’s `min(...)` to find the cheapest option  
- **Defensive programming** with error handling for missing credentials, failed requests, and empty results  
- **Command-line UX**: user inputs normalized (`upper()`), structured outputs for readability  

This shows my ability to work with **real-time APIs**, write **secure and maintainable code**, and design solutions with **product sense** — exactly the mindset I bring into professional software development.

---

## 🌍 How to Get API Credentials

1. Go to the official Amadeus Developer Portal:  
   👉 https://developers.amadeus.com/

2. Create a free developer account  

3. Register a new application to receive your **API Key** and **API Secret**  

4. Save them into a `.env` file in the project root:

   ```dotenv
   AMADEUS_CLIENT_ID=your_amadeus_api_key
   AMADEUS_CLIENT_SECRET=your_amadeus_api_secret



## ▶️ Example Run & Output

```
Enter origin airport code (e.g., WAW): waw
Enter destination airport code (e.g., BCN): JFK
Enter departure date (YYYY-MM-DD): 2025-10-15
Enter currency code (e.g., USD): USD


Cheapest flight: 442.33 USD
  Carrier: TAP PORTUGAL, Route: WAW -> LIS
  Carrier: TAP PORTUGAL, Route: LIS -> JFK

