from fastapi import APIRouter, status, HTTPException
import requests
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

load_dotenv()

class BerryFetcher:

    def __init__(self, api_url: str):
        self.api_url = api_url 

    def fetch(self) -> list:
        """
        Fetches all berry data from the API endpoint.

        Returns: 
            list: A list of berry data.
        """
        all_berries = []

        try:
            while self.api_url:
                response = requests.get(self.api_url)  
                response.raise_for_status()
                raw_data = response.json()
                berries = raw_data.get('results', [])

                if self._validate(berries):
                    all_berries.extend(berries)

                self.api_url = raw_data.get('next')

            return all_berries
        except requests.RequestException as e:
            print(f"Error fetching berry data: {e}")
            return []

    def _validate(self, data: list) -> bool:
        """
        Validates the fetched data.

        Args:
            data (list): Fetched berry data.

        Returns:
            bool: True if the data is valid, False otherwise.
        """
        return isinstance(data, list) and all(isinstance(berry, dict) and 'name' in berry for berry in data)
    
    
router = APIRouter(prefix="/api/v1", tags=["Get all berry stats"], responses={404: {"description": "Not found"}})

@router.get("/allBerryStats", status_code=status.HTTP_200_OK, response_description="Get all berry stats")
async def get_all_berry_stats() -> JSONResponse:
    try:
        api_url = os.getenv('POKEBERRIES_API_URL')
        if not api_url:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Missing API URL")

        fetcher = BerryFetcher(api_url)
        berries = fetcher.fetch()

        response_content = {'error': False, 'quantity': len(berries), 'data': berries}
        return JSONResponse(content=response_content, status_code=status.HTTP_200_OK)
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))