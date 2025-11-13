# AI-Powered Deep Analysis with Google Gemini

## 10. AI-Powered Deep Analysis with Google Gemini

Using Google's Gemini AI to perform advanced analysis on different data segments and provide actionable insights.

```python
# Install and import Google Generative AI
try:
    import google.generativeai as genai
    print("✓ google-generativeai already installed")
except ImportError:
    print("Installing google-generativeai...")
    import sys
    !{sys.executable} -m pip install -q google-generativeai
    import google.generativeai as genai
    print("✓ google-generativeai installed successfully")

import os
from IPython.display import Markdown, display
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    print("✓ python-dotenv already installed")
except ImportError:
    print("Installing python-dotenv...")
    import sys
    !{sys.executable} -m pip install -q python-dotenv
    from dotenv import load_dotenv
    print("✓ python-dotenv installed successfully")

# Get the project root (two levels up from this notebook)
notebook_path = Path.cwd()
project_root = notebook_path.parent.parent
dotenv_path = project_root / '.env'

print(f"📂 Notebook location: {notebook_path}")
print(f"📂 Project root: {project_root}")
print(f"📂 Looking for .env at: {dotenv_path}")

if dotenv_path.exists():
    load_dotenv(dotenv_path)
    print(f"✓ Loaded environment variables from .env file")
else:
    print(f"⚠️  .env file not found at: {dotenv_path}")

# Ensure all required data is loaded
print("\nChecking required data...")
required_vars = ['gsc_dates', 'gsc_queries', 'ahrefs_keywords', 'ahrefs_backlinks', 
                 'theme_impact', 'allen_comparison', 'pre_theme', 'post_theme',
                 'previous_agency', 'allen_pre_theme', 'metrics']

missing_vars = [var for var in required_vars if var not in globals()]

if missing_vars:
    print(f"⚠️  Missing required variables: {', '.join(missing_vars)}")
    print("Please run all previous analysis cells before running AI analysis.")
else:
    print("✓ All required data is available")

# Configure API key
try:
    api_key = os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        print("\n⚠️  GOOGLE_API_KEY not found in environment variables.")
        print(f"Please ensure .env file exists at: {dotenv_path}")
        print("With content: GOOGLE_API_KEY='your-api-key-here'")
        print("\nOr uncomment the line below and add your API key directly:")
        # api_key = "your-api-key-here"
    else:
        print(f"\n✓ GOOGLE_API_KEY found (length: {len(api_key)} characters)")
        genai.configure(api_key=api_key)
        print("✓ Google Gemini API configured successfully")
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.5-pro')
        print("✓ Gemini model initialized (gemini-2.5-pro)")
except Exception as e:
    print(f"\n❌ Error configuring Gemini: {e}")
    print("Please ensure you have a valid GOOGLE_API_KEY set.")

```

**Output:**

```
✓ google-generativeai already installed
✓ python-dotenv already installed
✓ Loaded environment variables from: /Users/ali/Sites/business/oil-company/seo/analysis/../../.env

Checking required data...
✓ All required data is available

⚠️  GOOGLE_API_KEY not found in environment variables.
Please create a .env file in the project root with:
GOOGLE_API_KEY='your-api-key-here'

Or uncomment the line below and add your API key directly:

```


---

[← Back to Index](./00_index.md)
