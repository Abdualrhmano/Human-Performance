
<div align="center">

# 🚀 Human Performance OS
## محرك الأداء البشري الذكي مع تشفير Zero-Trust

[![Status][status-badge]][status-url] [![Docker][docker-badge]][docker-url] [![FastAPI][fastapi-badge]][fastapi-url] [![Streamlit][streamlit-badge]][streamlit-url]

**نظام ذكي يحلل أداءك اليومي ويعطيك توصيات مخصصة مع تشفير البيانات AES-256**

![Demo Screenshot](https://via.placeholder.com/1200x600/1e3a8a/ffffff?text=Human+Performance+OS+Demo)

</div>

## ✨ **المميزات**

- 🔐 **Zero-Trust Security**: تشفير AES-256-GCM لبيانات السلوك
- 🧠 **AI Decision Engine**: تحليل تفاعلية بين النوم، التركيز، الطاقة، والعادات
- 📊 **Dashboard تفاعلي**: Streamlit مع Gauge Charts
- 🛡️ **Rate Limiting**: حماية من DDoS (10 دقيقة/دقيقة)
- ⚡ **Production-Ready**: FastAPI Async + Docker Compose
- 🔍 **Burnout Detection**: كشف الإرهاق المبكر

## 🚀 **بدء التشغيل (Click-and-Run)**

### 🐳 **الطريقة الأسرع - Docker**
```bash
git clone <repo-url>
cd HumanPerformanceOS
docker compose up --build
```
**Backend:** http://localhost:8000/status  
**Frontend:** http://localhost:8501

### 🐍 **Local Development**
```bash
# Terminal 1 - Backend
cd backend && pip install -r ../requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Frontend
pip install -r requirements_streamlit.txt
streamlit run app_ui.py --server.port 8501
```

## 📱 **استخدام الـ Demo**

1. **افتح** http://localhost:8501
2. **اضبط** الـ Sliders (النوم، التركيز، الطاقة، الاتساق)
3. **اضغط** "🧠 Calculate Performance"
4. **شوف** النتيجة + التوصيات الذكية
5. **افتح** "🔒 Security View" للتشفير

## 🛠 **هيكل المشروع**

```
HumanPerformanceOS/
├── backend/                 # FastAPI Backend
│   ├── main.py             # API Endpoints
│   ├── security.py         # AES-256 Encryption
│   ├── engine.py           # AI Scoring + ReAct Logic
│   └── __init__.py
├── app_ui.py              # Streamlit Frontend
├── docker-compose.yml     # One-Command Deployment
├── Dockerfile*            # Backend Container
└── requirements*.txt      # Dependencies
```

## 🔑 **API Documentation**

```bash
# Health Check
curl http://localhost:8000/status

# Performance Evaluation
curl -X POST "http://localhost:8000/evaluate" \
  -H "X-API-Key: demo-key" \
  -H "Content-Type: application/json" \
  -d '{"sleep_hours":7.5,"focus_hours":4,"energy_level":6,"habit_consistency":0.8}'
```

**Response:**
```json
{
  "user_id": "user1",
  "encrypted_data": "AE...==",
  "performance_score": 6.24,
  "recommendation": "✅ جيد (النتيجة: 6.24/10)"
}
```

## 🛡️ **طبقة الأمان (LUNA-Inspired)**

| Feature | Protection |
|---------|------------|
| **AES-256-GCM** | تشفير البيانات الحساسة |
| **API Key Auth** | التحقق من الهوية |
| **Rate Limiting** | 100/ساعة، 10/دقيقة |
| **Input Sanitization** | Pydantic + Bounds Checking |
| **Prompt Injection** | Template-based ReAct |

## 🎯 **Demo Script للـ Chairman**

```
1. "ده نظام يحلل الأداء البشري بذكاء اصطناعي"
2. حرك الـ Sliders → Calculate 
3. "شوف النتيجة الذكية + كشف الإرهاق"
4. افتح Security View → "البيانات مشفرة AES-256"
5. "Production-ready في Docker ثواني"
```

## 📈 **Performance Score Formula**

```
S = (Focus × 0.4) + (Energy × 0.3) + (Consistency × 0.3 × 10)
```

**Pattern Detection:**
- نوم قليل + طاقة عالية = ⚠️ إرهاق محتمل
- تركيز منخفض = 💡 Pomodoro موصى

## 🔌 **الاعتماديات**

| Backend | Frontend |
|---------|----------|
| FastAPI 0.115 | Streamlit 1.38 |
| Pydantic 2.9 | Requests 2.32 |
| Cryptography 43 | streamlit-gauge |
| SlowAPI 0.1.9 | |

## 🤝 **المساهمة**

1. Fork الـ Repository
2. أنشئ Feature Branch
3. Commit التغييرات
4. Push + Pull Request

## 📄 **الترخيص**

[MIT License](LICENSE) - استخدم بحرية في المشاريع التجارية

## 👨‍💻 **المطور**

**Senior AI Solutions Architect**  
[Perplexity AI] | [LinkedIn] | [Portfolio]

<div align="center">
  
**⭐ Star the repo إذا عجبك المشروع!**
  
![Footer](https://via.placeholder.com/1200x100/0f172a/ffffff?text=Production-Ready+AI+Performance+Engine+%7C+March+2026)

</div>
