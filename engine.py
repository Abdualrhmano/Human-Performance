# backend/engine.py
from pydantic import BaseModel
from typing import Dict, Any

class UserMetrics(BaseModel):
    sleep_hours: float
    focus_hours: float
    energy_level: float
    habit_consistency: float

def calculate_performance_score(metrics: UserMetrics) -> float:
    focus = max(0, min(10, metrics.focus_hours))
    energy = max(0, min(10, metrics.energy_level))
    consistency = max(0, min(1, metrics.habit_consistency))
    score = (focus * 0.4) + (energy * 0.3) + (consistency * 0.3 * 10)
    return round(score, 2)

def generate_enhanced_recommendation(metrics: UserMetrics, score: float) -> str:
    sleep_low = metrics.sleep_hours < 6
    energy_low = metrics.energy_level < 5
    focus_low = metrics.focus_hours < 2
    consistency_low = metrics.habit_consistency < 0.5
    
    insights = []
    
    # Pattern matching for interactions
    if sleep_low and energy_high := (metrics.energy_level > 7):
        insights.append("⚠️ Potential burnout: High energy despite low sleep - monitor caffeine/adrenaline.")
    elif sleep_low and energy_low:
        insights.append("Prioritize sleep recovery (7-9h) to restore energy baseline.")
    if focus_low:
        insights.append("Increase focused work blocks (Pomodoro: 25min x 4).")
    if consistency_low:
        insights.append("Build habit stack: 1-2min daily → scale up.")
    
    if score >= 8.0:
        base = "🚀 Elite Performance"
    elif score >= 6.0:
        base = "✅ Strong Performance"
    elif score >= 4.0:
        base = "⚡ Improving"
    else:
        base = "🔄 Recovery Mode"
    
    return f"{base} (Score: {score}/10)

" + "
".join(insights) if insights else f"{base} (Score: {score}/10). Maintain momentum!"
