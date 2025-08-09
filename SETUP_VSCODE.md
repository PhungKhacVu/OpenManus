# Hướng dẫn chạy OpenManus trên VS Code Browser

## 🚀 Các cách mở VS Code Browser

### Phương pháp 1: Sử dụng github.dev
1. **Đẩy dự án lên GitHub**:
   ```bash
   git init
   git add .
   git commit -m "OpenManus project setup"
   git remote add origin https://github.com/your-username/your-repo.git
   git push -u origin main
   ```

2. **Mở trên VS Code Browser**:
   - Vào GitHub repo của bạn
   - Nhấn phím `.` → Mở github.dev
   - Hoặc truy cập: `https://github.dev/your-username/your-repo`

### Phương pháp 2: Sử dụng vscode.dev
1. Truy cập: https://vscode.dev
2. Mở folder từ máy tính local
3. Chọn thư mục `F:\Repos\OpenManus`

### Phương pháp 3: VS Code Desktop
1. Cài đặt VS Code từ: https://code.visualstudio.com/
2. Mở workspace file: `openmanus.code-workspace`

## ⚙️ Cấu hình dự án

### 1. Virtual Environment đã được tạo
- Path: `F:\Repos\OpenManus\venv`
- Python: 3.13.2
- Tất cả dependencies đã được cài đặt

### 2. Cấu hình LLM
File: `config/config.toml` đã được cấu hình để sử dụng Ollama:
```toml
[llm]
api_type = "ollama"
model = "llama3.2"
base_url = "http://localhost:11434/v1"
api_key = "ollama"
max_tokens = 4096
temperature = 0.0
```

### 3. Browser Automation
- Playwright đã được cài đặt
- Chromium, Firefox, và Webkit browsers đã sẵn sàng

## 🎯 Cách chạy dự án

### Với Ollama (Khuyến nghị)
1. **Cài đặt Ollama**:
   - Download từ: https://ollama.ai/
   - Chạy: `ollama pull llama3.2`

2. **Chạy OpenManus**:
   ```bash
   # Kích hoạt virtual environment
   venv\Scripts\activate
   
   # Chạy dự án
   python main.py
   ```

### Với API khác (OpenAI, Claude)
1. **Sửa file config**:
   ```toml
   [llm]
   model = "gpt-4o"
   base_url = "https://api.openai.com/v1"
   api_key = "your-actual-api-key"
   max_tokens = 4096
   temperature = 0.0
   ```

2. **Chạy dự án**:
   ```bash
   python main.py
   ```

## 🛠️ Các lệnh hữu ích

### Chạy các phiên bản khác nhau
```bash
# Version cơ bản
python main.py

# Version với MCP
python run_mcp.py

# Version multi-agent (thử nghiệm)
python run_flow.py
```

### Kiểm tra cài đặt
```bash
# Kiểm tra dependencies
python -c "import app; print('✅ Dependencies OK!')"

# Kiểm tra Manus agent
python -c "from app.agent.manus import Manus; print('✅ Manus OK!')"
```

## 📁 Cấu trúc dự án
```
F:\Repos\OpenManus\
├── app/                    # Core application
├── config/                 # Configuration files
├── venv/                   # Virtual environment
├── main.py                 # Main entry point
├── run_mcp.py             # MCP version
├── run_flow.py            # Multi-agent version
└── openmanus.code-workspace # VS Code workspace
```

## 🎉 Trạng thái hiện tại
- ✅ Dependencies đã cài đặt
- ✅ Virtual environment đã thiết lập
- ✅ Playwright browsers đã sẵn sàng
- ✅ Configuration đã được thiết lập
- ✅ Workspace VS Code đã được tạo
- ✅ Dự án sẵn sàng để chạy!

## 🔧 Troubleshooting

### Lỗi import module
```bash
pip install -r requirements.txt
```

### Lỗi Playwright
```bash
playwright install
```

### Lỗi Python version
```bash
# Dự án hỗ trợ Python 3.11-3.13
python --version
```
