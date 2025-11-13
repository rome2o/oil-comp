# Technical Health Foundation

**Pillar 1: Site Performance, Mobile Experience & Technical SEO**  
**HBNO Essential Natural Oils**

[← Back to Our Approach](./01_our-approach.md) | [← Proposal Home](../README.md) | [Next: Search Visibility →](./03_search-visibility.md)

---

## Why Technical Health Comes First

You can't build sustainable growth on a shaky foundation. Technical health issues create cascading problems:

- **Slow page loads** → Higher bounce rates → Lower conversions
- **Mobile UX problems** → 60%+ of traffic frustrated → Revenue ceiling
- **Technical SEO errors** → Poor crawlability → Reduced organic visibility
- **Checkout friction** → Cart abandonment → Lost sales

**Core Principle:** Technical health isn't a one-time fix. It's an ongoing commitment to maintaining performance standards as your store evolves.

---

## Current State Assessment

Based on your site analysis, several technical health issues require systematic attention:

### Documented Issues

**Site Speed & Performance:**

- Recent theme changes have impacted load times
- Core Web Vitals may not meet Google's "good" thresholds
- Mobile performance typically lags desktop (common Shopify pattern)

**Mobile Experience:**

- Responsive design present, but optimization opportunity exists
- Touch target sizing and mobile navigation may need refinement
- Mobile checkout flow requires friction analysis

**Technical SEO:**

- Crawlability baseline acceptable, but optimization opportunities identified
- Structured data implementation may be incomplete
- Redirect chains and orphan pages possible (standard site hygiene)

**Search Console Indicators:**

- CTR decline noted (5.47% → 1.20%) suggests meta optimization needed
- Position improvements not translating to proportional CTR gains
- Mobile usability issues may exist

### What This Means

These aren't catastrophic failures—they're **optimization opportunities**. Your site functions, but it's not performing at the level required for competitive B2B e-commerce.

**Recovery Timeline:** 3-6 months to achieve "good" health scores across all metrics.

---

## Our Technical Health Strategy

We organize technical health work into five interconnected focus areas:

---

### 1. Core Web Vitals Optimization

**What These Are:**  
Google's standardized metrics for user experience quality:

- **LCP (Largest Contentful Paint):** Page loading performance (target: <2.5s)
- **FID (First Input Delay):** Interactivity responsiveness (target: <100ms)
- **CLS (Cumulative Layout Shift):** Visual stability (target: <0.1)

**Why They Matter:**

- Google uses these as ranking signals (affects SEO)
- Directly correlate with conversion rates (affects revenue)
- Mobile performance especially critical (60%+ of traffic)

**Our Approach:**

**Month 1-2: Baseline & Quick Wins**

- Audit current Core Web Vitals scores (desktop + mobile)
- Identify specific elements causing poor LCP/FID/CLS
- Implement quick fixes:
  - Image optimization (compression, lazy loading, sizing)
  - Font loading optimization (FOUT prevention)
  - Third-party script audit (remove/defer non-essential)
  - CSS/JS minification and consolidation

**Month 3-4: Structural Improvements**

- Theme code optimization (remove unused CSS/JS)
- Critical CSS inlining for above-fold content
- Server response time optimization
- CDN configuration review
- Shopify app audit (remove performance-draining apps)

**Month 5-6: Ongoing Monitoring**

- Weekly Core Web Vitals monitoring
- Performance regression testing after changes
- Seasonal traffic spike preparation
- Continuous improvement iterations

**Expected Outcomes:**

- All Core Web Vitals in "good" range by Month 4
- Mobile performance score 80+ by Month 3
- Page load times consistently under 3 seconds

---

### 2. Mobile Optimization

**Current Reality:**  
Mobile traffic likely represents 50-70% of your visitors. If mobile experience is subpar, you're alienating your majority audience.

**Our Focus Areas:**

**Mobile Speed:**

- Lighter images for mobile viewports
- Touch-optimized interactions (no hover dependencies)
- Reduced data transfer for cellular connections
- Faster initial render for mobile CPUs

