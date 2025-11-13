#!/usr/bin/env python3
"""Extract outputs from Jupyter notebook and update report files."""

import json
import os

# Read the notebook
with open('hbno_data_analysis.ipynb', 'r') as f:
    nb = json.load(f)

# Cell mapping: execution_count -> (report_number, report_name, section_title)
cell_mapping = {
    33: (11, 'Revenue_Conversion_Performance', 'REVENUE & CONVERSION PERFORMANCE ANALYSIS'),
    34: (12, 'Traffic_SEO_Performance', 'TRAFFIC & SEO PERFORMANCE ANALYSIS'),
    35: (13, 'Geographic_Marketing_Attribution', 'GEOGRAPHIC & MARKETING ATTRIBUTION ANALYSIS'),
    37: (14, 'Revenue_Optimization_Opportunities', 'REVENUE OPTIMIZATION OPPORTUNITIES'),
    38: (14, 'Revenue_Optimization_Opportunities', 'SHOPIFY PERFORMANCE VISUALIZATIONS'),
    20: (15, 'Customer_Lifecycle_AOV_Analysis', 'SEO INTELLIGENCE DATA'),
    62: (15, 'Customer_Lifecycle_AOV_Analysis', 'ENHANCED REVENUE OPTIMIZATION ANALYSIS'),
    22: (15, 'Customer_Lifecycle_AOV_Analysis', 'ADVANCED CUSTOMER LIFECYCLE VISUALIZATIONS'),
    39: (2, 'SEO_Intelligence_Report', 'SEO OPPORTUNITIES ANALYSIS'),
    40: (2, 'SEO_Intelligence_Report', 'SEO SERVICE VALUE QUANTIFICATION'),
    41: (1, 'Ultimate_Comprehensive_Analysis', 'COMPREHENSIVE SEO STRATEGY'),
    42: (1, 'Ultimate_Comprehensive_Analysis', 'SERVICE RECOMMENDATION ENGINE'),
    43: (1, 'Ultimate_Comprehensive_Analysis', 'ADVANCED SEO INTELLIGENCE'),
    52: (1, 'Ultimate_Comprehensive_Analysis', 'COMPREHENSIVE MARKDOWN REPORTS'),
    56: (7, 'Super_Intelligence_AI_Analysis', 'SUPER INTELLIGENCE ANALYSIS'),
    61: (7, 'Super_Intelligence_AI_Analysis', 'SUPER INTELLIGENCE AI INSIGHTS REPORT'),
}

# Extract outputs for each cell
extracted_outputs = {}

for cell in nb['cells']:
    if cell.get('cell_type') == 'code':
        exec_count = cell.get('execution_count')
        if exec_count in cell_mapping:
            report_num, report_name, section = cell_mapping[exec_count]
            
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
for key, items in extracted_outputs.items():
    report_file = f"{reports_dir}/{key}.md"
    if os.path.exists(report_file):
        print(f"Would update: {report_file}")
    else:
        print(f"Warning: Report file not found: {report_file}")
