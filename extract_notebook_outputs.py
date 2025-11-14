#!/usr/bin/env python3
"""Extract outputs from Jupyter notebook and update report files."""

import json
import os
import sys

# Check for command-line argument
filter_cell = None
if len(sys.argv) > 1:
    filter_cell = sys.argv[1].lower()
    print(f"🔍 Filtering for cell: {filter_cell}")

# Read the notebook
with open('hbno_data_analysis.ipynb', 'r') as f:
    nb = json.load(f)

# Cell mapping: execution_count -> (report_number, report_name, section_title, cell_identifier)
cell_mapping = {
    33: (11, 'Revenue_Conversion_Performance', 'REVENUE & CONVERSION PERFORMANCE ANALYSIS', 'revenue'),
    34: (12, 'Traffic_SEO_Performance', 'TRAFFIC & SEO PERFORMANCE ANALYSIS', 'traffic'),
    72: (13, 'Geographic_Marketing_Attribution', 'GEOGRAPHIC & MARKETING ATTRIBUTION ANALYSIS', 'geography'),
    37: (14, 'Revenue_Optimization_Opportunities', 'REVENUE OPTIMIZATION OPPORTUNITIES', 'optimization'),
    38: (14, 'Revenue_Optimization_Opportunities', 'SHOPIFY PERFORMANCE VISUALIZATIONS', 'visualizations'),
    20: (15, 'Customer_Lifecycle_AOV_Analysis', 'SEO INTELLIGENCE DATA', 'seo'),
    62: (15, 'Customer_Lifecycle_AOV_Analysis', 'ENHANCED REVENUE OPTIMIZATION ANALYSIS', 'enhanced'),
    22: (15, 'Customer_Lifecycle_AOV_Analysis', 'ADVANCED CUSTOMER LIFECYCLE VISUALIZATIONS', 'lifecycle'),
    39: (2, 'SEO_Intelligence_Report', 'SEO OPPORTUNITIES ANALYSIS', 'seo-opportunities'),
    40: (2, 'SEO_Intelligence_Report', 'SEO SERVICE VALUE QUANTIFICATION', 'seo-value'),
    41: (1, 'Ultimate_Comprehensive_Analysis', 'COMPREHENSIVE SEO STRATEGY', 'seo-strategy'),
    42: (1, 'Ultimate_Comprehensive_Analysis', 'SERVICE RECOMMENDATION ENGINE', 'recommendations'),
    43: (1, 'Ultimate_Comprehensive_Analysis', 'ADVANCED SEO INTELLIGENCE', 'seo-intelligence'),
    52: (1, 'Ultimate_Comprehensive_Analysis', 'COMPREHENSIVE MARKDOWN REPORTS', 'reports'),
    56: (7, 'Super_Intelligence_AI_Analysis', 'SUPER INTELLIGENCE ANALYSIS', 'ai-analysis'),
    61: (7, 'Super_Intelligence_AI_Analysis', 'SUPER INTELLIGENCE AI INSIGHTS REPORT', 'ai-insights'),
}

# Extract outputs for each cell
extracted_outputs = {}

for cell in nb['cells']:
    if cell.get('cell_type') == 'code':
        exec_count = cell.get('execution_count')
        if exec_count in cell_mapping:
            report_num, report_name, section, cell_id = cell_mapping[exec_count]
            
            # Skip if filtering and this doesn't match
            if filter_cell and filter_cell not in cell_id.lower() and filter_cell not in section.lower():
                continue
            
            # Extract text output
            output_text = []
            if 'outputs' in cell and cell['outputs']:
                for output in cell['outputs']:
                    if 'text' in output:
                        output_text.append(''.join(output['text']))
                    elif 'data' in output and 'text/plain' in output['data']:
                        output_text.append(''.join(output['data']['text/plain']))
            
            if output_text:
                key = f"{report_num:02d}_{report_name}"
                if key not in extracted_outputs:
                    extracted_outputs[key] = []
                extracted_outputs[key].append({
                    'section': section,
                    'output': '\n'.join(output_text)
                })

# Print extracted outputs
for key in sorted(extracted_outputs.keys()):
    print(f"\n{'='*80}")
    print(f"REPORT: {key}")
    print('='*80)
    for item in extracted_outputs[key]:
        print(f"\n--- {item['section']} ---")
        print(item['output'])
        print()

# Save to files
reports_dir = 'reports'

if not extracted_outputs:
    print(f"\n⚠️  No matching cells found for filter: '{filter_cell}'")
    print(f"\nAvailable cell identifiers:")
    seen = set()
    for exec_count, (num, name, section, cell_id) in cell_mapping.items():
        if cell_id not in seen:
            print(f"  • {cell_id:<20} - {section}")
            seen.add(cell_id)
    sys.exit(1)

for key, items in extracted_outputs.items():
    report_file = f"{reports_dir}/{key}.md"
    if os.path.exists(report_file):
        # Read existing content
        with open(report_file, 'r') as f:
            existing_content = f.read()
        
        # Append new sections
        with open(report_file, 'a') as f:
            f.write('\n\n' + '='*80 + '\n')
            f.write(f'EXTRACTED NOTEBOOK OUTPUTS - {key}\n')
            f.write('='*80 + '\n\n')
            for item in items:
                f.write(f'\n## {item["section"]}\n\n')
                f.write('```\n')
                f.write(item['output'])
                f.write('\n```\n')
        
        print(f"✅ Updated: {report_file}")
    else:
        print(f"⚠️  Report file not found: {report_file}")