**Mobile UX:**

- Touch target sizing (minimum 48x48px per guidelines)
- Thumb-friendly navigation zones
- Simplified mobile checkout (fewer form fields)
- Mobile-first product gallery experience

**Mobile Checkout:**

- One-column layout (no side-by-side fields)
- Autofill compatibility verification
- Error message visibility without scrolling
- Mobile payment options (Apple Pay, Google Pay)

**Testing Methodology:**

- Real device testing (not just emulators)
- Network throttling tests (3G/4G conditions)
- Different OS/browser combinations (iOS Safari, Android Chrome)
- Accessibility testing (screen reader compatibility)

**Deliverables:**

- Mobile UX audit report (Month 1)
- Prioritized mobile improvement roadmap (Month 1)
- Monthly mobile performance dashboards
- Quarterly mobile experience reviews

---

### 3. Technical SEO Foundation

Technical SEO ensures search engines can effectively crawl, understand, and index your site.

**Crawlability & Indexation:**

**What We Check:**

- XML sitemap accuracy and submission
- Robots.txt configuration (no accidental blocks)
- Orphan page identification (pages with no internal links)
- Redirect chains and loops (cause crawl budget waste)
- 404 errors and broken internal links
- Canonical tag implementation (prevent duplicate content issues)

**What We Fix:**

- Submit updated XML sitemaps to Google/Bing
- Create internal linking strategy for orphan pages
- Consolidate redirect chains into direct redirects
- Fix broken links via 301 redirects to relevant pages
- Implement proper canonical tags site-wide

**Structured Data (Schema Markup):**

**What We Implement:**

- Product schema (price, availability, reviews)
- Organization schema (business info, logo)
- Breadcrumb schema (navigation context)
- Review/rating schema (rich snippets)
- FAQ schema (search visibility)

**Why This Matters:**

- Rich snippets improve CTR in search results
- Google Shopping compatibility
- Voice search optimization
- Enhanced search result presentation

**URL & Site Architecture:**

**What We Optimize:**

- URL structure clarity (descriptive, keyword-relevant)
- Category hierarchy logic (supports user + crawler navigation)
- Breadcrumb implementation (UX + SEO benefit)
- Pagination strategy (view-all vs. paginated category pages)
- Faceted navigation SEO handling (prevent crawl traps)

**Search Console Monitoring:**

- Weekly search console review
- Coverage error identification and remediation
- Manual action monitoring (penalty detection)
- Enhancement report tracking (structured data validation)

---

### 4. Site Speed & Performance Engineering

**Shopify-Specific Optimizations:**

**Theme Optimization:**

- Liquid code efficiency (reduce loop complexity)
- Unused section/snippet removal
- App embed code consolidation
- Theme update implementation (security + performance)

**Image Optimization:**

- Shopify CDN leverage (automatic sizing)
- Modern format delivery (WebP with fallbacks)
- Lazy loading implementation (below-fold images)
- Product image dimension standardization

**Script Management:**

- Third-party script audit (tracking, marketing tools)
- Async/defer attribute optimization
- Script consolidation where possible
- Remove redundant tracking pixels

**Caching Strategy:**

- Browser caching headers optimization
- Shopify CDN utilization
- Dynamic content vs. static content separation
- Customer-specific content caching strategy

**Database & Backend:**

- Collection query optimization
- Metafield usage efficiency
- Bulk operation implementation (reduce API calls)
- Shopify API rate limit management

**Monitoring & Alerts:**

- Uptime monitoring (99.9% target)
- Performance regression alerts (sudden slowdowns)
- Traffic spike capacity planning
- Incident response protocol

---

### 5. Security & Trust Signals

Technical health includes ensuring customers feel safe completing purchases.

**Security Fundamentals:**

- SSL certificate validation (HTTPS everywhere)
- PCI compliance verification (Shopify handles, but verify)
- Regular security audit (app permissions, admin access)
- Two-factor authentication enforcement (admin accounts)

**Trust Signal Implementation:**

