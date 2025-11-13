# Oil Company - Quotation Engine

[Quotation Engine → Entities](Oil%20Company%20-%20Quotation%20Engine%2023a28eac4f2f8080bc95f6b7524d2ab3/Quotation%20Engine%20%E2%86%92%20Entities%2023e28eac4f2f805e93f6d20b71664d44.md)
 
## Finance Related Manual Steps

### HBNO SKU

1. To calculate the price a product:
    1. First, sum up all components cost (e.g Raw Material, Packaging cost, Labour cost, Labeling cost)
2. Then we will find estimated sale price
3. Compare the last sale price (pulled out from invoice of customer) with estimated price

**We have different sheets for each components/materials:**

1. Raw Material BOM
    1. Calculate average price of all raw material
    2. BOM multiplied by billend price
2. Packing material
    1. the cost of packing material varies according to the size
3. PL packing separate sheet
4. Labor cost for customer
    1. labour cost is calculated on the basis of category
    2. find average labour cost
5. and Return to BOM sheet
    1. After adding up all prices (Raw material, packing, labeling, labor)
    2. Now add additional cost which known as as → Flush Oil

**Now, the complex problem here is calculating the cost Raw material, because there are some different cost that varies according to the sizes.**

---

There could be 200 items on the same time.

The pricing specification might have to be visible upon hovers

Might need to bulk import

Get the excel sheet of bulk items

Might be retail customers - need more info

Most of the data shared is related to private label

Bulk department and retail customers might be different.

Retailer customers give SKU

Deep dive into request quotation from the customer side and sales side.

---

**Entities**

User

Customer

Vendor

Invoice

Quote

- Sales requests a quote
- Finance can see an automated quote pulled up against a request and approve it

Labor cost

Products 

BOMs

Sales

Brand/Business/Warehouse (e.g. BULK, RETAIL)

Packaging material

Vendor will be required

Each vendor might have different cost.

Purchase orders might be required

Different views for sales and finance. 

Has RBAC

Refine.dev

Might need option 

Vendors are 50% inside US and 50% outside US.

Profitability on the product is fluctuating

Average price is considered to cover up the fluctuation.

Figure out how Netsuite is doing the average pricing.

Put an automation to put quote under review on the basis of specific conditions

---

What is the accounting system in use? Xero? MYOB? Is it all done within NetSuite? - completely netsuite, push quotations to netsuite, 

Payment methods - authorize.net,  — if this global?

Taxation - Taxation depends on the state if in US. 

- Get the taxation details for overseas customers

On the basis of what category?  

How often the prices are updated and where do you receive them?

How often price is fluctuated?

If one raw material price is increasing, does it drastically increase price of overall product?

Price of flush oil, on what basis? is fixed or variable?

Take us through a part of quote, internal quote.

How many kinds of costs there are altogether?

Explain tiered pricing?

- depending upon the size of the batch, running the fixed would be higher if the batch is small.
- quantity of the bulk order is tiered.

Types of packaging? Standard packaging or private label packaging?

Lets name the variables and formulas

will need connection to netsuite to pull sales orders to see previous pricing

We need a standard format to request for the quote from customers.

Customer’s SKU might be needing to be mapped → might need to be in the system

Vendor’s SKU might be needing to be mapped. → might need to be in the system

SKU mapping file

---

Finale was the previous system.

price for 70 items - could took around 3-4 hours.

Bom to Cassie

Avg price to Joseph

Fixed cost, labor cost, fixed cost.

Avg time of the team for quotation per week.

---

**Sales flow:**

Login to system

Go to quotation window

Select warehouse/business

Select customer

Item SKUs - should be able to import

Get the price of that

Send to customer PDF / Excel.

Be able to push to netsuite

**Quick quote flow:**

Create quick quote

Uploading list of items

Select customer

Send the quote

Maybe standardize the customer file?

**Review flow:**

Login to the system

Click Quotes an list see all the quotes

Be able to filter the quotes

Be able to approve the quote

Joseph needs to see the listing

---

get the quotes within 30 secs.

product cards and product details

need to collect sample quotes of 20-30 — dependency on data on netsuite, write tests on the basis of this.

will need scheduled sync on netsuite products, customers or so.

---

[Procurement](Oil%20Company%20-%20Quotation%20Engine%2023a28eac4f2f8080bc95f6b7524d2ab3/Procurement%2024228eac4f2f80479562c7a20364beb0.md)