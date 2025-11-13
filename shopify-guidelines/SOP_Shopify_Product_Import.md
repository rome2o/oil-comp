# SOP: Shopify Product Import Guidelines

This document provides a standard operating procedure for importing products into Shopify using a CSV file. Following these guidelines will ensure consistency, prevent common errors, and optimize products for performance and SEO.

## Table of Contents
1.  [Pre-Import Checklist](#pre-import-checklist)
2.  [Product Metadata Completion Checklist](#product-metadata-completion-checklist)
3.  [The Product CSV File](#the-product-csv-file)
    - [Using a Template](#using-a-template)
    - [Key CSV Columns Explained](#key-csv-columns-explained)
4.  [Handling Product Variants](#handling-product-variants)
5.  [Image Preparation and SEO](#image-preparation-and-seo)
6.  [The Import Process](#the-import-process)
7.  [Post-Import Verification](#post-import-verification)
8.  [Common Errors and Solutions](#common-errors-and-solutions)
9.  [Advanced Tips](#advanced-tips)

---

### Pre-Import Checklist
- [ ] **Backup Existing Products:** Before any major import, export your current product list as a backup. Go to `Products` > `Export` and save the CSV.
- [ ] **Finalize Product Data:** Ensure all product information is complete and accurate in your source spreadsheet.
- [ ] **Prepare All Images:** All product images should be resized, renamed, and ready for upload.
- [ ] **Review CSV for Formatting:** Double-check that your CSV file is correctly formatted and saved as a UTF-8 encoded CSV.

---

### Product Metadata Completion Checklist

This checklist is designed to guide the team in filling out the crucial metadata for our Shopify products. Completing these fields is essential for SEO, site usability, and customer experience.

#### High Priority - Must Be Completed

- [ ] **Image Alt Text:**
    - **Action:** Fill this out for every single product and variant image.
    - **Guideline:** Write a descriptive sentence explaining what the image shows. Good Example: "A clear glass bottle of HBNO's You Glow Girl Facial Serum with a white dropper cap." Bad Example: "product image".

- [ ] **Variant SKU:**
    - **Action:** Verify that every single variant has a unique SKU.
    - **Guideline:** No two rows in the final CSV should have the same SKU. This is critical for inventory.

- [ ] **Tags:**
    - **Action:** Review and standardize tags for all products.
    - **Guideline:** Use tags to create logical groups for collections. For example, all essential oils must have the `essential-oil` tag. All organic products must have the `organic` tag.

#### Medium Priority - Highly Recommended

- [ ] **SEO Title & Description Review:**
    - **Action:** Review the existing SEO titles and descriptions.
    - **Guideline:**
        - **SEO Title:** Keep it under 60 characters. Make it compelling and keyword-rich.
        - **SEO Description:** Keep it under 160 characters. It should be an engaging summary.

- [ ] **Custom Metafields Consistency:**
    - **Action:** Audit the custom metafields for completeness across all relevant products.
    - **Guideline:** Ensure that for every essential oil, fields like `BOTANICAL NAME`, `COUNTRY OF ORIGIN`, `EXTRACTION METHOD`, and `Oil Part of Plant` are populated.

- [ ] **Shopify Product Category:**
    - **Action:** Review the assigned `Product Category` for accuracy.
    - **Guideline:** Choose the most specific category possible from Shopify's official taxonomy. This helps with tax calculation and sales channel integrations.

#### Low Priority - Optional but Recommended

- [ ] **Google Shopping Fields:**
    - **Action:** If planning to use Google Shopping, populate these fields.
    - **Guideline:** Focus on `Google Shopping / Google Product Category` and `Google Shopping / MPN` if applicable.

- [ ] **Variant Barcode:**
    - **Action:** If you use a barcode system for inventory, fill in this column.
    - **Guideline:** Otherwise, this can be left blank.

---

### The Product CSV File

#### Using a Template
The safest way to create your import file is to use Shopify's own structure.
1.  Go to **Products**.
2.  Click **Export**.
3.  Select "All products" (or a single product to see the structure) and choose "Plain CSV file".
4.  Use this exported file as your template.

#### Key CSV Columns Explained

-   **Handle:** The unique, URL-friendly identifier for a product (e.g., `premium-olive-oil`).
    -   **Rule:** Every product must have a unique handle. It should not contain spaces or special characters. Use hyphens to separate words.
    -   **For Variants:** All variants of the same product share the **same handle**.
-   **Title:** The main product name displayed to customers.
-   **Body (HTML):** The product description. You can use HTML tags for formatting (e.g., `<p>`, `<strong>`, `<ul>`).
-   **Vendor:** The manufacturer or brand of the product.
-   **Product Type:** The category of the product (e.g., `Cooking Oil`, `Skincare`). Used for filtering in the Shopify admin.
-   **Tags:** Keywords used for filtering and organizing products on your storefront (e.g., `organic`, `extra-virgin`, `sale`). Separate tags with a comma. Also ensure any tagging that will help categorising. E.g. for all essential oil products you should tag it with `essential-oil`. Our goal is to have smart collections at the end of the day so these tags are going to be helpful.
-   **SKU (Stock Keeping Unit):** A unique code to identify the product or variant for inventory tracking.
    -   **Rule:** Each variant must have a unique SKU. This should exist in NetSuite. 
-   **Variant Price:** The price of the specific product variant. Do not include currency symbols.
-   **Compare at Price:** An optional higher price to show a "sale" or discount.
-   **inventory_policy:** Set to `deny` to prevent sales when out of stock, or `continue` to allow overselling.
-   **inventory_quantity:** The number of items in stock. Leave blank if you are not tracking inventory.
-   **SEO Title & SEO Description:** Crucial for search engine optimization. If left blank, Shopify will use the product Title and Body, which may not be optimal.

---

### Handling Product Variants

This is a critical section. If a product has options like size or color, you must structure the CSV correctly.

-   **First Row:** The first row for a product defines the main product and the first variant. It includes the `Handle`, `Title`, and other core details.
-   **Subsequent Rows (for other variants):**
    -   These rows must have the **same Handle** as the first row.
    -   Leave the `Title`, `Body (HTML)`, `Vendor`, and `Tags` columns **blank**.
    -   Fill in the `Option1 Value`, `Option2 Value`, etc., for each variant.
    -   Each variant row needs its own `Variant SKU`, `Variant Price`, and `inventory_quantity`.

**Example for a T-Shirt:**

| Handle          | Title         | Option1 Name | Option1 Value | Option2 Name | Option2 Value | Variant SKU |
|-----------------|---------------|--------------|---------------|--------------|---------------|-------------|
| cool-t-shirt    | Cool T-Shirt  | Size         | Small         | Color        | Red           | COOL-T-S-R  |
| cool-t-shirt    |               | Size         | Medium        | Color        | Red           | COOL-T-M-R  |
| cool-t-shirt    |               | Size         | Large         | Color        | Red           | COOL-T-L-R  |
| cool-t-shirt    |               | Size         | Small         | Color        | Blue          | COOL-T-S-B  |

---

### Image Preparation and SEO

-   **Image Sizing:** Use a consistent aspect ratio and size (e.g., 2048x2048 pixels for square images) for a professional look.
-   **File Naming:** Rename image files to be descriptive and SEO-friendly before uploading (e.g., `brand-product-name.jpg`).
-   **Image URLs:** Upload images to Shopify's `Settings > Files` section first. This is more reliable than external hosts. Copy the generated URL and paste it into the `Image Src` column.
-   **Alt Text:** Always fill in the `Image Alt Text` column. This is vital for accessibility and image search SEO. Describe the image accurately (e.g., "A bottle of Extra Virgin Olive Oil on a marble countertop").

---

### The Import Process

1.  Navigate to **Products** in your Shopify admin.
2.  Click **Import**.
3.  Click **Add file** and select your prepared CSV.
4.  **Crucial:** If you are updating existing products, check the box **"Overwrite any current products that have the same handle."** If you are only adding new products, leave this unchecked to be safe.
5.  Click **Upload and continue**.
6.  Shopify will show a preview. Carefully review the column mappings to ensure they are correct.
7.  Click **Import products**. The import will run in the background. You'll receive an email notification when it's complete.

---

### Post-Import Verification

Do not assume the import was perfect. Always perform these checks:
- [ ] **Spot-Check Products:** Open 5-10 imported products (including variants) on the storefront.
    -   Are the images correct?
    -   Is the title, price, and description correct?
    -   Do all variants (e.g., sizes, colors) appear and function correctly?
- [ ] **Check Collections:** If you used tags to automate collections, verify that products are appearing in the correct collections.
- [ ] **Review for Import Errors:** Check the email notification from Shopify for any reported errors.

---

### Common Errors and Solutions

-   **"Validation failed: Handle cannot be blank"**: The `Handle` column is missing for a product. Ensure every product has a unique handle.
-   **"Validation failed: Options are not unique"**: You have two variants with the exact same option values (e.g., two variants are both "Small" and "Red"). Each variant must be unique.
-   **"Image download failed"**: The URL in `Image Src` is broken, not publicly accessible, or not a direct image link. Verify the URL by pasting it into your browser.
-   **"Duplicate products created"**: This happens if you re-import without checking the "Overwrite" box. You will need to manually delete the duplicates.
-   **"Invalid CSV format"**: The file is not a properly formatted CSV. This often happens if you save it as a different file type or use incorrect delimiters.
    -   **Solution**: Save your file as a `CSV (Comma-delimited)` file. Use a template exported from Shopify to avoid formatting issues.

---

### Advanced Tips

-   **Use Spreadsheet Formulas:** Use functions like `CONCATENATE` to build handles or SKUs from product titles and options, saving significant time.
-   **Metafields:** For custom data, you'll need to use a third-party app (like Shopify's own Metafields editor) to bulk-import metafields after the main product import.
-   **Partial Imports:** You can import a CSV with just `Handle` and `SKU` columns along with the data you want to update (e.g., `Variant Price`) to quickly modify existing products.
-   **Chunk Large Imports:** For imports with thousands of products, split your CSV into smaller files (e.g., 500-1000 rows per file). This makes the import process more stable and allows you to find and fix errors more easily. If one small batch fails, it doesn't halt the entire import.