- Security badges on checkout (Norton, McAfee, etc.)
- Trust certifications displayed (if applicable)
- SSL padlock visibility emphasis
- Privacy policy and terms accessibility
- Contact information prominence

**Checkout Reliability:**

- Payment gateway uptime monitoring
- Order submission error tracking
- Email confirmation delivery verification
- Thank-you page load reliability

---

## Service Tier Implementation

### Starter Tier (20 hours/month)

**Focus:** Critical issues only

- Core Web Vitals baseline audit
- Mobile speed quick wins
- Technical SEO foundation (sitemap, robots.txt, basic schema)
- Monthly performance monitoring

**Timeline:** 6-12 months to "good" health

---

### Growth Tier (40 hours/month) ⭐ RECOMMENDED

**Focus:** Systematic improvement

- Full Core Web Vitals optimization
- Comprehensive mobile UX improvements
- Complete technical SEO implementation
- Structured data deployment
- Weekly performance monitoring
- Proactive issue identification

**Timeline:** 3-6 months to "good" health

---

### Plus Tier (60 hours/month)

**Focus:** Advanced optimization + ongoing excellence

- All Growth tier services
- Advanced performance engineering
- Dedicated technical audits (quarterly)
- Real-time monitoring and alerts
- Competitive technical benchmarking
- Pre-emptive optimization for new features

**Timeline:** 2-4 months to "good" health + sustained excellence

---

## Success Metrics

### Primary Technical Metrics

**Core Web Vitals:**

- LCP < 2.5 seconds (desktop + mobile)
- FID < 100 milliseconds
- CLS < 0.1
- All metrics in "good" range (75th percentile)

**Page Speed:**

- Desktop load time < 2 seconds
- Mobile load time < 3 seconds
- Time to Interactive < 3.5 seconds

**Mobile Performance:**

- Google PageSpeed Insights mobile score 80+
- Lighthouse mobile performance 90+

**Technical SEO:**

- Zero critical errors in Search Console
- 100% of important pages indexed
- Zero redirect chains
- All product pages have structured data

**Reliability:**

- 99.9% uptime
- Zero checkout failures
- Zero critical security issues

### Business Impact Metrics

**How Technical Health Affects Revenue:**

- **Lower bounce rates:** Faster pages = more engaged visitors
- **Higher conversion rates:** Smooth checkout = more completions
- **Better SEO rankings:** Technical health = ranking signal
- **Improved mobile revenue:** Mobile optimization = mobile conversions
- **Reduced cart abandonment:** Performance + trust = completions

**Expected Impact (Growth Tier, 6 months):**

- 10-15% improvement in organic rankings (technical factors)
- 5-10% reduction in bounce rate
- 15-20% improvement in mobile conversion rate
- 2-5% overall conversion rate improvement

---

## Common Questions

**Q: Why does this take 3-6 months?**  
A: Technical improvements require testing, validation, and Google re-crawling. SEO ranking benefits compound over time. Rush jobs break things.

**Q: Can't I just use a speed optimization app?**  
A: Apps help, but create new performance overhead. Manual optimization is more effective but requires expertise.

**Q: What if my theme is the problem?**  
A: Theme optimization is included. Theme replacement is a separate project (we can scope if needed).

**Q: How do I know you're not breaking things?**  
A: Every change is tested in dev/staging first. We monitor error rates and have rollback protocols.

**Q: What happens after health is "good"?**  
A: Ongoing monitoring and maintenance. Sites degrade over time (new apps, content, features). Health requires continuous attention.

---

## Next Steps

Technical health is the foundation. Once established, the other three pillars can deliver maximum impact:

- **[Search Visibility & Quality Traffic →](./03_search-visibility.md)** - Organic search strategy
- **[Conversion & Revenue Optimization →](./04_conversion-optimization.md)** - Revenue per visitor
- **[Analytics & Continuous Improvement →](./05_analytics-improvement.md)** - Measurement framework

---

**Ready to see how this fits into your service tier?**  
[← View Service Options](../service-models/01_service-overview.md)

---

[← Back to Our Approach](./01_our-approach.md) | [← Proposal Home](../README.md)
