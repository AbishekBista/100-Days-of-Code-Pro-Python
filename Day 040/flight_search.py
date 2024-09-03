from secret import AMADEUS_BASE_URL, AMADEUS_API_KEY, AMADEUS_SECRET
from flight_data import FlightData
import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def getAccessToken(self):
        access_params = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_SECRET
        }
        access_header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=access_params, headers=access_header)
        response.raise_for_status()
        return response.json()["access_token"]
    

    def get_destination_code(self):
        token = self.getAccessToken()
        print(token)
        headers = {
            "Authorization": f"Bearer {token}"
        }
        iata_search_params = {
            "subType": ["CITY"],
            "keyword": self.flightData.city, 
        }

        response = requests.get(f"{AMADEUS_BASE_URL}/reference-data/locations", json=iata_search_params, headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        code = data[0]["code"]
        return code
        

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        token = self.getAccessToken()
        headers = {
            "Authorization": f"Bearer {token}"
        }

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=f"{AMADEUS_BASE_URL}/v2/search", headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(requests.get(url=f"{AMADEUS_BASE_URL}/v2/search", headers=headers, params=query))
            data = response.json()["data"][0]
            print(data)

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs= 1,
                via_city = data["route"][0]["cityTo"]
            )

            return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
        
        

    # get the IATA code
    # the flight data format will be used to structure the data and then sent to sheety, call data_manager

    # get the cheapest flight from tomorrow to 6 months for all cities, get data_manager to get the list of data for cheapest
    # comparison

    # price lower logic?