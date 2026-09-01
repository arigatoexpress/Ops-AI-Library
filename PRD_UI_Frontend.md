# Product Requirements Document — UI (Frontend)

## SecureAlly — Security-By-Design Intake & Tracking Portal

| Field | Value |
|-------|-------|
| Document Version | 1.0 |
| Date | 2026-05-21 |
| Status | Draft |
| Product Name | SecureAlly |
| Business Owner | InfoSec / Architecture Team |

---

## 1. Product Overview

SecureAlly is a web-based portal that enables FedEx Project Teams (Initiative Owners, Project Managers, Architects) to submit, track, and manage Security-By-Design (SBD) intake requests through a single, guided workflow. The portal replaces fragmented email/spreadsheet-driven processes with an auditable, real-time experience.

---

## 2. User Personas

| Persona | Description | Primary Goal |
|---------|-------------|--------------|
| **Project Initiator** | FedEx team member starting a new initiative | Submit an SBD intake form quickly and track its review status |
| **Project Manager** | Coordinates initiative timelines and team | View status dashboard, ensure team responds to review outcomes |
| **Architect** | Provides architecture & deployment inputs | Fill relevant intake sections, review feedback |
| **Security Reviewer** | Reviews submitted intakes (L1) | Receive notifications, access submitted details, provide Go/No-Go |
| **Admin** | Manages system settings, users, lookups | Configure system, manage user access |

---

## 3. Information Architecture & Navigation

### 3.1 Global Navigation Structure

```
┌─────────────────────────────────────────────────────────────┐
│  [FedEx Logo]  [Breadcrumb]         [Search] [Bell] [Avatar]│
├──────────┬──────────────────────────────────────────────────┤
│ Sidebar  │                                                  │
│          │         Main Content Area                        │
│ • Home   │                                                  │
│ • Intake │                                                  │
│ • Search │                                                  │
│          │                                                  │
│ Quick    │                                                  │
│ Actions  │                                                  │
│ • AEGIS  │                                                  │
│ • Query  │                                                  │
│          │                                                  │
│ Recent   │                                                  │
│ • ...    │                                                  │
│          │                                                  │
│──────────│                                                  │
│ Settings │                                                  │
│ Admins   │                                                  │
│ [Status] │                                                  │
└──────────┴──────────────────────────────────────────────────┘
```

### 3.2 Navigation Items

| Section | Item | Behavior |
|---------|------|----------|
| Route | `/` (root URL) | Automatically redirects to `/dashboard` — no landing page or splash screen |
| Primary | Home | Navigates to Dashboard (default landing page) |
| Primary | Intake Form | Opens the "Before You Begin" modal, then intake wizard |
| Primary | Search | Opens global search for initiatives |
| Quick Actions | AEGIS GPT | Opens AEGIS GPT tool (external link or embedded) |
| Quick Actions | Infosec Query | Opens Infosec query interface |
| Recent | (Dynamic) | Shows recently viewed initiatives |
| Footer | Settings | Opens user/system settings |
| Footer | Admins | Opens admin panel (visible to admin role only) |
| Footer | Status Pill | Shows system health — "System online & Secure" |

### 3.3 Top Navigation Bar

| Element | Behavior |
|---------|----------|
| FedEx Logo | Click navigates to Home |
| Sidebar Toggle (Left) | Collapses/expands left sidebar |
| Breadcrumb | Shows current page path; each segment is clickable |
| Search Input | Click expands search; type to search initiatives |
| Notifications Bell | Click opens notification dropdown with recent alerts |
| User Avatar | Click opens profile dropdown (profile, logout) |

---

## 4. Screens & User Flows

---

### 4.1 Home — Dashboard

**Purpose:** Default landing page. Shows a personalized greeting and a table of the user's SBD requests.

#### Welcome Section

| Element | Content |
|---------|---------|
| Heading | "Welcome, {First Name}" |
| Subheading | "Track and manage your security review requests in one place." |

#### Your Requests Table

Displays all intake requests associated with the logged-in user.

**Columns:**

