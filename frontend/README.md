# SnapReport

AI-powered monthly real estate market report generator for Snaphomz partner agents.

## Problem

Real estate agents know they should send monthly market updates to homeowners and prospective sellers. However, creating these reports manually requires:

- Collecting local market statistics
- Writing market analysis
- Designing branded reports
- Distributing reports to clients

This process can take several hours every month, leading many agents to skip it entirely.

## Solution

SnapReport automates the process by allowing an agent to:

1. Enter a target ZIP code
2. Provide agent details
3. Upload a profile photo
4. Generate an AI-powered market report
5. Download a branded PDF within seconds

The report contains:

- Market statistics
- AI-generated market analysis
- Agent branding
- Snaphomz branding
- Professional PDF export

---

## Features

### Agent Profile

- Agent Name
- Agent Email
- Agent Phone Number
- Agent Photo Upload

### Market Data

- Median Home Price
- Days on Market
- List-to-Sale Ratio
- New Listings
- Inventory Months

### AI Market Narrative

Market commentary is generated using a Large Language Model through the Groq API.

### PDF Export

Generates a branded PDF report containing:

- Snaphomz logo
- Agent information
- Agent photo
- Market metrics
- AI-generated narrative

---

## Architecture

```text
React Frontend
       |
       v
FastAPI Backend
       |
       +---- Synthetic Market Dataset
       |
       +---- Groq LLM
       |
       +---- PDF Generation
```

---

## Tech Stack

### Frontend

- React
- Vite
- CSS

### Backend

- FastAPI
- Python

### AI

- Groq API
- Llama 3.3 70B

### PDF Generation

- jsPDF

### Data

- Synthetic ZIP-code market dataset

---

## Project Structure

```text
SnapReport/

├── backend/
│   ├── main.py
│   ├── market_data.json
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── assets/
│   │       └── logo.png
│   │
│   └── package.json
│
└── README.md
```

---

## Setup Instructions

### Backend

Install dependencies:

```bash
pip install fastapi uvicorn groq python-dotenv
```

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

Run:

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### Frontend

Install dependencies:

```bash
npm install
npm install jspdf
```

Run:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## API Endpoints

### Get Available ZIP Codes

```http
GET /zipcodes
```

### Generate Market Report

```http
GET /report/{zipcode}
```

Example:

```http
GET /report/32801
```

---

## Sample Workflow

1. Open SnapReport
2. Enter Agent Details
3. Upload Agent Photo
4. Enter Target ZIP Code
5. Click Generate Report
6. Review AI-generated report
7. Download Branded PDF

---

## Design Decisions

### Why Synthetic Market Data?

The challenge duration was limited to one hour.

To demonstrate the complete workflow, a synthetic dataset was created for multiple ZIP codes while maintaining a production-ready architecture.

The data layer can later be replaced with:

- RealEstateAPI.com
- MLS feeds
- Internal Snaphomz data sources

### Why Groq Instead of OpenAI?

Groq was used as a drop-in replacement for OpenAI because:

- Faster inference
- Free developer tier
- API-based integration
- Suitable for generating real estate narratives

The overall architecture remains unchanged.

---

## Future Enhancements

### Market Data Integration

- RealEstateAPI.com
- MLS integration

### Agent CRM

- Automatic profile loading
- Agent branding assets

### Report Distribution

- SendGrid integration
- Monthly scheduling

### Storage

- AWS S3
- Historical report archive

### Analytics

- Open rates
- Download tracking
- Lead attribution

---

## Business Value for Snaphomz

- Keeps agents engaged every month
- Increases Snaphomz brand visibility
- Automates agent marketing
- Improves homeowner engagement
- Creates recurring touchpoints that can convert into future listings

---

## Author

**Harshitha Narahari**

Built for **Snaphomz Hackathon 2.0**