# 1 Helper Functions for AI Analysis

### 10.1 Helper Functions for AI Analysis

```python
def prepare_data_context(dataframe, description, max_rows=50):
    """
    Prepare data context for AI analysis by formatting dataframe information
    """
    context = f"{description}\n\n"
    context += f"Data Shape: {dataframe.shape[0]} rows × {dataframe.shape[1]} columns\n\n"
    context += "Columns: " + ", ".join(dataframe.columns.tolist()) + "\n\n"
    context += "Sample Data (first few rows):\n"
    context += dataframe.head(max_rows).to_string() + "\n\n"
    context += "Statistical Summary:\n"
    context += dataframe.describe().to_string()
    return context

def analyze_with_gemini(prompt, data_context="", max_retries=3):
    """
    Send data and prompt to Gemini for analysis
    """
    try:
        full_prompt = f"{prompt}\n\n{data_context}" if data_context else prompt
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"❌ Error during AI analysis: {e}")
        return None

def display_ai_response(title, response):
    """
    Display AI response in a formatted way
    """
    print("\n" + "="*80)
    print(f"🤖 {title}")
    print("="*80)
    if response:
        display(Markdown(response))
    else:
        print("No response received.")
    print("="*80 + "\n")

print("✓ Helper functions defined successfully")
```


---

[← Back to Index](./00_index.md)