| Column | Description |
|--------|-------------|
| NAME | Initiative name |
| PROJECT ID | Numeric project identifier |
| REVIEW ID | SBD number (format: SBD-XXXXXXXXXXX) |
| STATUS | Current review status (pill badge) |
| COMPLETE % | Percentage of review completion |

**Status Values & Visual Treatment:**

| Status | Color | Meaning |
|--------|-------|---------|
| UNDER REVIEW | Purple pill | Intake submitted, review in progress |
| GO | Green pill | Approved to proceed |
| NO GO | Red pill | Rejected, action required |

**Interactions:**

- Click on any row → Navigate to Request Detail page. **The entire row is the click target** (not just the name column). Row displays hover state and pointer cursor across all cells.
- Click on column header → Sort ascending/descending
- Scroll → Load more rows (pagination)
- Left-edge accent bar on flagged/selected rows (yellow)

**Mocked Data:**

| NAME | PROJECT ID | REVIEW ID | STATUS | COMPLETE % |
|------|-----------|-----------|--------|------------|
| ENTERPRISE INTERNAL TRACKING | 7781 | SBD-88423854993 | UNDER REVIEW | 48% |
| CLOUD MIGRATION PLATFORM | 8842 | SBD-77291034521 | GO | 88% |
| CUSTOMER PORTAL REDESIGN | 6234 | SBD-99182736450 | NO GO | 72% |
| DATA LAKE MODERNIZATION | 9012 | SBD-55648271039 | UNDER REVIEW | 30% |
| MOBILE DELIVERY APP V3 | 4456 | SBD-33917254680 | UNDER REVIEW | 56% |
| WAREHOUSE AUTOMATION | 5523 | SBD-44028163795 | GO | 20% |
| PARTNER API GATEWAY | 7101 | SBD-66839472150 | UNDER REVIEW | 0% |

---

### 4.2 Request Detail Page

**Purpose:** Shows comprehensive details of a specific initiative when user clicks a row from the dashboard.

**Breadcrumb:** Home / {Initiative Name}

#### 4.2.1 Project Metadata Card

Displays key project information in a card layout.

| Field | Mocked Value |
|-------|--------------|
| Project Owner | Sarah Mitchell |
| Project Manager | David Chen |
| Assigned Architects | Maria Garcia, James Wilson |
| Percentage Complete | 48% (with progress bar) |
| Assigned BDM/BSO | Robert Taylor |
| Assigned Enterprise Arch | Lisa Anderson |
| Assigned PM | David Chen |
| Status | UNDER REVIEW |

**Interactions:**
- Progress bar visually reflects completion percentage
- Data loads automatically on page render

#### 4.2.2 Team Members Card

Shows initiative team members with avatars (initials), names, and roles.

**Mocked Data:**

| Avatar | Name | Role |
|--------|------|------|
| SM | Sarah Mitchell | Initiative Owner |
| DC | David Chen | Project Manager |
| MG | Maria Garcia | Solution Architect |

**Interactions:**
- Click arrow icon on a team member row → Opens member profile/contact

#### 4.2.3 Observation Notes Card

Displays reviewer notes and observations chronologically.

**Mocked Data:**

| Date | Note | Tag |
|------|------|-----|
| May 15, 2026 | Architecture diagram needs revision for cloud failover paths. | INFOSEC ARCHITECT |
| May 12, 2026 | Data flow between services lacks encryption notation. | REVIEWER |
| May 10, 2026 | Initial submission received. Assigning L1 reviewer. | INFOSEC ARCHITECT |

**Interactions:**
- "View all →" link at bottom → Opens full observation history

#### 4.2.4 Documents Card

Shows uploaded documents/artifacts associated with the initiative.

**Mocked Data:**

| Document Title | Type | Quality Score |
|----------------|------|---------------|
| Solution Architecture Diagram | PDF | 7.2 / 10 |
| Initiative Checklist (Required) | DOCX | 8.5 / 10 |
| Financial Architecture | XLSX | 6.8 / 10 |

**Interactions:**
- Click download icon → Downloads the document
- Quality score is read-only (set by reviewers)

