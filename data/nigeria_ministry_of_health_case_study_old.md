**DATA SCIENCE PROJECT BRIEF**  
**Operation HealthShield**  
**Nigeria’s COVID-19 Resilience Analysis**  
**Advising the Federal Ministry of Health**  

**Client**  
Federal Ministry of Health, Federal Republic of Nigeria  
**Engagement Type**  
Data Science Consulting Sprint Project  
**Dataset**  
OWID COVID-19 Global Dataset (full file ≈160 MB)  
**Prepared for**  
Junior Data Science Consultants – Data Science Bootcamp  
**Classification**  
Internal / Training Use Only  

### 1. Executive Summary  

Nigeria has emerged from the acute phase of the COVID-19 pandemic, but the virus has not disappeared. With over 220 million people, diverse geographies, and limited hospital infrastructure, every future wave carries real risk to lives and the economy.  

The Honourable Minister of Health needs fresh, data-driven intelligence before the next Federal Executive Council meeting. Your team has been selected as the **first Junior Data Science Unit** embedded inside the Ministry.  

You are given the complete OWID COVID-19 global dataset. Your mandate: extract every Nigeria-specific row (country code “NGA”), turn two decades of global pandemic data into actionable insight for **Nigeria alone**, and produce a briefing pack that the Minister can take straight to the President.  

This is not a toy dataset exercise. Your findings will shape national vaccination strategy, hospital preparedness budgets, and early-warning triggers for 2026 and beyond. The Minister is counting on you.

### 2. About the Federal Ministry of Health  

Nigeria’s Ministry of Health is responsible for protecting one of Africa’s largest and youngest populations. After successfully weathering multiple COVID waves, the Ministry now faces a new reality: transmission is near-zero today, but vaccination coverage has stalled for almost two years.  

The Minister wants to shift from emergency response to **long-term resilience**. The central question the Ministry has given you is:  

**“Can we map Nigeria’s COVID-19 journey to a clear Resilience Quadrant, and does that quadrant reliably predict future healthcare stress and vaccination needs?”**  

Answering this will give the Minister the evidence needed to request budget, launch targeted campaigns, and brief the nation with confidence.

### 3. Your Dataset  

You have the full OWID COVID-19 dataset. Filter immediately to `iso_code == "NGA"` (Nigeria rows only).  

Key columns you will work with (all explained in class):  

**Identifiers & Time**  
- `date`  
- `year` (derived)  

**Cases & Deaths**  
- `new_cases`, `new_cases_smoothed`  
- `total_cases_per_million`  
- `new_deaths`, `new_deaths_smoothed`  
- `total_deaths_per_million`  
- `reproduction_rate`  

**Healthcare Pressure**  
- `hosp_patients_per_million`  
- `icu_patients_per_million`  
- `weekly_hosp_admissions_per_million`  
- `hospital_beds_per_thousand` (Nigeria’s structural capacity)  

**Vaccination**  
- `people_vaccinated_per_hundred`  
- `people_fully_vaccinated_per_hundred`  
- `total_boosters_per_hundred`  
- `new_vaccinations_smoothed`  

**Demographics & Context**  
- `population`  
- `median_age`  
- `diabetes_prevalence`  

**Data Quality Note**  
Expect missing values (especially early 2020 and late 2025+), zero entries during low-transmission periods, and occasional outliers. Cleaning and deciding how to handle zeros is part of the real-world challenge.

### 4. The Nigeria COVID Resilience Framework  

The Ministry’s Chief Epidemiologist has defined a simple but powerful **Resilience Quadrant** using two core axes from the dataset:  

| Quadrant       | Definition                                      | What it means for Nigeria                          |
|----------------|-------------------------------------------------|----------------------------------------------------|
| **Q1: Stable** | Low cases + High vaccination coverage           | Strong herd protection, minimal healthcare strain  |
| **Q2: Fragile** | Low cases + Low vaccination coverage            | Quiet today, but vulnerable to any new variant     |
| **Q3: Recovering** | Rising cases + Improving vaccination            | Early warning phase – time to act                  |
| **Q4: High Risk** | High cases + Low vaccination & high hospital load | Immediate emergency needed                         |

Your job is to assign **every Nigeria row** to one of these four quadrants and then use that classification to answer the Minister’s questions.

### 5. Engagement Objectives  

The Minister has given your team five clear objectives. Every insight must tie back to these.

**Objective 1 — Understand the Data Landscape**  
Profile the full Nigeria dataset: completeness, trends, and anomalies. Give the Minister a trustworthy foundation.

**Objective 2 — Map Nigeria’s Epidemic Curve & Waves**  
Visualise how cases, deaths, and reproduction rate have evolved. Identify every wave Nigeria experienced and how severe each was.

**Objective 3 — Deploy the Resilience Quadrant**  
Classify every date into one of the four quadrants. Show how Nigeria moved between quadrants over time and whether the current “quiet” period is Stable or Fragile.

**Objective 4 — Stress-Test Healthcare Capacity**  
Compare hospital/ICU occupancy against Nigeria’s known bed capacity. Quantify how close the system came to breaking point in past waves and how much buffer exists today.

**Objective 5 — Diagnose & Fix the Vaccination Stagnation**  
Explain why coverage has flat-lined. Calculate the one-dose-only gap, identify at-risk demographics, and recommend concrete actions that could lift Nigeria from Fragile to Stable.

### 6. Project Phases  

**Phase 1: Data Exploration & Cleaning**  
Load the full file, filter to Nigeria, audit quality, handle missing values, and create derived columns (e.g., vaccination gap, resilience quadrant).

**Phase 2: Epidemic & Healthcare Profiling**  
Build the epidemic curve, wave timeline, and hospital pressure visuals. Show exactly what Nigeria went through.

**Phase 3: Resilience Quadrant & Vaccination Analysis**  
Apply the quadrant framework, analyse quadrant shifts, and diagnose the vaccination stall with clear metrics.

**Phase 4: Insight Synthesis & Storytelling**  
Pull everything into a compelling narrative the Minister can present to the President.

### 7. Deliverables  

At the end of the sprint each team must submit:  

- **D1** – Clean, well-commented Python notebook/script that reproduces the Nigeria-only dataset.  
- **D2** – Epidemic curve + wave timeline dashboard (Matplotlib/Seaborn).  
- **D3** – Full dataset with new “Resilience_Quadrant” column + supporting visuals.  
- **D4** – Healthcare stress-test charts comparing occupancy vs capacity.  
- **D5** – Vaccination gap analysis + one clear recommendation slide.  
- **D6** – One-page Executive Briefing Memo in plain English (no code) for the Minister – top three insights + immediate next steps.

### 8. What Good Looks Like  

The Minister will judge your work on:  
- **Rigour** – Every claim backed by a number or chart.  
- **Clarity** – Charts that a non-technical audience can read in <10 seconds.  
- **Relevance** – Insights that directly answer “What should we do next?”  
- **Story** – Findings that build into one clear message the Minister can own.  

Top teams will have their memo printed and presented in the Ministry briefing.

**Operation HealthShield starts now.**