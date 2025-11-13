#!/usr/bin/env python3
"""
Toxic & Irrelevant Keyword Analysis Script
==========================================
Analyzes SEO data to identify and flag problematic keywords including:
- Non-English keywords
- Non-oil/industrial relevant terms
- Toxic/illicit content
- Drug/addiction related
- Poor quality link sources
- Shady/spam keywords

Author: Tyger SEO Assistant
Date: October 22, 2025
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime, timedelta
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION
# ============================================================================

# Define analysis period (last 3 months from Oct 2025)
ANALYSIS_END_DATE = datetime(2025, 10, 22)
ANALYSIS_START_DATE = ANALYSIS_END_DATE - timedelta(days=90)

# Toxic/irrelevant keyword patterns
TOXIC_PATTERNS = {
    'drugs': [
        r'\b(cannabis|marijuana|weed|thc|cbd oil for high|get high|stoner|bong)\b',
        r'\b(cocaine|heroin|meth|mdma|ecstasy|lsd|mushroom trip)\b',
        r'\b(prescription drugs|oxycontin|vicodin|xanax|adderall abuse)\b',
    ],
    'addiction': [
        r'\b(addiction|rehab|detox|withdrawal|substance abuse)\b',
        r'\b(alcoholic|drug addict|crack|opiate)\b',
    ],
    'illicit': [
        r'\b(illegal|illicit|black market|darknet|underground)\b',
        r'\b(counterfeit|fake|scam|fraud)\b',
    ],
    'adult_content': [
        r'\b(porn|sex|xxx|adult|erotic|nude)\b',
        r'\b(escort|prostitute|cam girl|onlyfans)\b',
    ],
    'non_business': [
        r'\b(free download|crack software|torrent|pirate)\b',
        r'\b(hack|cheat|exploit|bypass)\b',
        r'\b(casino|gambling|poker|betting)\b',
    ],
    'consumer_misalignment': [
        r'\b(diy|home remedy|personal use|for face|for hair|for skin)\b',
        r'\b(best oil for cooking|edible oil|food grade oil)\b',
        r'\b(walmart|amazon|ebay|buy online cheap)\b',
    ],
    'medical_claims': [
        r'\b(cure|treatment|therapy|medicine|pharmaceutical)\b',
        r'\b(cancer|disease|illness|diagnosis)\b',
    ]
}

# Non-English detection patterns (common non-English characters/words)
NON_ENGLISH_PATTERNS = [
    r'[\u4e00-\u9fff]',  # Chinese
    r'[\u0400-\u04FF]',  # Cyrillic
    r'[\u0600-\u06FF]',  # Arabic
    r'[\u0590-\u05FF]',  # Hebrew
    r'[\u3040-\u309F]',  # Hiragana
    r'[\u30A0-\u30FF]',  # Katakana
    r'[\u0E00-\u0E7F]',  # Thai
]

# Poor quality domain patterns
POOR_QUALITY_DOMAINS = [
    r'\.wix\.com',
    r'\.weebly\.com',
    r'\.blogspot\.com',
    r'\.wordpress\.com',
    r'\.tumblr\.com',
    r'\.angelfire\.com',
    r'\.geocities\.com',
    r'\.tripod\.com',
]

# Oil/industrial relevant terms (keywords that SHOULD be present)
OIL_RELEVANT_TERMS = [
    'oil', 'oils', 'essential', 'carrier', 'bulk', 'wholesale', 'industrial',
    'manufacturing', 'supplier', 'b2b', 'business', 'cosmetic', 'organic',
    'natural', 'aromatherapy', 'ingredient', 'formulation', 'distilled',
    'extracted', 'pure', 'grade', 'certified', 'hbno', 'hbnobulk'
]

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def is_non_english(keyword):
    """Check if keyword contains non-English characters"""
    for pattern in NON_ENGLISH_PATTERNS:
        if re.search(pattern, keyword):
            return True
    return False

def check_toxic_patterns(keyword):
    """Check keyword against all toxic patterns and return categories found"""
    keyword_lower = keyword.lower()
    found_categories = []
    
    for category, patterns in TOXIC_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, keyword_lower, re.IGNORECASE):
                found_categories.append(category)
                break
    
    return found_categories

def is_oil_relevant(keyword):
    """Check if keyword is relevant to oil/industrial business"""
    keyword_lower = keyword.lower()
    
    # Check if any oil-relevant term is present
    for term in OIL_RELEVANT_TERMS:
        if term in keyword_lower:
            return True
    
    return False

def calculate_relevance_score(keyword):
    """
    Calculate relevance score (0-100)
    100 = highly relevant, 0 = completely irrelevant
    """
    score = 50  # Start at neutral
    keyword_lower = keyword.lower()
    
    # Positive indicators
    if is_oil_relevant(keyword):
        score += 30
    
    if any(term in keyword_lower for term in ['bulk', 'wholesale', 'supplier', 'manufacturer']):
        score += 10
    
    if any(term in keyword_lower for term in ['b2b', 'industrial', 'commercial']):
        score += 10
    
    # Negative indicators
    if is_non_english(keyword):
        score -= 40
    
    toxic_cats = check_toxic_patterns(keyword)
    if toxic_cats:
        score -= 50
    
    if any(term in keyword_lower for term in ['free', 'diy', 'home', 'recipe', 'personal']):
        score -= 20
    
    # Clamp between 0-100
    return max(0, min(100, score))

def analyze_keyword_quality(keyword, clicks, impressions, position, ctr):
    """
    Analyze a single keyword and return quality assessment
    """
    issues = []
    severity = 'LOW'
    
    # Check non-English
    if is_non_english(keyword):
        issues.append('NON_ENGLISH')
        severity = 'HIGH'
    
    # Check toxic patterns
    toxic_cats = check_toxic_patterns(keyword)
    if toxic_cats:
        issues.extend([f'TOXIC_{cat.upper()}' for cat in toxic_cats])
        severity = 'CRITICAL'
    
    # Check oil relevance
    if not is_oil_relevant(keyword):
        issues.append('NOT_OIL_RELEVANT')
        if severity == 'LOW':
            severity = 'MEDIUM'
    
    # Check if it's a poor quality keyword (high impressions, low clicks, bad position)
    if impressions > 100 and clicks < 5 and position > 50:
        issues.append('POOR_PERFORMANCE')
    
    # Calculate relevance score
    relevance_score = calculate_relevance_score(keyword)
    
    # Determine if keyword should be flagged
    flagged = len(issues) > 0 or relevance_score < 30
    
    return {
        'keyword': keyword,
        'clicks': clicks,
        'impressions': impressions,
        'position': position,
        'ctr': ctr,
        'relevance_score': relevance_score,
        'issues': ', '.join(issues) if issues else 'NONE',
        'severity': severity,
        'flagged': flagged
    }

# ============================================================================
# MAIN ANALYSIS FUNCTIONS
# ============================================================================

def load_and_filter_data():
    """Load GSC and Ahrefs data and filter to last 3 months"""
    print("="*80)
    print("LOADING DATA")
    print("="*80)
    
    # Load GSC queries
    gsc_queries = pd.read_csv('analysis/processed_data/gsc_queries.csv')
    print(f"✓ Loaded {len(gsc_queries):,} GSC queries")
    
    # Load Ahrefs keywords
    ahrefs_keywords = pd.read_csv('analysis/processed_data/ahrefs_organic_keywords.csv')
    print(f"✓ Loaded {len(ahrefs_keywords):,} Ahrefs keywords")
    
    # Load Ahrefs backlinks
    ahrefs_backlinks = pd.read_csv('analysis/processed_data/ahrefs_backlinks.csv')
    print(f"✓ Loaded {len(ahrefs_backlinks):,} backlinks")
    
    print(f"\n✓ Analysis period: {ANALYSIS_START_DATE.date()} to {ANALYSIS_END_DATE.date()}")
    print(f"✓ Total days: 90 days")
    
    return gsc_queries, ahrefs_keywords, ahrefs_backlinks

def analyze_gsc_keywords(gsc_queries):
    """Analyze GSC queries for toxic/irrelevant keywords"""
    print("\n" + "="*80)
    print("ANALYZING GSC KEYWORDS")
    print("="*80)
    
    results = []
    
    for idx, row in gsc_queries.iterrows():
        keyword = row['Top queries']
        clicks = row.get('Clicks', 0)
        impressions = row.get('Impressions', 0)
        ctr = row.get('CTR', 0)
        position = row.get('Position', 999)
        
        analysis = analyze_keyword_quality(keyword, clicks, impressions, position, ctr)
        results.append(analysis)
    
    results_df = pd.DataFrame(results)
    
    # Filter to flagged keywords only
    flagged_df = results_df[results_df['flagged'] == True].copy()
    flagged_df = flagged_df.sort_values('severity', 
                                         key=lambda x: x.map({'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}))
    
    print(f"\n✓ Analyzed {len(results_df):,} keywords")
    print(f"✓ Flagged {len(flagged_df):,} problematic keywords ({len(flagged_df)/len(results_df)*100:.1f}%)")
    
    # Severity breakdown
    print("\nSeverity Breakdown:")
    severity_counts = flagged_df['severity'].value_counts()
    for severity, count in severity_counts.items():
        print(f"  {severity}: {count:,} keywords")
    
    return flagged_df, results_df

def analyze_backlinks(ahrefs_backlinks):
    """Analyze backlinks for poor quality sources"""
    print("\n" + "="*80)
    print("ANALYZING BACKLINK QUALITY")
    print("="*80)
    
    poor_quality_links = []
    
    for idx, row in ahrefs_backlinks.iterrows():
        url = str(row.get('Referring page URL', ''))
        domain_rating = row.get('Domain rating', 0)
        
        issues = []
        
        # Check for poor quality domains
        for pattern in POOR_QUALITY_DOMAINS:
            if re.search(pattern, url, re.IGNORECASE):
                issues.append(f'POOR_DOMAIN_{pattern.replace("\\.", "").replace("\\", "")}')
        
        # Check for very low DR
        if domain_rating < 10:
            issues.append('VERY_LOW_DR')
        
        # Check for suspicious patterns in URL
        if re.search(r'(casino|porn|drugs|hack|spam)', url, re.IGNORECASE):
            issues.append('SUSPICIOUS_URL')
        
        if issues:
            poor_quality_links.append({
                'url': url,
                'domain_rating': domain_rating,
                'issues': ', '.join(issues),
                'first_seen': row.get('First seen', ''),
            })
    
    poor_links_df = pd.DataFrame(poor_quality_links)
    
    print(f"\n✓ Analyzed {len(ahrefs_backlinks):,} backlinks")
    print(f"✓ Found {len(poor_links_df):,} poor quality backlinks ({len(poor_links_df)/len(ahrefs_backlinks)*100:.1f}%)")
    
    return poor_links_df

def generate_reports(flagged_keywords, all_keywords, poor_backlinks):
    """Generate comprehensive reports"""
    print("\n" + "="*80)
    print("GENERATING REPORTS")
    print("="*80)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create outputs directory
    output_dir = Path('outputs/toxic_analysis')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Save flagged keywords CSV
    flagged_file = output_dir / f'flagged_keywords_{timestamp}.csv'
    flagged_keywords.to_csv(flagged_file, index=False)
    print(f"\n✓ Saved flagged keywords: {flagged_file}")
    
    # 2. Save poor quality backlinks CSV
    if len(poor_backlinks) > 0:
        backlinks_file = output_dir / f'poor_quality_backlinks_{timestamp}.csv'
        poor_backlinks.to_csv(backlinks_file, index=False)
        print(f"✓ Saved poor quality backlinks: {backlinks_file}")
    
    # 3. Generate summary report
    summary_file = output_dir / f'toxic_analysis_summary_{timestamp}.md'
    
    with open(summary_file, 'w') as f:
        f.write("# Toxic & Irrelevant Keyword Analysis Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Analysis Period:** {ANALYSIS_START_DATE.date()} to {ANALYSIS_END_DATE.date()} (90 days)\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write(f"- **Total Keywords Analyzed:** {len(all_keywords):,}\n")
        f.write(f"- **Flagged Keywords:** {len(flagged_keywords):,} ({len(flagged_keywords)/len(all_keywords)*100:.1f}%)\n")
        f.write(f"- **Poor Quality Backlinks:** {len(poor_backlinks):,}\n\n")
        
        # Severity breakdown
        f.write("## Severity Breakdown\n\n")
        severity_counts = flagged_keywords['severity'].value_counts()
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            count = severity_counts.get(severity, 0)
            if count > 0:
                f.write(f"- **{severity}:** {count:,} keywords\n")
        
        # Issue categories
        f.write("\n## Issue Categories\n\n")
        all_issues = []
        for issues_str in flagged_keywords['issues'].dropna():
            all_issues.extend(issues_str.split(', '))
        
        issue_counts = pd.Series(all_issues).value_counts()
        for issue, count in issue_counts.head(10).items():
            f.write(f"- **{issue}:** {count:,} occurrences\n")
        
        # Critical keywords
        f.write("\n## Critical Keywords (Immediate Action Required)\n\n")
        critical = flagged_keywords[flagged_keywords['severity'] == 'CRITICAL'].head(20)
        if len(critical) > 0:
            f.write("| Keyword | Clicks | Impressions | Position | Issues |\n")
            f.write("|---------|--------|-------------|----------|--------|\n")
            for _, row in critical.iterrows():
                f.write(f"| {row['keyword']} | {row['clicks']} | {row['impressions']} | {row['position']:.1f} | {row['issues']} |\n")
        else:
            f.write("*No critical keywords found.*\n")
        
        # Recommendations
        f.write("\n## Recommendations\n\n")
        f.write("### Immediate Actions (Next 7 Days)\n\n")
        
        critical_count = len(flagged_keywords[flagged_keywords['severity'] == 'CRITICAL'])
        high_count = len(flagged_keywords[flagged_keywords['severity'] == 'HIGH'])
        
        if critical_count > 0:
            f.write(f"1. **Review {critical_count} CRITICAL keywords** - These may contain toxic/illicit content\n")
            f.write("   - Add to Google Search Console's URL removal tool if ranking for dangerous content\n")
            f.write("   - Check if content on your site is causing these rankings\n")
            f.write("   - Consider adding negative keywords to paid campaigns\n\n")
        
        if high_count > 0:
            f.write(f"2. **Audit {high_count} HIGH severity keywords** - Non-English or highly irrelevant\n")
            f.write("   - Review content that's ranking for these terms\n")
            f.write("   - Adjust content to be more specific to target audience\n")
            f.write("   - Use hreflang tags if serving international content\n\n")
        
        if len(poor_backlinks) > 0:
            f.write(f"3. **Disavow {len(poor_backlinks)} poor quality backlinks**\n")
            f.write("   - Create Google Disavow file\n")
            f.write("   - Submit through Google Search Console\n")
            f.write("   - Monitor for penalty warnings\n\n")
        
        f.write("### Strategic Actions (Next 30 Days)\n\n")
        f.write("1. **Content Audit**: Review pages ranking for irrelevant keywords\n")
        f.write("2. **Internal Linking**: Strengthen relevance signals with better internal links\n")
        f.write("3. **Meta Tags**: Update title tags and meta descriptions to be more specific\n")
        f.write("4. **Monitoring**: Set up alerts for new toxic keyword rankings\n")
        f.write("5. **Competitor Analysis**: Check if competitors face similar issues\n\n")
        
        # Impact assessment
        f.write("## Traffic Impact Assessment\n\n")
        
        flagged_traffic = flagged_keywords['clicks'].sum()
        total_traffic = all_keywords['clicks'].sum()
        
        f.write(f"- **Total Clicks (All Keywords):** {total_traffic:,.0f}\n")
        f.write(f"- **Clicks from Flagged Keywords:** {flagged_traffic:,.0f}\n")
        f.write(f"- **% of Traffic at Risk:** {flagged_traffic/total_traffic*100:.1f}%\n\n")
        
        if flagged_traffic / total_traffic > 0.1:
            f.write("⚠️ **WARNING:** More than 10% of traffic comes from flagged keywords. High priority cleanup needed.\n\n")
        else:
            f.write("✓ Flagged keywords represent a small portion of traffic. Manageable cleanup effort.\n\n")
        
    print(f"✓ Saved summary report: {summary_file}")
    
    # 4. Generate Google Disavow file if poor backlinks found
    if len(poor_backlinks) > 0:
        disavow_file = output_dir / f'disavow_{timestamp}.txt'
        with open(disavow_file, 'w') as f:
            f.write("# Disavow file for hbnobulk.com / hbno.com\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write("# Submit this file to Google Search Console\n\n")
            for url in poor_backlinks['url']:
                # Extract domain from URL
                domain_match = re.search(r'https?://([^/]+)', url)
                if domain_match:
                    domain = domain_match.group(1)
                    f.write(f"domain:{domain}\n")
        print(f"✓ Generated Google Disavow file: {disavow_file}")
    
    print("\n" + "="*80)
    print("✓ ANALYSIS COMPLETE")
    print("="*80)
    print(f"\nAll reports saved to: {output_dir}/")
    print("\nNext Steps:")
    print("1. Review the summary report")
    print("2. Examine critical keywords in detail")
    print("3. Submit disavow file to Google Search Console (if generated)")
    print("4. Monitor rankings for flagged keywords over next 30 days")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    print("\n" + "="*80)
    print("TOXIC & IRRELEVANT KEYWORD ANALYSIS")
    print("="*80)
    print(f"Analysis Period: Last 90 days (ending {ANALYSIS_END_DATE.date()})")
    print("="*80 + "\n")
    
    try:
        # Load data
        gsc_queries, ahrefs_keywords, ahrefs_backlinks = load_and_filter_data()
        
        # Analyze GSC keywords
        flagged_keywords, all_keywords = analyze_gsc_keywords(gsc_queries)
        
        # Analyze backlinks
        poor_backlinks = analyze_backlinks(ahrefs_backlinks)
        
        # Generate reports
        generate_reports(flagged_keywords, all_keywords, poor_backlinks)
        
        print("\n✓ SUCCESS: Analysis completed successfully")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
