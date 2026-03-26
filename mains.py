
from fastapi import FastAPI, Depends, Request, Header, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from backend.security import encrypt_data
from backend.engine import UserMetrics, calculate_performance_score, generate_enhanced_recommendation
import os

API_KEYS = {"demo-key": "user1"}
limiter = Limiter(key_func=get_remote_address, default_limits=["100/hour"])
app = FastAPI(title="Human Performance OS")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, RateLimitExceeded().handler)

async def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return API_KEYS[x_api_key]

@app.get("/status")
async def health_check():
    return {"status": "healthy"}

@app.post("/evaluate")
@limiter.limit("10/minute")
async def evaluate_performance(
    metrics: UserMetrics,
    user_id: str = Depends(verify_api_key),
    _=Depends(lambda: None)  # Request for limiter
):
    encrypted_metrics = encrypt_data(metrics.dict())
    score = calculate_performance_score(metrics)
    recommendation = generate_enhanced_recommendation(metrics, score)
    
    return {
        "user_id": user_id,
        "encrypted_data": encrypted_metrics,
        "performance_score": score,
        "recommendation": recommendation
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
