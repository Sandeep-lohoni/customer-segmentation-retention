# Customer Segmentation & Retention Analysis

## Problem
Customer churn disproportionately impacts revenue in subscription and e-commerce businesses.
This project builds an end-to-end retention decision system using real transactional data.

## Solution Overview
- RFM-based customer segmentation
- Behavioral churn prediction
- Probabilistic CLV estimation
- ROI-driven retention decision engine

## Tech Stack
Python, Pandas, Scikit-learn, Lifetimes, FastAPI

## Key Outcomes
- Identified high-value at-risk customers
- Prioritized retention spending using CLV
- Avoided wasted retention on low-value churners

## Business Impact
Demonstrates how data science supports revenue-preserving decisions rather than
purely predictive modeling.

## How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
