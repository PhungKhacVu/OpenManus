#!/usr/bin/env python3
"""
Demo script để test OpenManus setup
"""
import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

async def test_setup():
    """Test basic setup without requiring external services"""
    print("🚀 Testing OpenManus Setup...")
    
    try:
        # Test imports
        print("  ✅ Testing imports...")
        from app.config import Config
        from app.logger import logger
        print("  ✅ Core modules imported successfully")
        
        # Test config loading
        print("  ✅ Testing config loading...")
        config = Config()
        llm_config = config.llm.get('default')
        if llm_config:
            print(f"  ✅ Config loaded. LLM model: {llm_config.model}")
        else:
            print("  ✅ Config loaded successfully")
        
        # Test agent import
        print("  ✅ Testing agent import...")
        from app.agent.manus import Manus
        print("  ✅ Manus agent imported successfully")
        
        # Test dependencies
        print("  ✅ Testing key dependencies...")
        import playwright
        import browser_use
        import langchain_core
        print("  ✅ Key dependencies available")
        
        print("\n🎉 All tests passed! OpenManus is ready to run.")
        print("\n📋 Next steps:")
        print("  1. Cài đặt Ollama: https://ollama.ai/")
        print("  2. Chạy: ollama pull llama3.2")
        print("  3. Chạy: python main.py")
        print("  4. Hoặc mở VS Code Browser với openmanus.code-workspace")
        
    except Exception as e:
        print(f"❌ Setup test failed: {e}")
        print(f"💡 Try: pip install -r requirements.txt")
        return False
    
    return True

if __name__ == "__main__":
    asyncio.run(test_setup())
