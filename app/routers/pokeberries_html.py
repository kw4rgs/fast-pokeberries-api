from fastapi import Request, APIRouter, status, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import io
import base64
import json
import matplotlib.pyplot as plt
from app.routers.pokeberries_stats import get_all_berry_stats

class DataRetriever:
    async def retrieve_berry_stats(self) -> dict:
        '''
        Retrieves the berry statistics from the Pokeberries API
        
        Returns:    
            dict: The berry statistics
        '''
        try:
            response = await get_all_berry_stats()
            if isinstance(response, JSONResponse):
                data = json.loads(response.body.decode('utf-8')).get('data', {})
                return data if data is not None else {}
            else:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected response type")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

class Plotter:
    def create_histogram(self, data: dict) -> str:
        '''
        Creates a histogram of the frequency distribution of the berry growth times
        
        Args:
            data (dict): The data to be plotted
        
        Returns:
            str: The base64 encoded image data
        '''
        try:
            growth_times = list(data.get('frequency_growth_time', {}).keys())
            frequency = [int(value.split()[0]) for value in data.get('frequency_growth_time', {}).values()]
            plt.figure(figsize=(11, 5))
            plt.bar(growth_times, frequency, color='skyblue')
            plt.xlabel('Growth Time')
            plt.ylabel('Berries Qty')
            plt.title('Frequency Distribution of Berry Growth Time')
            plt.tight_layout()

            # Encode image to base64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close()

            return plot_data
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
templates = Jinja2Templates(directory="app/templates")
router = APIRouter(responses={404: {"description": "Not found"}})

@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK, tags=["Berry Histogram"])
async def berry_histogram(request: Request) -> HTMLResponse:
    data_retriever = DataRetriever()
    plotter = Plotter()
    try:
        all_data = await data_retriever.retrieve_berry_stats()
        plot_data = plotter.create_histogram(all_data)
        return templates.TemplateResponse("index.html", {"request": request, "all_data": all_data, "plot_data": plot_data})
    except HTTPException as e: 
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": str(e.detail)})
