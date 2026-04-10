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
        readme_content = "# Welcome to TaskTracker API\n\nBuka [/docs](/docs) untuk interaktif dokumentasi."
        
    safe_markdown = json.dumps(readme_content)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TaskTracker API - Advanced UI</title>
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Outfit:wght@500;700;800&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown-dark.min.css">
        <style>
            :root {{
                --bg-gradient: linear-gradient(135deg, #020617, #0f172a, #1e1b4b);
                --glass-bg: rgba(255, 255, 255, 0.03);
                --glass-border: rgba(255, 255, 255, 0.08);
            }}
            body {{
                font-family: 'Inter', sans-serif;
                background: var(--bg-gradient);
                color: #f8fafc;
                min-height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: flex-start;
                padding: 80px 20px;
                background-attachment: fixed;
            }}
            .app-wrapper {{
                max-width: 900px;
                width: 100%;
                animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
            }}
            .container {{
                background: var(--glass-bg);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border: 1px solid var(--glass-border);
                border-radius: 24px;
                padding: 60px;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255,255,255,0.1);
            }}
            @keyframes slideUp {{
                from {{ opacity: 0; transform: translateY(40px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            .header {{
                text-align: center;
                margin-bottom: 50px;
                padding-bottom: 40px;
                border-bottom: 1px solid var(--glass-border);
            }}
            .logo-title {{
                font-family: 'Outfit', sans-serif;
                font-size: 3.5rem;
                font-weight: 800;
                margin: 0 0 15px 0;
                background: linear-gradient(to right, #60a5fa, #c084fc, #ff7eb3);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: -1.5px;
            }}
            .subtitle {{
                font-size: 1.15rem;
                color: #94a3b8;
                margin-bottom: 35px;
            }}
            .btn-glow {{
                display: inline-block;
                background: linear-gradient(135deg, #2563eb, #7c3aed);
                color: white;
                padding: 16px 36px;
                text-decoration: none;
                border-radius: 50px;
                font-weight: 600;
                font-size: 1.1rem;
                letter-spacing: 0.5px;
                box-shadow: 0 10px 20px -10px rgba(124, 58, 237, 0.8);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }}
            .btn-glow:hover {{
                transform: translateY(-3px) scale(1.02);
                box-shadow: 0 15px 25px -10px rgba(124, 58, 237, 1);
                background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            }}
            .markdown-body {{
                background-color: transparent !important;
                color: #e2e8f0 !important;
                font-family: 'Inter', sans-serif;
                font-size: 1.05rem;
            }}
            .markdown-body h1, .markdown-body h2 {{
                border-bottom-color: var(--glass-border) !important;
                font-family: 'Outfit', sans-serif;
                color: #f8fafc;
            }}
            .markdown-body a {{ color: #60a5fa !important; }}
            .markdown-body pre {{
                background-color: rgba(0,0,0,0.5) !important;
                border: 1px solid var(--glass-border);
                border-radius: 14px;
            }}
            .markdown-body code {{
                background-color: rgba(255,255,255,0.1) !important;
            }}
            .markdown-body blockquote {{
                border-left-color: #7c3aed !important;
                color: #cbd5e1 !important;
                background: rgba(124, 58, 237, 0.05);
                padding: 16px 20px !important;
                border-radius: 0 12px 12px 0;
            }}
        </style>
    </head>
    <body>
        <div class="app-wrapper">
            <div class="container">
                <div class="header">
                    <h1 class="logo-title">TaskTracker API</h1>
                    <p class="subtitle">API Manajemen Tugas dengan performa tinggi & dokumentasi interaktif.</p>
                    <a href="/docs" class="btn-glow">Buka Interactive API (Swagger UI) ➔</a>
                </div>
                <div id="markdown-container" class="markdown-body"></div>
            </div>
        </div>
        <script>
            marked.setOptions({{ breaks: true, gfm: true }});
            const markdownContent = {safe_markdown};
            document.getElementById('markdown-container').innerHTML = marked.parse(markdownContent);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)