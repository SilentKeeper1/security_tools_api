from fastapi import APIRouter, Query
import httpx

router = APIRouter()

@router.get("/geoip")
async def geoip_lookup(ip: str = Query(..., min_length=7, max_length=15)):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://ip-api.com/json/{ip}")
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error occurred: {e.response.status_code} - {e.response.text}"}
    except httpx.RequestError as e:
        return {"error": f"An error occurred while requesting GeoIP data: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}