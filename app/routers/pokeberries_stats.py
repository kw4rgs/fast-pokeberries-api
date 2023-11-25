from fastapi import APIRouter, status, HTTPException
import requests
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/v1", tags=["Get external endpoint data"], responses={404: {"description": "Not found"}})

@router.get("/allBerryStats", status_code=status.HTTP_200_OK, response_description="Get all berry stats")
async def read_all_berry_stats() -> JSONResponse:
    try:
        url = os.getenv('POKEBERRIES_API_URL')
        response = requests.get(url)
        response.raise_for_status() 
        response_content = {'error': False, 'data': response.json()['results']}
        return JSONResponse(content=response_content, status_code=status.HTTP_200_OK)
    except requests.exceptions.RequestException as e:
        response_content = {'error': True, 'detail': str(e)}
        return JSONResponse(content=response_content, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    