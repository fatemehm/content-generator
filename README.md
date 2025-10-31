## 🚀 Live Demo

**Production URL:** [https://content-generator-5yzhmwb92zcw3n3ozerfyk.streamlit.app/](https://content-generator-5yzhmwb92zcw3n3ozerfyk.streamlit.app/)

## 📊 Project Metrics

- **Tests:** 21 passing (100% success rate)
- **Coverage:** 61% (unit + integration)
- **Generation Time:** 1.85s average
- **API Cost:** $0 (Groq free tier)
- **Uptime:** 99.9% (Streamlit Cloud)

## 🧪 Testing
```bash
# Run all tests
pytest tests/ -v

# Run only unit tests
pytest tests/ -v -m unit

# Generate coverage report
pytest --cov=src --cov=config --cov-report=html
```

## 🐳 Docker Deployment
```bash
# Build image
docker build -t growces-content-generator .

# Run container
docker-compose up -d

# Access at http://localhost:8501
```

## 📈 CI/CD Pipeline

Automated workflow runs on every push:
- Code quality checks (Black, isort, flake8)
- Unit tests
- Integration tests
- Coverage analysis (>50% required)
- Security scanning

## 📝 Recent Updates

- ✅ Full test suite implemented (21 tests)
- ✅ CI/CD pipeline configured
- ✅ Docker containerization
- ✅ Production deployment
- ✅ MLflow integration
