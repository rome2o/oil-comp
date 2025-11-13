#!/usr/bin/env python3
"""
Export Jupyter Notebook to HTML with all outputs
"""

import subprocess
import sys
from pathlib import Path

# Paths
notebook_path = Path(__file__).parent / "analysis/notebooks/seo_analysis.ipynb"
output_dir = Path(__file__).parent / "analysis/reports"
output_html = output_dir / "seo_analysis_full_report.html"

# Ensure output directory exists
output_dir.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Exporting Notebook to HTML")
print("=" * 60)
print(f"Source: {notebook_path}")
print(f"Output: {output_html}")
print()

try:
    # Run nbconvert command
    cmd = [
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "html",
        "--output", str(output_html.absolute()),
        str(notebook_path.absolute())
    ]
    
    print("Running command:")
    print(" ".join(cmd))
    print()
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ SUCCESS!")
        print(f"\nFull report exported to: {output_html}")
        print(f"\nYou can open it in your browser:")
        print(f"  open {output_html}")
    else:
        print("❌ Export failed!")
        print("\nSTDOUT:", result.stdout)
        print("\nSTDERR:", result.stderr)
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTrying alternative method...")
    
    # Alternative: use nbconvert directly
    try:
        import nbconvert
        from nbconvert import HTMLExporter
        import nbformat
        
        print("Loading notebook...")
        with open(notebook_path, 'r') as f:
            nb = nbformat.read(f, as_version=4)
        
        print("Converting to HTML...")
        html_exporter = HTMLExporter()
        html_exporter.template_name = 'classic'
        
        (body, resources) = html_exporter.from_notebook_node(nb)
        
        print("Writing output...")
        with open(output_html, 'w') as f:
            f.write(body)
        
        print("✅ SUCCESS!")
        print(f"\nFull report exported to: {output_html}")
        print(f"\nYou can open it in your browser:")
        print(f"  open {output_html}")
        
    except Exception as e2:
        print(f"❌ Alternative method also failed: {e2}")
        print("\nPlease run: pip install nbconvert jupyter")
        sys.exit(1)

print("=" * 60)
