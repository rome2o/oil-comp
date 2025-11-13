# GitHub Copilot XML-Based Instructions for SEO Analysis Project

This document provides detailed XML-based instructions for GitHub Copilot to effectively assist with SEO data analysis and reporting for the oil company website project.

## Project Context XML Structure

```xml
<project_context>
    <name>Oil Company SEO Analysis</name>
    <description>
        Comprehensive SEO performance analysis focusing on the impact of theme change 
        on July 19th, 2025, and evaluation of Allen's SEO efforts since February 12th, 2025.
    </description>
    <domain>hbnobulk.com / hbno.com</domain>
    <analysis_period>
        <start_date>2024-02-01</start_date>
        <theme_change_date>2025-07-19</theme_change_date>
        <allen_start_date>2025-02-12</allen_start_date>
        <end_date>2025-10-22</end_date>
    </analysis_period>
</project_context>
```

## Data Sources XML Configuration

```xml
<data_sources>
    <google_analytics>
        <location>./google_analytics/</location>
        <files>
            <file type="xlsx">Pages and screens_ Page path and screen class.xlsx</file>
            <file type="xlsx">Traffic acquisition_ Session primary channel group (Default Channel Group).xlsx</file>
        </files>
        <metrics>
            <metric>Users</metric>
            <metric>Sessions</metric>
            <metric>Engaged sessions</metric>
            <metric>Engagement rate</metric>
            <metric>Conversions</metric>
        </metrics>
        <date_range>2024-02-01 to 2025-10-22</date_range>
    </google_analytics>
    
    <google_search_console>
        <location>./google_search_console/</location>
        <files>
            <file type="xlsx">https___hbno.com_-Performance-on-Search-2025-10-22.xlsx</file>
            <file type="xlsx">https___hbno.com_-core-web-vitals-2025-10-22.xlsx</file>
            <file type="xlsx">https___hbno.com_-core-web-vitals-2025-10-22 (1).xlsx</file>
        </files>
        <metrics>
            <metric>Total Clicks</metric>
            <metric>Total Impressions</metric>
            <metric>Average CTR</metric>
            <metric>Average Position</metric>
        </metrics>
        <date_range>2024-06-21 to 2025-10-22</date_range>
    </google_search_console>
    
    <ahrefs>
        <location>./ahrefs/</location>
        <files>
            <file type="csv">hbnobulk.com-organic-keywords-subdomains-al_2025-10-22_19-38-50.csv</file>
            <file type="csv">hbnobulk.com-backlinks-subdomains_2025-10-22_19-38-16.csv</file>
            <file type="pdf">Overview - Hbnobulk-22-mar-2025.pdf</file>
            <file type="pdf">Overview - Hbno-9-feb-2025.pdf</file>
            <file type="pdf">Overview - Hbno-29-jun-2025.pdf</file>
            <file type="pdf">Overview - Hbno-current-2025.pdf</file>
            <file type="pdf">Overview - Hbnobulk-28-jun-2025.pdf</file>
            <file type="pdf">Overview - Hbnobulk-current-2025.pdf</file>
        </files>
        <metrics>
            <metric>Keyword rankings</metric>
            <metric>Estimated organic traffic</metric>
            <metric>Visibility score</metric>
            <metric>Backlink count</metric>
            <metric>Referring domains</metric>
        </metrics>
    </ahrefs>
</data_sources>
```

## Analysis Framework XML

```xml
<analysis_framework>
    <objectives>
        <objective id="1">
            <title>Theme Change Impact Assessment</title>
            <description>Analyze SEO performance changes after July 19th, 2025 theme implementation</description>
            <key_periods>
                <period name="pre_theme">2025-06-01 to 2025-07-18</period>
                <period name="post_theme">2025-07-20 to 2025-10-22</period>
            </key_periods>
            <focus_metrics>
                <metric>organic_traffic</metric>
                <metric>keyword_rankings</metric>
                <metric>core_web_vitals</metric>
                <metric>click_through_rate</metric>
            </focus_metrics>
        </objective>
        
        <objective id="2">
            <title>Allen's SEO Performance Evaluation</title>
            <description>Compare SEO performance under Allen's management vs previous agency</description>
            <key_periods>
                <period name="previous_agency">2024-02-01 to 2025-02-11</period>
                <period name="allen_management">2025-02-12 to 2025-10-22</period>
            </key_periods>
            <focus_metrics>
                <metric>organic_keyword_growth</metric>
                <metric>backlink_acquisition</metric>
                <metric>traffic_quality</metric>
                <metric>conversion_improvement</metric>
            </focus_metrics>
        </objective>
    </objectives>
</analysis_framework>
```

