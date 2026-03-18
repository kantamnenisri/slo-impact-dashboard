from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from app.calculator import calculate_slo_metrics

app = FastAPI(title="SLO Business Impact Dashboard")

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SLOCalculationRequest(BaseModel):
    service_name: str
    slo_target: float = Field(..., gt=0, lt=100)
    current_uptime: float = Field(..., gt=0, lt=100)
    monthly_revenue: float = Field(..., gt=0)
    monthly_traffic: int = Field(..., gt=0)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "slo-dashboard-api"}

@app.get("/ping")
async def ping():
    return "OK"

@app.post("/calculate")
def calculate_metrics(data: SLOCalculationRequest):
    try:
        results = calculate_slo_metrics(
            service_name=data.service_name,
            slo_target=data.slo_target,
            current_uptime=data.current_uptime,
            monthly_revenue=data.monthly_revenue,
            monthly_traffic=data.monthly_traffic
        )
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Serve static files from the frontend directory
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
