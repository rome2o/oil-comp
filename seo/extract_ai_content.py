#!/usr/bin/env python3
"""
Extract AI-generated content from HTML export
"""

from pathlib import Path
from bs4 import BeautifulSoup
import re

# Paths
html_path = Path(__file__).parent / "analysis/notebooks/seo_analysis.html"
output_dir = Path(__file__).parent / "analysis/reports/markdown_docs"

print("=" * 60)
print("Extracting AI-Generated Content from HTML")
print("=" * 60)
print(f"Source: {html_path}")
print(f"Output: {output_dir}")
print()

if not html_path.exists():
    print(f"❌ HTML file not found: {html_path}")
    print("Please export the notebook to HTML first")
    exit(1)

# Load HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all cells
cells = soup.find_all('div', class_='jp-Cell')

print(f"Found {len(cells)} cells in HTML")
print()

# Track AI analysis sections
ai_sections = []
current_section = None
in_ai_section = False

for cell in cells:
    # Check if it's a markdown cell with AI section header
    if 'jp-MarkdownCell' in cell.get('class', []):
        text = cell.get_text().strip()
        
        # Check for AI analysis section markers
        if 'Analysis #' in text or 'Helper Functions for AI Analysis' in text or 'Strategic SEO Roadmap' in text or 'Save AI Analysis Reports' in text:
            if current_section:
                ai_sections.append(current_section)
            
            # Extract section title
            lines = text.split('\n')
            title = lines[0].strip('#').strip()
            
            current_section = {
                'title': title,
                'content': [f"# {title}\n\n"]
            }
            in_ai_section = True
            print(f"📝 Found AI section: {title}")
    
    # Check if it's a code cell output
    elif in_ai_section and 'jp-CodeCell' in cell.get('class', []):
        # Find the output area
        output_area = cell.find('div', class_='jp-Cell-outputArea')
        if output_area:
            # Look for text outputs
            outputs = output_area.find_all('div', class_='jp-OutputArea-output')
            for output in outputs:
                text = output.get_text().strip()
                if text and len(text) > 50:  # Only capture substantial outputs
                    # Clean up the text
                    text = text.replace('🔍 Analyzing', '## 🔍 Analysis Results\n\n')
                    text = text.replace('🤖', '## 🤖')
                    text = text.replace('='*80, '')
                    text = re.sub(r'\n{3,}', '\n\n', text)  # Remove excessive newlines
                    
                    if current_section:
                        current_section['content'].append(text + "\n\n")

# Add last section
if current_section:
    ai_sections.append(current_section)

print(f"\n✅ Found {len(ai_sections)} AI-generated sections")
print()

# Save AI sections
if ai_sections:
    print("Creating AI analysis files...\n")
    
    # Create AI subdirectory
    ai_dir = output_dir / "ai_analysis"
    ai_dir.mkdir(parents=True, exist_ok=True)
    
    # Create index
    index_content = ["# AI-Generated Analysis Results\n\n"]
    index_content.append("This directory contains the AI-generated insights from Google Gemini 2.5 Pro.\n\n")
    index_content.append("## Analysis Sections\n\n")
    
    for i, section in enumerate(ai_sections, 1):
        filename = f"{i:02d}_{re.sub(r'[^a-z0-9]+', '-', section['title'].lower()).strip('-')}.md"
        index_content.append(f"{i}. [{section['title']}](./{filename})\n")
        
        # Write section file
        filepath = ai_dir / filename
        content = ''.join(section['content'])
        
        # Add navigation
        content += "\n\n---\n\n"
        content += "[← Back to AI Analysis Index](./00_index.md) | "
        content += "[← Back to Main Documentation](../00_index.md)\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created: {filename}")
    
    # Write AI index
    index_content.append("\n---\n\n")
    index_content.append("[← Back to Main Documentation](../00_index.md)\n")
    
    index_path = ai_dir / "00_index.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(''.join(index_content))
    
    print(f"\n✓ Created: 00_index.md")
    
    # Update main index
    main_index_path = output_dir / "00_index.md"
    if main_index_path.exists():
        with open(main_index_path, 'r', encoding='utf-8') as f:
            main_index = f.read()
        
        # Add AI section link if not already there
        if 'ai_analysis' not in main_index:
            ai_link = "\n\n## AI-Generated Analysis\n\n"
            ai_link += "📊 [View AI-Powered Deep Analysis Results](./ai_analysis/00_index.md)\n\n"
            ai_link += "*Includes strategic insights, recommendations, and detailed analysis from Google Gemini 2.5 Pro*\n"
            
            # Insert before the end
            main_index = main_index.rstrip() + "\n" + ai_link
            
            with open(main_index_path, 'w', encoding='utf-8') as f:
                f.write(main_index)
            
            print("\n✓ Updated main index with AI analysis link")
    
    print()
    print("=" * 60)
    print("✅ AI Content Extraction Complete!")
    print("=" * 60)
    print(f"\nAI analysis files created in: {ai_dir}")
    print(f"Total files: {len(ai_sections) + 1} (including index)")
    print("\nView the AI insights:")
    print(f"  {ai_dir / '00_index.md'}")
    print("=" * 60)
else:
    print("⚠️  No AI-generated content found in HTML")
    print("Make sure to run the AI analysis cells in the notebook first")
