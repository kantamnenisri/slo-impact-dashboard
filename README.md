# SLO Business Impact Dashboard

**Live Demo: [https://slo-impact-dashboard.onrender.com/](https://slo-impact-dashboard.onrender.com/)**

A full-stack application to quantify the business value of service reliability and visualize SLO (Service Level Objective) health.

## Features
- **SLO Impact Calculator**: Compute error budget, burn rate, and revenue at risk.
- **Health Status**: Real-time status assessment (HEALTHY / AT RISK / BREACHED).
- **PDF Export**: Generate a clean reliability report for stakeholders.
- **Modern UI**: Built with Tailwind CSS for a professional look.
- **SRE Ready**: Includes a `/health` endpoint for monitoring.

## Tech Stack
- **Backend**: Python FastAPI
- **Frontend**: Plain HTML5 + Tailwind CSS + html2pdf.js
- **Logic**: Custom SLO math module in `app/calculator.py`

## Local Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Access the Dashboard**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Deployment

### Render
This project is ready for deployment on [Render](https://render.com/).
1. Connect your GitHub repository to Render.
2. Render will automatically detect the `render.yaml` file.
3. Your app will be deployed as a Web Service.

## SLO Math Logic
- **Error Budget Remaining**: Total monthly allowed downtime minus current downtime.
- **Burn Rate**: (1 - Current Uptime) / (1 - SLO Target). A burn rate > 1 means you are consuming budget faster than allowed.
- **Revenue at Risk**: Current downtime duration multiplied by the calculated downtime cost per hour (Monthly Revenue / 720 hours).


## 💡 Inspiration
This project is a reference implementation exploring concepts related to 
multi-cloud reliability engineering. The author holds USPTO patent 
applications in this domain (US 19/325,718 and US 19/344,864).

## Health Check
- Added /ping endpoint for automated health monitoring.