---

### 4.3 Intake Form Flow

**Entry Point:** User clicks "Intake Form" in the left sidebar.

#### 4.3.1 Before You Begin Modal

**Purpose:** Inform the user about form requirements before starting.

| Element | Content |
|---------|---------|
| Title | "Before you begin" |
| Body | "This form is to be completed at the point of project initiation. Your responses will be used to determine the scope of your initiative, select the relevant security patterns and baselines, and generate a tailored set of security requirements for your project." |
| Emphasis | "All questions are mandatory. If a definitive answer is not yet available, select 'Don't know yet' and ensure the form is updated prior to your security review session. Incomplete or deferred answers may delay the initiation of your Secure by Design engagement." |
| Action | "Start Intake" button |

**Interactions:**
- Click "Start Intake" → Dismiss modal, navigate to Step A (Project Basics)
- Click outside modal or press Escape → Close modal, stay on current page

---

#### 4.3.2 Intake Form Wizard — Multi-Step Stepper

The intake form is a **5-step wizard** with a horizontal stepper indicator at the top.

**Steps:**

| Step | Label | Badge |
|------|-------|-------|
| A | Project Basics | A |
| B | Deployment | B |
| C | Users & Access | C |
| D | Data Classification | D |
| E | Data Residency | E |

**Stepper Behavior:**
- Active step: Purple badge with white letter, purple-tinted background
- Inactive steps: Light purple badge with purple letter
- Completed steps: Checkmark replaces letter badge
- Clicking a completed step navigates back with data preserved
- Clicking a future (uncompleted) step is disabled

**Form-Wide Rules:**
- "Next" button is **disabled by default** until all required fields on the current step are completed
- "Back" button always navigates to the previous step with **pre-filled data preserved**
- All form state persists across forward/back navigation within the session

---

#### Step A — Project Basics

**Fields:**

| # | Field | Input Type | Placeholder / Options | Required |
|---|-------|------------|----------------------|----------|
| 1 | Brief Description | Textarea | "2-3 sentence description what it does, who it serves, and the primary business outcome" | Yes |
| 2 | Project Stakeholder — Requestor | Text input with autocomplete | "Name or Employee ID" | Yes |
| 3 | Project Stakeholder — Delegate(s) | Text input with autocomplete | "Name or Employee ID" | No |
| 4 | Project Stakeholder — Manager | Text input with autocomplete | "Name or Employee ID" | Yes |
| 5 | Project Stakeholder — MD | Text input with autocomplete | "Name or Employee ID" | Yes |
| 6 | Project Stakeholder — VP | Text input with autocomplete | "Name or Employee ID" | Yes |
| 7 | Solution Type | Dropdown (single select) | "Select Solution Type" | Yes |

**Solution Type Options (Mocked):**

- New Application
- Application Enhancement
- Infrastructure Change
- Third-Party Integration
- Cloud Migration
- API Development
- Data Platform

**Interactions:**
- Info icon (ⓘ) next to each field label → Hover shows help tooltip with guidance
- Stakeholder inputs → Typing triggers employee lookup/autocomplete suggestions
- Selecting a suggestion populates the field
- All required fields filled → "Next" button becomes enabled
- Click "Next" → Validates, advances to Step B
- Click "Back" → Disabled on Step A (first step)

**Mocked Autocomplete Suggestions (for Stakeholder fields):**

| Typed | Suggestions |
|-------|-------------|
| "Sar" | Sarah Mitchell (SM-123456), Sarah Johnson (SJ-789012) |
| "Dav" | David Chen (DC-345678), David Park (DP-901234) |

---

#### Step B — Deployment

**Fields:**

