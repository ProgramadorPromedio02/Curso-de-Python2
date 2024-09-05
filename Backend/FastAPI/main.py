from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
  return 'Hello FastAPI!'

@app.get('/url')
async def url():
  return {'url_curso': 'https://mouredev.com/python'}

# Ejecutar servidor: uvicorn main:app --reload