## Code Generation Guidelines XML

```xml
<code_guidelines>
    <python_preferences>
        <libraries>
            <library name="pandas" usage="primary data manipulation" />
            <library name="numpy" usage="numerical computations" />
            <library name="matplotlib" usage="basic plotting" />
            <library name="seaborn" usage="statistical visualizations" />
            <library name="plotly" usage="interactive charts" />
            <library name="openpyxl" usage="Excel file handling" />
            <library name="datetime" usage="date operations" />
        </libraries>
        
        <coding_standards>
            <standard>Use descriptive variable names (e.g., organic_traffic_df, not df1)</standard>
            <standard>Include comprehensive docstrings for all functions</standard>
            <standard>Add inline comments for complex data transformations</standard>
            <standard>Use type hints where applicable</standard>
            <standard>Follow PEP 8 style guidelines</standard>
        </coding_standards>
        
        <data_handling>
            <practice>Always check data quality and handle missing values</practice>
            <practice>Normalize date formats across all data sources</practice>
            <practice>Create backup copies before major transformations</practice>
            <practice>Use consistent column naming conventions</practice>
        </data_handling>
    </python_preferences>
    
    <visualization_guidelines>
        <chart_types>
            <chart type="line_plot" use_case="time series trends" />
            <chart type="bar_chart" use_case="period comparisons" />
            <chart type="heatmap" use_case="correlation analysis" />
            <chart type="scatter_plot" use_case="relationship analysis" />
            <chart type="box_plot" use_case="distribution analysis" />
        </chart_types>
        
        <styling>
            <color_scheme>professional blues and oranges for contrast</color_scheme>
            <font_size>minimum 12pt for readability</font_size>
            <titles>clear, descriptive titles with date ranges</titles>
            <legends>position to avoid obscuring data</legends>
        </styling>
    </visualization_guidelines>
</code_guidelines>
```

## Task-Specific Instructions XML

```xml
<task_instructions>
    <data_preparation>
        <steps>
            <step order="1">Load and inspect all data files for structure and quality</step>
            <step order="2">Standardize date formats across all datasets</step>
            <step order="3">Create unified column naming conventions</step>
            <step order="4">Handle missing values and outliers appropriately</step>
            <step order="5">Create summary statistics for data validation</step>
        </steps>
        
        <output_requirements>
            <requirement>Generate data quality report</requirement>
            <requirement>Create standardized datasets for analysis</requirement>
            <requirement>Document any data transformations applied</requirement>
        </output_requirements>
    </data_preparation>
    
    <trend_analysis>
        <focus_areas>
            <area name="organic_traffic">
                <metrics>sessions, users, page_views</metrics>
                <comparison_periods>pre_allen, allen_era, pre_theme, post_theme</comparison_periods>
            </area>
            
            <area name="keyword_performance">
                <metrics>rankings, impressions, clicks, ctr</metrics>
                <segmentation>brand_keywords, non_brand_keywords, top_10_keywords</segmentation>
            </area>
            
            <area name="technical_seo">
                <metrics>core_web_vitals, mobile_usability, crawl_errors</metrics>
                <focus>theme_change_impact</focus>
            </area>
        </focus_areas>
    </trend_analysis>
    
    <reporting>
        <executive_summary>
            <include>key_findings, performance_metrics, recommendations</include>
            <format>bullet_points with supporting data</format>
            <length>maximum 500 words</length>
        </executive_summary>
        
        <detailed_analysis>
            <sections>
                <section name="methodology">description of analysis approach</section>
                <section name="data_overview">summary of data sources and quality</section>
                <section name="theme_impact">before/after analysis with statistical significance</section>
                <section name="allen_performance">comparative performance analysis</section>
                <section name="recommendations">actionable insights and next steps</section>
            </sections>
        </detailed_analysis>
        
        <visualizations>
            <chart type="dashboard" content="key_metrics_overview" />
            <chart type="timeline" content="major_events_and_trends" />
            <chart type="comparison" content="period_performance_analysis" />
        </visualizations>
    </reporting>
</task_instructions>
```

