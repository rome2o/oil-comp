# Quotation Engine - Development Plan

This document outlines the tasks required to build the Oil Company Quotation Engine.

## Phase 1: Project Setup & Core Data Models

- [ ] **Project Initialization:**
    - [ ] Set up a new project using a suitable framework (e.g., Next.js with Refine.dev, as mentioned in the notes).
    - [ ] Initialize a database (e.g., PostgreSQL).
    - [ ] Configure the ORM (e.g., Prisma, TypeORM).

- [ ] **Define Core Schemas:**
    - [ ] Create database schema for `Customer`.
    - [ ] Create database schema for `Vendor`.
    - [ ] Create database schema for `RawMaterial`.
    - [ ] Create database schema for `PackagingMaterial`.
    - [ ] Create database schema for `LaborCategory`.
    - [ ] Create database schema for `Product` (including variants).
    - [ ] Create database schema for `BillOfMaterial` (BOM).
    - [ ] Create database schema for `Quote` and `QuoteItem`.

## Phase 2: Core Logic - Cost & Price Calculation

- [ ] **Costing Engine:**
    - [ ] Implement logic to calculate `Total Manufacturing Cost` by rolling up costs from BOMs (Raw Materials, Packaging, Labor).
    - [ ] Implement logic to handle tiered pricing based on quantity for materials.
    - [ ] Implement logic for currency conversion for costs from international vendors.
    - [ ] Implement logic to calculate "landed costs" including freight and import duties.
    - [ ] Add logic for special costs like "Flush Oil".

- [ ] **Pricing Engine:**
    - [ ] Implement logic to calculate the `Estimated Sale Price` based on total cost and default markup rules.
    - [ ] Implement logic to handle tiered pricing for bulk orders (customer-facing).
    - [ ] Implement tax calculation engine for US (state-based) and international (GST/VAT) customers.

## Phase 3: Quotation Workflow & UI

- [ ] **Sales Flow UI:**
    - [ ] Build the main quotation creation interface.
    - [ ] Implement customer selection and item selection/import (for SKUs).
    - [ ] Implement the "Quick Quote" feature allowing bulk item list uploads.
    - [ ] Develop UI for dynamically recalculating quotes when quantities change.

- [ ] **Review & Approval Flow:**
    - [ ] Create a dashboard to list and filter all quotes.
    - [ ] Implement the quote status state machine (`Draft`, `Under Review`, `Approved`, `Rejected`).
    - [ ] Build the interface for the Finance team to review cost breakdowns and approve/reject quotes.

- [ ] **Output & Communication:**
    - [ ] Implement PDF and Excel export functionality for quotes.
    - [ ] Design a standardized email template for sending quotes to customers.

## Phase 4: NetSuite Integration

- [ ] **API Connection:**
    - [ ] Establish a secure connection to the NetSuite API.
    - [ ] Handle authentication and error handling.

- [ ] **Data Synchronization:**
    - [ ] Implement a scheduled job to sync `Customers` from NetSuite.
    - [ ] Implement a scheduled job to sync `Products` from NetSuite.
    - [ ] Implement logic to pull historical sales order data for the "Last Sale Price Comparison" feature.

- [ ] **Data Push:**
    - [ ] Implement functionality to push an `Approved` quote to NetSuite to create a Sales Order.

## Phase 5: Procurement Module (Phase 2 of Project)

- [ ] **Vendor Management:**
    - [ ] Build UI to manage the list of vendors.
    - [ ] Implement the vendor approval and sample tracking workflow.

- [ ] **Purchase Orders:**
    - [ ] Design a workflow for creating and managing Purchase Orders (POs) for raw materials.
    - [ ] Track inbound materials and timelines.

## Phase 6: System Administration & UX

- [ ] **Role-Based Access Control (RBAC):**
    - [ ] Implement user authentication and roles (e.g., `Sales`, `Finance`, `Admin`).
    - [ ] Restrict access to features based on user roles (e.g., only Finance can approve).

- [ ] **Product & Data Management:**
    - [ ] Build interfaces for admins to manage products, BOMs, and costing rules.
    - [ ] Implement SKU mapping interface for both customer and vendor SKUs.

- [ ] **UI/UX Refinements:**
    - [ ] Create product card views and detailed product pages.
    - [ ] Add hover-over details for pricing specifications.

## Phase 7: Testing & Deployment

- [ ] **Testing:**
    - [ ] Collect 20-30 sample quotes to use as a basis for test cases.
    - [ ] Write unit tests for the costing and pricing logic.
    - [ ] Write integration tests for the full quotation workflow (create -> approve -> push to NetSuite).

- [ ] **Deployment:**
    - [ ] Set up a staging environment for UAT (User Acceptance Testing).
    - [ ] Configure a CI/CD pipeline for automated builds and deployments.
    - [ ] Deploy the application to a production environment.
