#!/usr/bin/env python3
"""
SEO Analysis Data Extraction and Standardization - Phase 2
=========================================================

This script handles:
- Excel and CSV data processing with proper encoding
- Date format standardization
- Data cleaning and transformation
- PDF data extraction planning

Author: GitHub Copilot Assistant
Date: October 22, 2025
"""

import os
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class SEODataProcessor:
    """Main class for processing SEO data from multiple sources"""
    
    def __init__(self):
        self.processed_data = {}
        self.data_issues = []
        
    def process_google_analytics(self):
        """Process Google Analytics Excel files"""
        print("\n=== Processing Google Analytics Data ===")
        
        # Process Pages and Screens data
        print("\n1. Processing Pages and Screens data...")
        try:
            # Read the file, skipping header rows
            ga_pages = pd.read_excel(
                'google_analytics/Pages and screens_ Page path and screen class.xlsx',
                sheet_name=0
            )
            
            # Display initial structure
            print(f"   Initial shape: {ga_pages.shape}")
            print(f"   Columns: {list(ga_pages.columns)[:5]}...")
            
            # Clean the data - find actual header row
            # Usually GA exports have multiple header rows
            header_row = None
            for idx, row in ga_pages.iterrows():
                if 'Page path' in str(row.values) or 'Page' in str(row.values):
                    header_row = idx
                    break
            
            if header_row is not None:
                print(f"   Found header at row {header_row}")
                # Re-read with proper header
                ga_pages = pd.read_excel(
                    'google_analytics/Pages and screens_ Page path and screen class.xlsx',
                    sheet_name=0,
                    header=header_row
                )
                
            print(f"   Processed shape: {ga_pages.shape}")
            print(f"   Columns: {list(ga_pages.columns)}")
            
            # Save processed data
            ga_pages.to_csv('analysis/processed_data/ga_pages_raw.csv', index=False)
            self.processed_data['ga_pages'] = ga_pages
            print("   ✓ Saved to: analysis/processed_data/ga_pages_raw.csv")
            
        except Exception as e:
            error_msg = f"Error processing GA Pages data: {str(e)}"
            print(f"   ❌ {error_msg}")
            self.data_issues.append(error_msg)
        
        # Process Traffic Acquisition data
        print("\n2. Processing Traffic Acquisition data...")
        try:
            ga_traffic = pd.read_excel(
                'google_analytics/Traffic acquisition_ Session primary channel group (Default Channel Group).xlsx',
                sheet_name=0
            )
            
            print(f"   Initial shape: {ga_traffic.shape}")
            
            # Find header row
            header_row = None
            for idx, row in ga_traffic.iterrows():
                if 'channel' in str(row.values).lower() or 'session' in str(row.values).lower():
                    header_row = idx
                    break
            
            if header_row is not None:
                print(f"   Found header at row {header_row}")
                ga_traffic = pd.read_excel(
                    'google_analytics/Traffic acquisition_ Session primary channel group (Default Channel Group).xlsx',
                    sheet_name=0,
                    header=header_row
                )
            
            print(f"   Processed shape: {ga_traffic.shape}")
            print(f"   Columns: {list(ga_traffic.columns)}")
            
            ga_traffic.to_csv('analysis/processed_data/ga_traffic_raw.csv', index=False)
            self.processed_data['ga_traffic'] = ga_traffic
            print("   ✓ Saved to: analysis/processed_data/ga_traffic_raw.csv")
            
        except Exception as e:
            error_msg = f"Error processing GA Traffic data: {str(e)}"
            print(f"   ❌ {error_msg}")
            self.data_issues.append(error_msg)
    
    def process_google_search_console(self):
        """Process Google Search Console Excel files"""
        print("\n=== Processing Google Search Console Data ===")
        
        # Process Performance data
        print("\n1. Processing Search Performance data...")
        try:
            gsc_perf = pd.read_excel(
                'google_search_console/https___hbno.com_-Performance-on-Search-2025-10-22.xlsx',
                sheet_name='Queries'
            )
            
            print(f"   Shape: {gsc_perf.shape}")
            print(f"   Columns: {list(gsc_perf.columns)}")
            
            # Display sample data
            if len(gsc_perf) > 0:
                print(f"   Sample data:")
                print(gsc_perf.head(3).to_string())
            
            gsc_perf.to_csv('analysis/processed_data/gsc_queries.csv', index=False)
            self.processed_data['gsc_queries'] = gsc_perf
            print("   ✓ Saved to: analysis/processed_data/gsc_queries.csv")
            
            # Process Pages sheet
            try:
                gsc_pages = pd.read_excel(
                    'google_search_console/https___hbno.com_-Performance-on-Search-2025-10-22.xlsx',
                    sheet_name='Pages'
                )
                print(f"\n2. Processing Pages data...")
                print(f"   Shape: {gsc_pages.shape}")
                gsc_pages.to_csv('analysis/processed_data/gsc_pages.csv', index=False)
                self.processed_data['gsc_pages'] = gsc_pages
                print("   ✓ Saved to: analysis/processed_data/gsc_pages.csv")
            except:
                print("   ℹ Pages sheet not found or empty")
            
            # Process Dates sheet for time series data
            try:
                gsc_dates = pd.read_excel(
                    'google_search_console/https___hbno.com_-Performance-on-Search-2025-10-22.xlsx',
                    sheet_name='Dates'
                )
                print(f"\n3. Processing Dates (time series) data...")
                print(f"   Shape: {gsc_dates.shape}")
                print(f"   Columns: {list(gsc_dates.columns)}")
                
                # Convert date column if present
                if 'Date' in gsc_dates.columns or 'date' in gsc_dates.columns:
                    date_col = 'Date' if 'Date' in gsc_dates.columns else 'date'
                    gsc_dates[date_col] = pd.to_datetime(gsc_dates[date_col])
                    print(f"   Date range: {gsc_dates[date_col].min()} to {gsc_dates[date_col].max()}")
                
                gsc_dates.to_csv('analysis/processed_data/gsc_dates_timeseries.csv', index=False)
                self.processed_data['gsc_dates'] = gsc_dates
                print("   ✓ Saved to: analysis/processed_data/gsc_dates_timeseries.csv")
            except Exception as e:
                print(f"   ℹ Dates sheet issue: {str(e)}")
            
        except Exception as e:
            error_msg = f"Error processing GSC Performance data: {str(e)}"
            print(f"   ❌ {error_msg}")
            self.data_issues.append(error_msg)
        
        # Process Core Web Vitals data
        print("\n4. Processing Core Web Vitals data...")
        try:
            cwv_data = pd.read_excel(
                'google_search_console/https___hbno.com_-core-web-vitals-2025-10-22.xlsx',
                sheet_name='Table'
            )
            
            print(f"   Shape: {cwv_data.shape}")
            print(f"   Columns: {list(cwv_data.columns)}")
            
            # Convert Date column
            if 'Date' in cwv_data.columns:
                cwv_data['Date'] = pd.to_datetime(cwv_data['Date'])
                print(f"   Date range: {cwv_data['Date'].min()} to {cwv_data['Date'].max()}")
            
            cwv_data.to_csv('analysis/processed_data/core_web_vitals.csv', index=False)
            self.processed_data['core_web_vitals'] = cwv_data
            print("   ✓ Saved to: analysis/processed_data/core_web_vitals.csv")
            
        except Exception as e:
            error_msg = f"Error processing Core Web Vitals: {str(e)}"
            print(f"   ❌ {error_msg}")
            self.data_issues.append(error_msg)
    
    def process_ahrefs_csv(self):
        """Process Ahrefs CSV files with proper encoding detection"""
        print("\n=== Processing Ahrefs CSV Data ===")
        
        # Try different encodings for CSV files
        encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252', 'utf-16']
        
        # Process Organic Keywords
        print("\n1. Processing Organic Keywords data...")
        csv_file = 'ahrefs/hbnobulk.com-organic-keywords-subdomains-al_2025-10-22_19-38-50.csv'
        
        for encoding in encodings:
            try:
                print(f"   Trying encoding: {encoding}")
                keywords_df = pd.read_csv(csv_file, encoding=encoding)
                
                print(f"   ✓ Success with {encoding}")
                print(f"   Shape: {keywords_df.shape}")
                print(f"   Columns: {list(keywords_df.columns)[:10]}")
                
                # Save processed data
                keywords_df.to_csv('analysis/processed_data/ahrefs_organic_keywords.csv', index=False, encoding='utf-8')
                self.processed_data['ahrefs_keywords'] = keywords_df
                print("   ✓ Saved to: analysis/processed_data/ahrefs_organic_keywords.csv")
                break
                
            except Exception as e:
                if encoding == encodings[-1]:
                    error_msg = f"All encodings failed for keywords CSV: {str(e)}"
                    print(f"   ❌ {error_msg}")
                    self.data_issues.append(error_msg)
                continue
        
        # Process Backlinks
        print("\n2. Processing Backlinks data...")
        csv_file = 'ahrefs/hbnobulk.com-backlinks-subdomains_2025-10-22_19-38-16.csv'
        
        for encoding in encodings:
            try:
                print(f"   Trying encoding: {encoding}")
                backlinks_df = pd.read_csv(csv_file, encoding=encoding)
                
                print(f"   ✓ Success with {encoding}")
                print(f"   Shape: {backlinks_df.shape}")
                print(f"   Columns: {list(backlinks_df.columns)[:10]}")
                
                backlinks_df.to_csv('analysis/processed_data/ahrefs_backlinks.csv', index=False, encoding='utf-8')
                self.processed_data['ahrefs_backlinks'] = backlinks_df
                print("   ✓ Saved to: analysis/processed_data/ahrefs_backlinks.csv")
                break
                
            except Exception as e:
                if encoding == encodings[-1]:
                    error_msg = f"All encodings failed for backlinks CSV: {str(e)}"
                    print(f"   ❌ {error_msg}")
                    self.data_issues.append(error_msg)
                continue
    
    def create_data_summary(self):
        """Create summary of all processed data"""
        print("\n=== Data Processing Summary ===")
        
        summary_lines = []
        summary_lines.append("# Phase 2: Data Processing Summary")
        summary_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        summary_lines.append("")
        
        summary_lines.append("## Processed Datasets")
        summary_lines.append("")
        
        for name, df in self.processed_data.items():
            summary_lines.append(f"### {name}")
            summary_lines.append(f"- Rows: {len(df):,}")
            summary_lines.append(f"- Columns: {len(df.columns)}")
            summary_lines.append(f"- Columns: {', '.join(list(df.columns)[:10])}")
            
            # Check for date columns
            date_cols = [col for col in df.columns if 'date' in col.lower()]
            if date_cols:
                summary_lines.append(f"- Date columns: {', '.join(date_cols)}")
                for date_col in date_cols:
                    try:
                        if pd.api.types.is_datetime64_any_dtype(df[date_col]):
                            summary_lines.append(f"  - {date_col} range: {df[date_col].min()} to {df[date_col].max()}")
                    except:
                        pass
            
            summary_lines.append("")
        
        if self.data_issues:
            summary_lines.append("## Data Issues")
            summary_lines.append("")
            for issue in self.data_issues:
                summary_lines.append(f"- {issue}")
            summary_lines.append("")
        
        summary_lines.append("## Next Steps")
        summary_lines.append("")
        summary_lines.append("- [ ] Review processed data for quality")
        summary_lines.append("- [ ] Extract data from PDF reports manually")
        summary_lines.append("- [ ] Begin Phase 3: Baseline analysis")
        
        summary_text = '\n'.join(summary_lines)
        
        with open('analysis/reports/phase2_processing_summary.md', 'w') as f:
            f.write(summary_text)
        
        print("\n✓ Processing summary saved to: analysis/reports/phase2_processing_summary.md")
        print(f"\nProcessed {len(self.processed_data)} datasets successfully")
        if self.data_issues:
            print(f"Found {len(self.data_issues)} issues to review")

def main():
    """Main execution for Phase 2"""
    
    print("=== SEO Analysis Phase 2: Data Extraction and Standardization ===")
    
    processor = SEODataProcessor()
    
    # Process all data sources
    processor.process_google_analytics()
    processor.process_google_search_console()
    processor.process_ahrefs_csv()
    
    # Create summary
    processor.create_data_summary()
    
    print("\n=== Phase 2 Complete ===")
    print("\nNext steps:")
    print("1. Review the processing summary report")
    print("2. Manually extract key metrics from Ahrefs PDF reports")
    print("3. Begin Phase 3: Baseline analysis")
    print("\nFiles are ready in: analysis/processed_data/")

if __name__ == "__main__":
    main()
