# Quotation Engine → Entities

## Customer

### **Key Info:**

- Personal Info, Contact details
- Billing/shipping addresses
- Country
    - **For International Customer, Country is required, because tax will be calculated accordingly(GST/VAT)**
    - **For US Customer, Country + State is required, because tax will be calculated according to the state (Sales  tax).**
    - **If the B2B customer is in US, the tax Exemption Certificate will be required**
- State & Zip Code
- Customer SKU mappings
- Sales history
- Assigned sales representative

---

## Vendor

### **Key Info:**

- Name, Contact details,
- Location (Country & State)
- Currency
    - **First, We may need to calculate cost in international currency, than convert to USA dollars**
    - **Calculate Import Duties, Traffis.**
    - **If the vendor is in USA, no import duties will be calculated, but Freight, “landed cost”.**
    - **Predefined freight tables, vary from state to state, shiping cost will vary vendor location and HBNO warehouse**
- Specific costs for materials supplied
- Vendor SKU mappings.
- Payment Method
    - Must Support the international Payments

---

## Raw Material

### **Key Info:**

- Internal SKU
- Vendor SKU
- Descriptive name
- Unit of measure
- **Costing tiers based on purchase quantity/size**, average cost.
    - Compute Cost on the Basis of quantity & size
    - Size-based cost variation: compute accordingly
    - Compute Cost according to Vendor, because prices may vary according to the business
- Associated supplier details, currency of cost.
- ***Cost Volatility: Mec**hanisms to update and track fluctuating raw material price*

---

## Bill of Material (BOM)

### Key Info:

- **Product Link:** Identifies the finished Product SKU this BOM belongs to.
- **Raw Material Components:** A list of Raw Material SKUs included in this BOM.
- **Component Quantity:** The exact amount of each Raw Material needed per unit of the finished Product.
    - **What about wastage material?**
    - **Will there be any alternative material?**
- **Unit of Measure for Component Quantity:** The specific UoM (e.g., "ml," "g") for each raw material quantity within the BOM, ensuring precise measurement.
- **Notes:** Any specific instructions or details for assembly.

---

## Product

### Key Info:

- Unique internal SKU.
- Descriptive name and marketing description.
- Associated Bill of Materials (BOM) for cost rollup.
- Default unit of sale (e.g., "bottle," "unit").
- Category (e.g., "Essential Oil," "Carrier Oil," "Blend," "Private Label").
    - Product variants (”10ml”, “30ml”()
- Default pricing rules (e.g., base markup percentage).
    - Price distinguish if a product is being sold on “Retail” or in “Bulk”
    - Profatibility Tracking on “retail sold” and “Bulk sold”
- Status (e.g., "Active," "Discontinued").
- Links to associated Packaging Materials.

---

## Packaging Material

### Key Info

- Unique internal SKU.
- Descriptive name (e.g., "10ml Amber Dropper Bottle," "Custom Matte Label").
- Type (e.g., "Standard," "Private Label," "Retail Box," "Bulk Drum").
- Unit of measure for label (e.g., "each Label" "roll," "sheet").
- Costing tiers based on purchase quantity/size.
    - Cost vary by sizes (10ml bottle vs 100ml bottle)
    - Private Label specifics → unique cost
- Component Assembly and cost of each part
- Associated vendors and their specific product codes.
- Currency of cost.
- Physical attributes (e.g., volume capacity for bottles, dimensions for labels).

---

## Labor Category

### Key Info

- Unique identifier for the category (e.g., "Filling Line Labor," "Labeling & Packaging Labor").
- Descriptive name.
- Average cost per unit of time (e.g., per hour) or per unit of output (e.g., per bottle filled) for tasks within this category.
    - **Is labor cost calculated on that basis of time or Unit-based?**
- Associated production steps or activities.
- Last updated timestamp for cost.

---

## Quote

### Key Info

- **Unique Quote ID:** System-generated identifier.
- **Customer Link:** Reference to the `Customer` entity.
- **Sales Representative:** User who created the quote.
- **Creation Date & Expiration Date:** When the quote was made and when it becomes invalid.
- **Quote Items:** A list of `Quote Item` entities detailing each product being quoted (including its specific configuration and pricing breakdown).
- **Calculated Costs:**
    - Total Raw Material Cost.
    - Total Packaging Cost.
    - Total Labor Cost.
    - Total Flush Oil Cost.
    - Total Additional Costs (if any, beyond Flush Oil).
    - **Total Manufacturing Cost (sum of above).**
- **Dynamic Pricing Recalculation:** Any change in quantity, configuration.
- **Estimated Sale Price:** The proposed price to the customer.
- **Last Sale Price Comparison:** The price of the last similar sale to this customer (pulled from NetSuite/Sales Order entity).
- **Profitability Metrics:** Calculated margin and markup.
- **Taxation Details:** Calculated tax amount based on customer location and product taxability.
- **Shipping Method & Cost:** Selected shipping option and estimated cost according to location.
- **Status:** (e.g., "Draft," "Sent," "Under Review," "Approved," "Rejected," "Converted to Order").
- **Notes:** Internal or customer-facing notes.
- **Version/Revision:** To track changes made to the quote during negotiation.
- **Multi-Currency Display:** For international customers, display the quote in their currency while tracking costs in HBNO's base currency.
- **PDF/Excel Export:** Generate professional, branded quote documents.
- **User Permissions (RBAC):** Different users (Sales vs. Finance) will have different views and capabilities (e.g., Sales can create, Finance can approve/override).

---

FOB + Costs + Standard Labor + Build + Margin % by default  - discount rate

---

**REQUEST FROM DAVID**