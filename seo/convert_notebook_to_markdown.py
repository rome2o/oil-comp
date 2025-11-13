#!/usr/bin/env python3
"""
Convert Jupyter Notebook to organized Markdown files
"""

import json
import re
from pathlib import Path
from typing import List, Dict

# Paths
notebook_path = Path(__file__).parent / "analysis/notebooks/seo_analysis.ipynb"
output_dir = Path(__file__).parent / "analysis/reports/markdown_docs"

# Create output directory
output_dir.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Converting Notebook to Markdown Documentation")
print("=" * 60)
print(f"Source: {notebook_path}")
print(f"Output: {output_dir}")
print()

# Load notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Section tracking
sections = []
current_section = None
section_counter = 0

def sanitize_filename(text: str) -> str:
    """Convert text to valid filename"""
    # Remove special characters, keep alphanumeric and spaces
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Convert to lowercase
    return text.lower()

def format_code_cell(cell: Dict) -> str:
    """Format a code cell as markdown"""
    source = ''.join(cell.get('source', []))
    
    output_md = f"```python\n{source}\n```\n\n"
    
    # Add outputs if they exist
    outputs = cell.get('outputs', [])
    if outputs:
        output_md += "**Output:**\n\n"
        for output in outputs:
            if output.get('output_type') == 'stream':
                text = ''.join(output.get('text', []))
                output_md += f"```\n{text}\n```\n\n"
            elif output.get('output_type') == 'execute_result':
                data = output.get('data', {})
                if 'text/plain' in data:
                    text = ''.join(data['text/plain'])
                    output_md += f"```\n{text}\n```\n\n"
            elif output.get('output_type') == 'display_data':
                output_md += "*[Chart/Visualization displayed]*\n\n"
            elif output.get('output_type') == 'error':
                ename = output.get('ename', 'Error')
                evalue = output.get('evalue', '')
                output_md += f"```\nError: {ename}: {evalue}\n```\n\n"
    
    return output_md

def format_markdown_cell(cell: Dict) -> str:
    """Format a markdown cell"""
    source = ''.join(cell.get('source', []))
    return source + "\n\n"

# Process cells
for cell in notebook['cells']:
    cell_type = cell.get('cell_type')
    source = ''.join(cell.get('source', [])).strip()
    
    if not source:
        continue
    
    # Check if this is a new section (markdown cell starting with #)
    if cell_type == 'markdown' and source.startswith('#'):
        # Save previous section
        if current_section:
            sections.append(current_section)
        
        # Start new section
        section_counter += 1
        
        # Extract title (first line)
        lines = source.split('\n')
        title = lines[0].lstrip('#').strip()
        
        # Remove numbering if present (e.g., "1. Data Loading" -> "Data Loading")
        title_clean = re.sub(r'^\d+\.\s*', '', title)
        
        filename = f"{section_counter:02d}_{sanitize_filename(title_clean)}.md"
        
        current_section = {
            'title': title_clean,
            'filename': filename,
            'content': []
        }
        
        # Add the markdown header content
        current_section['content'].append(format_markdown_cell(cell))
    
    else:
        # Add to current section
        if current_section is None:
            # Create initial section if none exists
            section_counter += 1
            current_section = {
                'title': 'Introduction',
                'filename': f"{section_counter:02d}_introduction.md",
                'content': []
            }
        
        if cell_type == 'markdown':
            current_section['content'].append(format_markdown_cell(cell))
        elif cell_type == 'code':
            current_section['content'].append(format_code_cell(cell))

# Save last section
if current_section:
    sections.append(current_section)

# Write sections to files
print(f"Creating {len(sections)} markdown files...\n")

# Create index file
index_content = ["# SEO Analysis Documentation\n\n"]
index_content.append(f"**Analysis Date:** October 22, 2025\n\n")
index_content.append("## Contents\n\n")

for i, section in enumerate(sections, 1):
    index_content.append(f"{i}. [{section['title']}](./{section['filename']})\n")

# Write index
index_path = output_dir / "00_index.md"
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(''.join(index_content))
print(f"✓ Created: {index_path.name}")

# Write each section
for section in sections:
    filepath = output_dir / section['filename']
    
    content = [f"# {section['title']}\n\n"]
    content.extend(section['content'])
    
    # Add navigation footer
    content.append("\n---\n\n")
    content.append("[← Back to Index](./00_index.md)\n")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(''.join(content))
    
    print(f"✓ Created: {section['filename']}")

print()
print("=" * 60)
print("✅ Conversion Complete!")
print("=" * 60)
print(f"\nMarkdown files created in: {output_dir}")
print(f"Total files: {len(sections) + 1} (including index)")
print("\nYou can now:")
print(f"  1. View the index: {output_dir / '00_index.md'}")
print(f"  2. Share individual sections as needed")
print(f"  3. Commit to version control")
print("=" * 60)
