from fastapi import APIRouter, status, HTTPException
import requests
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import statistics 
import aiohttp
import asyncio

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
        '''
        Validates the data returned from the API endpoint.
        
        Args:
            data (list): The data returned from the API endpoint.
        
        Returns:
            bool: True if the data is valid, False otherwise.
        
        '''
        return isinstance(data, list) and all(isinstance(berry, dict) and 'name' in berry for berry in data)

class BerryStatisticsCalculator:
    def __init__(self):
        self.stats = {}

    async def _fetch_berry_data(self, session, berry):
        '''
        Fetches the berry data from the API endpoint.
        
        Args:
            session (aiohttp.ClientSession): The aiohttp client session.
            berry (dict): The berry data.
            
        Returns:
            tuple: The growth time and name of the berry.
        '''
        try:
            async with session.get(berry['url']) as response:
                if response.status == 200:
                    data = await response.json()
                    growth_time = data.get('growth_time')
                    name = berry['name']
                    return growth_time, name
        except aiohttp.ClientError as e:
            print(f"Error fetching data for {berry['name']}: {e}")
        return None, None

    async def get_stats(self, berries: list) -> dict:
        '''
        Gets the statistics for the berries.
        
        Args:
            berries (list): The list of berries.
            
        Returns:
            dict: The statistics for the berries in a human-readable way.
        '''
        try: 
            growth_times = []
            names = []
            
            # Use asyncio to fetch the berry data concurrently to make non blocking I/O http requests
            async with aiohttp.ClientSession() as session:
                tasks = []
                for berry in berries:
                    tasks.append(self._fetch_berry_data(session, berry))  

                results = await asyncio.gather(*tasks)
                for growth_time, name in results:
                    if growth_time is not None and name is not None:
                        growth_times.append(growth_time)
                        names.append(name)

            if not growth_times:
                return {}
            else:
                return self._calculate_stats(growth_times, names)
        except Exception as e:
            print(f"Error getting berry statistics: {e}")
            return {}

    def _calculate_stats(self, growth_times: list, names: list) -> dict:    
        '''
        Calculates the statistics for the berries.
        
        Args:
            growth_times (list): The list of growth times.
            names (list): The list of names.
        
        Returns:
            dict: The statistics for the berries in a human-readable way.
        
        '''
        def _add_berries_suffix(growth_times: list) -> dict:
                '''
                Adds the 'berry' or 'berries' suffix to the growth times.
                
                Args:
                    growth_times (list): The list of growth times.
                    
                Returns:
                    dict: The growth times with the 'berry' or 'berries' suffix.
                '''
                try: 
                    frequency_growth_time = {time: growth_times.count(time) for time in set(growth_times)}
                    frequency_growth_time = {f"{time} days": frequency for time, frequency in frequency_growth_time.items()}
                    frequency_growth_time_with_berries = {key: f"{value} {'berry' if value == 1 else 'berries'}" for key, value in frequency_growth_time.items()}
                    
                    return frequency_growth_time_with_berries
                except Exception as e:
                    print(f"Error adding suffix: {e}")
                    return {}

        try: 
            frequency_growth_time_hr = _add_berries_suffix(growth_times)

            self.stats = {
                "berries_names": sorted(names),
                "min_growth_time": f"{min(growth_times)} days",
                "median_growth_time": f"{round(statistics.median(growth_times))} days",
                "max_growth_time": f"{max(growth_times)} days",
                "variance_growth_time": round(statistics.variance(growth_times), 3),
                "mean_growth_time": f"{round(statistics.mean(growth_times))} days",
                "frequency_growth_time": frequency_growth_time_hr
            }

            return self.stats  
        except Exception as e:
            print(f"Error calculating berry statistics: {e}")
            return {}
    
router = APIRouter(prefix="/api/v1", tags=["Get all berry stats"], responses={404: {"description": "Not found"}})

@router.get("/allBerryStats", status_code=status.HTTP_200_OK, response_description="Get all berry stats")
async def get_all_berry_stats() -> JSONResponse:
    try:
        api_url = os.getenv('POKEBERRIES_API_URL')
        if not api_url:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Missing API URL")

        fetcher = BerryFetcher(api_url)
        stats_calculator = BerryStatisticsCalculator()

        berries = fetcher.fetch()
        stats = await stats_calculator.get_stats(berries)

        response_content = {'error': False, 'data': stats}
        return JSONResponse(content=response_content, status_code=status.HTTP_200_OK)
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
