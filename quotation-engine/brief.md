# Technical Brief: Automated Quotation Engine

## 1. Core Objective
To architect and build a high-throughput, low-latency quotation engine to replace a legacy, manual process. The system will automate complex, multi-variable cost and price calculations, integrating directly with NetSuite.

## 2. System Architecture
- **Frontend:** Next.js with Refine.dev (for rapid UI development for CRUD operations).
- **Backend:** Node.js / TypeScript.
- **Database:** PostgreSQL (to handle relational data complexity).
- **Integration:** NetSuite (via REST/SOAP API for bidirectional data sync).

## 3. Core Logic & Feature Requirements

### Costing Engine
- **BOM Rollup:** Aggregate costs from `RawMaterial`, `PackagingMaterial`, and `LaborCategory` entities linked via a `BillOfMaterial`.
- **Landed Cost Calculation:** Factor in `freight`, `tariffs`, and `duties` for international vendors.
- **Currency Conversion:** Handle multiple vendor currencies, converting to a base currency (USD).
- **Variable Costing:** Support tiered pricing from vendors based on quantity.
- **Special Costs:** Account for fixed/variable additions (e.g., `Flush Oil`).

### Pricing & Quoting Engine
- **Dynamic Pricing:** Calculate `Estimated Sale Price` based on total cost plus configurable markup rules.
- **Tiered Pricing:** Support customer-facing price tiers based on quote quantity.
- **Taxation Module:** Implement rules for US (state-level) and international (VAT/GST) taxes.
- **Quote Lifecycle:** Manage quote status (`Draft`, `Under Review`, `Approved`, `Rejected`, `Converted`).
- **Data I/O:**
    - **Input:** Bulk import of customer SKUs for quote creation.
    - **Output:** Generate and export quotes in PDF and Excel formats.

## 4. NetSuite Integration
- **Bidirectional Sync (Scheduled):**
    - **Pull:** `Customers`, `Products`, historical `Sales Orders` (for price comparison).
    - **Push:** `Approved Quotes` to create new `Sales Orders` in NetSuite.
- **API Strategy:** Utilize NetSuite's API for all data exchange. Requires robust error handling and authentication.

## 5. Key Technical Challenges & Risks
- **Performance:** The entire calculation and rendering pipeline must complete in <30 seconds for quotes with 200+ line items. This requires optimized database queries and efficient backend logic.
- **Calculation Accuracy:** The costing and pricing logic is the core of the application. It must be rigorously tested against real-world data to ensure financial accuracy.
- **Integration Complexity:** NetSuite API can be complex. Synchronization logic must be idempotent and resilient to failure.
- **Data Integrity:** Ensuring consistency between the local database and NetSuite is critical.

## 6. Data Model Highlights
- **Central Entities:** `Quote`, `QuoteItem`, `Customer`, `Product`, `Vendor`, `BillOfMaterial`.
- **Key Relationships:**
    - `Product` has one `BillOfMaterial`.
    - `BillOfMaterial` has many `RawMaterials`.
    - `Quote` has many `QuoteItems`.
    - `Customer` and `Vendor` have `SKUMapping` tables.
