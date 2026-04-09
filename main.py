from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import json
from database import engine, Base
from routers import auth, mata_kuliah, tugas
# Import models agar tabel terbuat di database
import models.user
import models.mata_kuliah
import models.tugas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskTracker API",
    description="API Manajemen Tugas Kuliah untuk UTS Pemrograman Web Lanjutan",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(mata_kuliah.router)
app.include_router(tugas.router)

@app.get("/", tags=["Root"])
def read_root():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
    except Exception:
        readme_content = "Selamat datang di TaskTracker API. Buka /docs untuk dokumentasi."
        
    safe_markdown = json.dumps(readme_content)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TaskTracker API - Beranda</title>
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                background-color: #f6f8fa;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
            }}
            .container {{
                max-width: 900px;
                width: 100%;
                background: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 1px solid #eaecef;
            }}
            .btn {{
                display: inline-block;
                background-color: #0969da;
                color: white;
                padding: 12px 24px;
                text-decoration: none;
                border-radius: 6px;
                font-weight: 600;
                font-size: 16px;
                transition: background-color 0.2s;
                margin-top: 10px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            .btn:hover {{
                background-color: #0550ae;
            }}
            .markdown-body {{
                box-sizing: border-box;
                min-width: 200px;
                max-width: 100%;
                margin: 0 auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <a href="/docs" class="btn">🚀 Buka Dokumentasi API (Swagger /docs) ➔</a>
            </div>
            <div id="markdown-container" class="markdown-body"></div>
        </div>
        <script>
            const markdownContent = {safe_markdown};
            document.getElementById('markdown-container').innerHTML = marked.parse(markdownContent);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)