| # | Field | Input Type | Required |
|---|-------|------------|----------|
| 1 | Where will this solution be deployed? | Multi-select dropdown | Yes |
| 2 | Will FedEx-owned software be installed or run on devices/environments not owned or managed by FedEx? | Single-select (Yes/No/Don't know yet) | Yes |

**Deployment Options (Multi-select Mocked):**

- [ ] FedEx Cloud - IaaS (e.g., GCE, EC2, Bare Metal VMs)
- [ ] FedEx Cloud - PaaS (e.g., Cloud Run, App Service, RDS)
- [ ] SaaS / Third-Party Hosted
- [ ] FedEx Data Center / On-Prem
- [ ] Edge / IoT Devices
- [  ] *Don't know yet* (italic, deferred)

**Multi-Select Behavior:**
- Click control → Opens options panel with checkboxes
- Click checkbox or row → Toggles selection
- Multiple selections allowed
- Selected items shown as chips/tags in the control
- "Don't know yet" can be selected alongside others (represents deferred)

**Interactions:**
- All required fields answered → "Next" enabled
- Click "Next" → Advance to Step C
- Click "Back" → Return to Step A with pre-filled data

---

#### Step C — Users & Access

**Fields:**

| # | Field | Input Type | Required |
|---|-------|------------|----------|
| 1 | Who will use this solution? | Multi-select dropdown | Yes |
| 2 | How will users authenticate? | Single-select dropdown | Yes |
| 3 | Will external (non-FedEx) users access this solution? | Single-select (Yes/No/Don't know yet) | Yes |
| 4 | What level of access will users have? | Single-select dropdown | Yes |

**Users Options (Mocked):**

- FedEx Employees (Internal)
- FedEx Contractors
- Third-Party Partners
- Customers (External)
- Automated Systems / Service Accounts
- Don't know yet

**Authentication Options (Mocked):**

- Single Sign-On (SSO)
- Certificate-Based Authentication
- API Key / Token
- Multi-Factor Authentication (MFA)
- Don't know yet

**Access Level Options (Mocked):**

- Read Only
- Read/Write
- Administrative
- Custom Role-Based
- Don't know yet

**Interactions:**
- Same pattern as previous steps
- "Next" enabled when all required fields complete
- "Back" returns to Step B with data preserved

---

#### Step D — Data Classification

**Fields:**

| # | Field | Input Type | Required |
|---|-------|------------|----------|
| 1 | What type of data will this solution process? | Multi-select dropdown | Yes |
| 2 | Will this solution store Personally Identifiable Information (PII)? | Single-select (Yes/No/Don't know yet) | Yes |
| 3 | What is the highest data classification level? | Single-select dropdown | Yes |

**Data Type Options (Mocked):**

- Customer Personal Data
- Employee Data
- Financial / Payment Data
- Shipment / Logistics Data
- Health / Medical Information
- Intellectual Property
- System / Infrastructure Logs
- Don't know yet

**Classification Level Options (Mocked):**

- Public
- Internal Use Only
- Confidential
- Highly Confidential / Restricted
- Don't know yet

**Interactions:**
- Same field-level validation pattern
- "Next" enabled when all required fields complete
- "Back" returns to Step C with data preserved

---

#### Step E — Data Residency

**Fields:**

| # | Field | Input Type | Required |
|---|-------|------------|----------|
| 1 | Where will data be stored at rest? | Multi-select dropdown | Yes |
| 2 | Will data cross international borders during processing or transfer? | Single-select (Yes/No/Don't know yet) | Yes |
| 3 | Are there specific regulatory requirements for data location? | Single-select (Yes/No/Don't know yet) | Yes |

**Data Residency Options (Mocked):**

- United States
- European Union (EU)
- Asia-Pacific (APAC)
- Multi-Region / Global
- FedEx Data Center Only
- Don't know yet

**Interactions:**
- "Next" button is replaced by **"Submit Intake Form"** button on this final step
- "Submit Intake Form" is disabled until all required fields are complete
- Click "Submit Intake Form" → Navigate to Confirmation Page
- Click "Back" → Return to Step D with data preserved

---

### 4.4 Confirmation Page

**Purpose:** Confirms successful submission and shows the user their assigned SBD number.

**Content:**

| Element | Value |
|---------|-------|
| Success Icon | Green checkmark |
| Heading | "Intake Form Submitted Successfully" |
| SBD Number | SBD-{auto-generated number} (e.g., SBD-55203847192) |
| Message | "Your Security-By-Design intake has been submitted. An L1 Security Reviewer will be notified and your request will appear on your dashboard." |
| Primary Action | "Go to Dashboard" button → Navigates to Home |
| Secondary Action | "View Submission" button → Navigates to Request Detail |

**Mocked Confirmation Data:**

| Field | Value |
|-------|-------|
| Initiative Name | (from Step A — Brief Description) |
| SBD Number | SBD-55203847192 |
| Submitted By | Jane Doe |
| Submitted At | May 21, 2026, 2:34 PM CST |
| Status | UNDER REVIEW |
| Assigned Reviewer | Pending Assignment |

---

## 5. Shared UI Patterns

### 5.1 Status Pill Component

A small badge/pill indicating the current review state of an initiative.

| Status | Visual Tone | Meaning |
|--------|-------------|---------|
| UNDER REVIEW | Purple | Intake submitted, review in progress |
| GO | Green | Approved — initiative may proceed |
| NO GO | Red | Rejected — action or revision required |

Each pill includes a leading dot indicator + uppercase label text.

### 5.2 Buttons

| Type | Usage | When |
|------|-------|------|
| Primary | Main forward actions | "Next", "Submit Intake Form", "Start Intake", "Go to Dashboard" |
| Primary (Disabled) | Blocked forward action | All required fields on current step are not yet completed |
| Secondary (Outlined) | Backward/cancel actions | "Back" button in form wizard |

**Rules:**
- "Next" / "Submit" buttons are **always visible and enabled** (not disabled). Clicking with incomplete or invalid fields triggers validation and shows errors — the button does not silently do nothing.
- Only one primary action per screen section
- Disabled buttons are visually muted but remain visible (not hidden)

**Validation Error Display (on button click):**
- An **error summary banner** appears at the top of the current form step, listing all validation errors
- **Inline error messages** appear directly below each invalid field with a red border
- Errors **clear automatically** when the user corrects the corresponding field
- The page scrolls to the first error if errors are off-screen

### 5.3 Form Field Patterns

| Pattern | Behavior |
|---------|----------|
| Required field — empty on submit attempt | Inline error message appears directly below the field |
| Dropdown — focused | Visual highlight to indicate active state |
| Autocomplete / Lookup | Suggestion list appears after 2+ characters typed; user selects from results |
| Tooltip / Info icon (ⓘ) | Help text appears on hover; disappears when cursor moves away |
| Multi-select | Selected values appear as removable chips/tags inside the input control |
| Textarea | Free-form text entry; grows vertically or shows scrollbar for long content |

**Multi-Select Control Structure:**
- The trigger element **must be a `<div>` with `role="combobox"`** (not a `<button>`), because chip remove buttons ("×") inside the trigger would create invalid nested `<button>` elements and cause hydration errors in SSR frameworks
- Each selected chip has a small "×" button to remove the selection
- Clicking outside any open dropdown **must close it** (click-outside handler required)

**Dropdown / Popover Rules:**
- All dropdowns must have a `max-height` with internal scroll for long option lists
- Dropdowns render with sufficient `z-index` to overlay content below, but must **not permanently obstruct** navigation buttons (Next/Back/Submit)
- Clicking outside any open dropdown or popover closes it immediately
- Only one dropdown may be open at a time

### 5.4 Cards

Content containers used for grouping related information on detail pages.

| Property | Behavior |
|----------|----------|
| Layout | Rounded container with subtle border |
| Header | Icon + bold title text at top |
| Content | Structured rows of label/value pairs, lists, or tiles |
| Actions | Optional link ("View all →") or icon buttons (download, arrow) |

### 5.5 Notifications (Bell Icon)

| Trigger | Notification Message |
|---------|---------------------|
| Intake submitted | "Intake SBD-XXXX submitted successfully" |
| Status changed | "Your initiative {name} status changed to {status}" |
| Reviewer assigned | "Reviewer {name} assigned to SBD-XXXX" |
| Review complete | "{name} review completed — outcome: {Go/No Go}" |

**Behavior:**
- Unread count shown as badge on the bell icon
- Click bell → Dropdown list of recent notifications (most recent first)
- Click a notification → Navigate to the related initiative detail page
- Notifications are marked read once the dropdown is opened

### 5.6 Sidebar Collapse

| State | Behavior |
|-------|----------|
| Expanded | Full sidebar with icons + text labels visible |
| Collapsed | Icons only; text labels hidden; tooltip on hover shows label |
| Toggle | Click sidebar toggle button in top bar to switch between states |

### 5.7 Breadcrumb

- Shows hierarchical path: e.g., "Home / Enterprise Internal Tracking"
- Each segment except the current page is clickable and navigates to that level
- Current page segment is displayed as plain text (non-clickable)

### 5.8 Empty States

| Context | Content |
|---------|---------|
| No requests on dashboard | Illustration + "You have no requests yet." + CTA to start intake |
| No search results | "No initiatives found." + suggestion text |
| No observations | "No observation notes yet." |
| No documents | "No documents uploaded." |

### 5.9 Loading States

- Skeleton placeholders (shimmer blocks) appear in place of content while data loads
- Form submission shows a spinner inside the submit button + button becomes disabled
- Page transitions show a subtle top-of-page progress indicator

---

## 6. User Flow Summary

```
[Home — Dashboard (Landing Page)]
        │
        ├──── Click row ──────────► [Request Detail Page]
        │                                   │
        │                                   ├── View Metadata
        │                                   ├── View Team Members
        │                                   ├── View Observations
        │                                   └── Download Documents
        │
        ├──── Click "Intake Form" ──► [Before You Begin Modal]
        │                                   │
        │                               Click "Start Intake"
        │                                   │
        │                                   ▼
        │                           [Step A: Project Basics]
        │                                   │ Next
        │                                   ▼
        │                           [Step B: Deployment]
        │                                   │ Next
        │                                   ▼
        │                           [Step C: Users & Access]
        │                                   │ Next
        │                                   ▼
        │                           [Step D: Data Classification]
        │                                   │ Next
        │                                   ▼
        │                           [Step E: Data Residency]
        │                                   │ Submit
        │                                   ▼
        │                           [Confirmation Page]
        │                                   │
        │                                   ├── "Go to Dashboard" → Home
        │                                   └── "View Submission" → Request Detail
        │
        ├──── Click "Search" ──────► [Search Page]
        │
        ├──── Click "Settings" ────► [Settings Page]
        │
        └──── Click "Admins" ──────► [Admin Panel] (admins only)
```

---

## 7. Responsive & Accessibility Requirements

| Requirement | Description |
|-------------|-------------|
| Minimum viewport | Desktop-first; minimum supported width 1280px |
| Sidebar collapse | On narrow viewports or toggle, sidebar collapses to icon-only mode |
| Keyboard navigation | All interactive elements reachable via Tab; Enter/Space to activate |
| Screen readers | All form fields have associated labels; status pills have aria-label |
| Color contrast | All text meets WCAG 2.1 AA contrast ratios |
| Focus indicators | Visible focus ring on all interactive elements |
| Error announcements | Form validation errors announced to assistive technology |

---

## 8. Loading & Empty States

| Scenario | UI Behavior |
|----------|-------------|
| Dashboard loading | Skeleton placeholders for table rows |
| No requests yet | Empty state illustration + "You have no requests yet. Start your first intake." with CTA button |
| Request detail loading | Skeleton cards for metadata, team, observations, documents |
| Search — no results | "No initiatives found matching your search." with suggestion to adjust filters |
| Form submission in progress | "Submit" button shows spinner, disabled to prevent double-submit |

---

## 9. Error States

| Scenario | UI Behavior |
|----------|-------------|
| Form field validation | Red border + inline message below field (e.g., "This field is required") |
| Submission failed | Toast notification: "Submission failed. Please try again." with retry option |
| Page not found | 404 illustration + "The page you're looking for doesn't exist." + "Go Home" link |
| System unavailable | Full-page message: "SecureAlly is temporarily unavailable. Please try again later." |

---

## 10. Mocked Data Summary

All screens use the following mocked dataset for demonstration and development purposes:

**Logged-In User:**
- Name: Jane Doe
- Employee ID: JD-567890
- Role: Initiator
- Email: jane.doe@fedex.com

**Mocked Initiatives (7 total):** See Section 4.1 table

**Mocked Team Members:** See Section 4.2.2

**Mocked Observation Notes:** See Section 4.2.3

**Mocked Documents:** See Section 4.2.4

**Mocked Dropdown Options:** See Sections 4.3.2 (Steps A–E)

**ID Format Requirements for Mocked Data:**

| Entity | Format | Example |
|--------|--------|---------|
| Initiative ID | Integer | `1`, `2`, `3` |
| SBD Number | `SBD-` + 11-digit numeric string | `SBD-88423854993` |
| Document ID | UUID v4 | `a1b2c3d4-e5f6-4890-abcd-ef1234567890` |
| Employee ID | Prefix + 6-digit number | `SM-123456` |
| Notification ID | UUID v4 | `f47ac10b-58cc-4372-a567-0e02b2c3d479` |

> **Important:** All IDs used in mock data, API routes, and download links must conform to these formats. Mismatched formats (e.g., plain integers where UUIDs are expected) will cause runtime validation errors.

---

## 11. Out of Scope (UI)

The following are explicitly **not** part of this UI PRD:

- **Authentication and authorization** — All screens are accessible without login for the MVP. No SSO, session management, role-based access control, or login/logout flows are in scope. User identity is mocked (see Section 10). Auth-related fields in the data model (e.g., "Authentication Method" in Step C) refer to the **initiative being reviewed**, not application-level auth.
- Security Reviewer workflow screens (review queue, Go/No-Go decision UI)
- Admin panel detailed screens (user management, lookup configuration)
- AEGIS GPT interface
- Infosec Query interface
- Email/Teams notification templates
- Report generation / export
- Mobile-responsive layouts (desktop-first only)
- Bulk operations on multiple initiatives
- File upload within intake form
- Real-time collaboration / multi-user editing

---

## 12. Open Questions

| # | Question | Impact |
|---|----------|--------|
| 1 | What are the exact dropdown options for "Solution Type" in Step A? | Blocks final field options |
| 2 | Should the sidebar "Recent" section show last 3 or last 5 initiatives? | UX decision |
| 3 | Is there a maximum character limit for the "Brief Description" textarea? | Validation rule |
| 4 | Should clicking a stepper step (completed) allow editing, or is it read-only after submission? | Interaction model |

---

## 13. Development Environment Requirements

The following requirements apply to the development and local testing environment:

| Requirement | Description |
|-------------|-------------|
| Network IP access | The app must be accessible via both `localhost` and LAN/network IP (e.g., `192.168.x.x`) during development. The dev server must allow cross-origin requests from network IPs for HMR (Hot Module Replacement) WebSocket connections. |
| CSP in development | `connect-src` in the Content-Security-Policy header must include WebSocket origins (`ws://localhost:*`, `ws://192.168.*:*`) in development mode to avoid blocking HMR and client-side hydration. |
| Allowed dev origins | Next.js `allowedDevOrigins` (or equivalent framework config) must be configured to include the machine's network IP so that client-side JavaScript hydrates correctly when accessed from other devices on the same network. |
| Cache clearing | After config changes (e.g., `next.config.ts`), the `.next/` build cache should be cleared and the dev server restarted to avoid stale bundle issues. |
| Port conflicts | If the default port (3000) is occupied by a stale process, the dev server must detect and warn — not silently start on an alternate port, which can cause confusion. |

> **Why this matters:** If the dev server blocks cross-origin HMR connections, client-side JavaScript fails to hydrate. The page renders as static HTML but **no buttons, dropdowns, or interactive elements will respond to clicks** — appearing completely broken even though the server is running.
| 5 | What happens if the user closes the browser mid-form — is there auto-save/draft? | Session persistence |
| 6 | What content appears in the "Search" page and what filters are available? | Separate screen spec needed |