## Error Handling and Validation XML

```xml
<error_handling>
    <data_validation>
        <check type="file_existence">Verify all referenced files exist before processing</check>
        <check type="data_completeness">Identify missing data ranges and document gaps</check>
        <check type="format_consistency">Ensure date formats and metrics are consistent</check>
        <check type="outlier_detection">Flag unusual values that may indicate data errors</check>
    </data_validation>
    
    <exception_handling>
        <strategy>Graceful degradation with informative error messages</strategy>
        <logging>Comprehensive logging of data processing steps</logging>
        <recovery>Provide alternative approaches when primary methods fail</recovery>
    </exception_handling>
    
    <quality_assurance>
        <validation>Cross-reference metrics across different data sources</validation>
        <sanity_checks>Verify that calculated metrics align with expected ranges</sanity_checks>
        <documentation>Document assumptions and limitations in analysis</documentation>
    </quality_assurance>
</error_handling>
```

## Communication Guidelines XML

```xml
<communication_guidelines>
    <code_comments>
        <style>Clear, concise explanations of complex operations</style>
        <frequency>Comment every major data transformation or calculation</frequency>
        <context>Explain business relevance of technical operations</context>
    </code_comments>
    
    <progress_reporting>
        <checkpoints>Report completion of major analysis phases</checkpoints>
        <issues>Immediately flag data quality or analysis concerns</issues>
        <insights>Highlight interesting findings as they emerge</insights>
    </progress_reporting>
    
    <recommendations>
        <format>Specific, actionable recommendations with supporting data</format>
        <priority>Rank recommendations by potential impact and implementation difficulty</priority>
        <metrics>Tie recommendations to measurable business outcomes</metrics>
    </recommendations>
</communication_guidelines>
```

## Usage Instructions

### For Initial Data Analysis
```xml
<usage_example type="data_loading">
    <instruction>
        When I ask you to analyze SEO data, start by referencing this XML structure 
        to understand the project context, data sources, and analysis objectives.
    </instruction>
    <expected_response>
        Load data according to the data_sources XML configuration, apply the 
        data_preparation steps, and provide initial data quality assessment.
    </expected_response>
</usage_example>
```

### For Specific Analysis Tasks
```xml
<usage_example type="trend_analysis">
    <instruction>
        When analyzing trends, focus on the key_periods and focus_metrics 
        defined in the analysis_framework XML section.
    </instruction>
    <expected_response>
        Generate visualizations and statistical analysis that directly address 
        the defined objectives with appropriate time period comparisons.
    </expected_response>
</usage_example>
```

### For Report Generation
```xml
<usage_example type="reporting">
    <instruction>
        When creating reports, follow the reporting XML structure for format, 
        content, and visualization requirements.
    </instruction>
    <expected_response>
        Produce comprehensive reports with executive summary, detailed analysis, 
        and actionable recommendations as specified in the XML framework.
    </expected_response>
</usage_example>
```

## Best Practices Summary

1. **Always reference this XML structure** when beginning any SEO analysis task
2. **Validate data quality** before proceeding with analysis
3. **Focus on business objectives** rather than just technical metrics
4. **Provide context** for all findings and recommendations
5. **Use consistent methodology** across all analysis phases
6. **Document assumptions** and limitations clearly
7. **Create reproducible code** with clear comments and structure

This XML-based instruction set ensures that GitHub Copilot provides consistent, high-quality assistance that aligns with the specific requirements and context of this SEO analysis project.