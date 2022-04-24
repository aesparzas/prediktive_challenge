import sys
import json
from datetime import datetime

import requests


class ValueCalculator:
    def __init__(self, api_client=''):
        self.api_client = api_client

    def _get_api_response(self):
        """Method to get the response from the API for getting the ratios info
        If no API client is set, it returns a mocked API response"""
        if self.api_client:
            response = requests.get(self.api_client)
            if not response:
                raise ValueError()
            response = response.json()
            response = response[0] if isinstance(response, list) else response
        else:
            with open('api-response.json') as f:
                txt = f.read()
            response = json.loads(txt)
        return response

    def calculate_vals(self, model_id, year):
        """Method to calculate the values based on inputs and response's ratios

        :param model_id: str of numeric id for the model
        :param year: str for the specific year to check ratios
        :return: dict with calculated market and auction values or error
        """
        current_year = datetime.now().year
        if int(year) > current_year:
            return {"error": "No data for future years"}

        try:
            response = self._get_api_response()
        except ValueError:
            return {"error": "Could not get API response"}

        try:
            response = response[model_id]
            cost = response['saleDetails']['cost']
        except KeyError:
            return {"error": "No such ID in data"}
        try:
            response = response['schedule']['years'][year]
        except KeyError:
            return {"error": "No data for given year"}
        return {
            "MarketValue": cost * response['marketRatio'],
            "AuctionValue": cost * response['auctionRatio'],
        }


if __name__ == '__main__':
    """For using the script, you need to pass at least two arguments
    Those being the model and year, in that order
    A third argument can be sent specifying the API url to get the data from"""
    args = sys.argv
    if not len(args) < 3:
        vc = ValueCalculator(args[3] if len(args) >= 4 else '')
        print(vc.calculate_vals(args[1], args[2]))
    else:
        print('arguments missing')
