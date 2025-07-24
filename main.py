import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from routers import password, geoip, password_strength

app = FastAPI(title="Securiti Tools API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(BASE_DIR, "templates")
static_dir = os.path.join(BASE_DIR, "static")

templates = Jinja2Templates(directory=templates_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(password.router)
app.include_router(geoip.router)
app.include_router(password_strength.router)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    print("DEBUG: Запит до кореневого шляху (/). Спроба відобразити index.html.")
    try:
        response = templates.TemplateResponse("index.html", {"request": request})
        print("DEBUG: TemplateResponse успішно створено.")
        return response
    except Exception as e:
        print(f"ERROR: Не вдалося відобразити index.html. Помилка: {e}")
        import traceback
        traceback.print_exc()
        return HTMLResponse(content=f"<h1>Помилка завантаження сторінки</h1><p>{e}</p><pre>{traceback.format_exc()}</pre>", status_code=500)
