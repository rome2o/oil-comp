#!/usr/bin/env python3
"""
Process Fixed Ahrefs CSV Files
==============================
This script processes the fixed Ahrefs CSV files that were previously failing.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("=== Processing Fixed Ahrefs CSV Files ===\n")

# Process fixed organic keywords file
print("1. Processing Fixed Organic Keywords CSV...")
try:
    keywords_df = pd.read_csv('ahrefs/fixed_hbnobulk.com-organic-keywords-subdomains-al_2025-10-22_20-47-48.csv')
    
    print(f"   ✓ Successfully loaded")
    print(f"   Shape: {keywords_df.shape}")
    print(f"   Columns: {list(keywords_df.columns)[:15]}")
    print(f"\n   Sample data:")
    print(keywords_df.head(3).to_string())
    
    # Save processed version
    keywords_df.to_csv('analysis/processed_data/ahrefs_organic_keywords.csv', index=False)
    print(f"\n   ✓ Saved to: analysis/processed_data/ahrefs_organic_keywords.csv")
    
    # Key statistics
    print(f"\n   Key Statistics:")
    print(f"   - Total keywords: {len(keywords_df):,}")
    if 'Position' in keywords_df.columns:
        print(f"   - Keywords in top 10: {len(keywords_df[keywords_df['Position'] <= 10]):,}")
        print(f"   - Keywords in top 20: {len(keywords_df[keywords_df['Position'] <= 20]):,}")
    if 'Traffic' in keywords_df.columns:
        print(f"   - Total estimated traffic: {keywords_df['Traffic'].sum():,.0f}")
    
except Exception as e:
    print(f"   ❌ Error: {str(e)}")

print("\n" + "="*50)

# Process fixed backlinks file
print("\n2. Processing Fixed Backlinks CSV...")
try:
    backlinks_df = pd.read_csv('ahrefs/fixed_hbnobulk.com-backlinks-subdomains_2025-10-22_20-45-31.csv')
    
    print(f"   ✓ Successfully loaded")
    print(f"   Shape: {backlinks_df.shape}")
    print(f"   Columns: {list(backlinks_df.columns)[:15]}")
    print(f"\n   Sample data:")
    print(backlinks_df.head(3).to_string())
    
    # Save processed version
    backlinks_df.to_csv('analysis/processed_data/ahrefs_backlinks.csv', index=False)
    print(f"\n   ✓ Saved to: analysis/processed_data/ahrefs_backlinks.csv")
    
    # Key statistics
    print(f"\n   Key Statistics:")
    print(f"   - Total backlinks: {len(backlinks_df):,}")
    if 'Domain Rating' in backlinks_df.columns:
        print(f"   - Average Domain Rating: {backlinks_df['Domain Rating'].mean():.1f}")
    if 'Referring domains' in backlinks_df.columns or 'Ref domains' in backlinks_df.columns:
        ref_col = 'Referring domains' if 'Referring domains' in backlinks_df.columns else 'Ref domains'
        print(f"   - Unique referring domains: {backlinks_df[ref_col].nunique():,}")
    
except Exception as e:
    print(f"   ❌ Error: {str(e)}")

print("\n" + "="*50)
print("\n✓ Fixed Ahrefs files processed successfully!")
print("\nNext: Add these datasets to the main analysis notebook")
