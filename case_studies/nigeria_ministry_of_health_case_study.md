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
**Classification**
Internal / Training Use Only

### 1. Executive Summary

Nigeria has successfully navigated the worst of the COVID-19 pandemic, but the fight is not over. With a population of over 220 million, the Minister of Health needs clear, data-driven answers before the next Federal Executive Council meeting.

You have been appointed as the **Data Analyst** supporting the Ministry. Using the OWID COVID-19 global dataset, your team must focus exclusively on Nigeria and deliver actionable intelligence on three critical questions the Honourable Minister has personally asked:

1. **What’s happening right now, and how fast is it moving?**  
2. **Will the health system hold, or will it collapse?**
3. **Who needs the vaccine most urgently, and are we reaching them?**

Your analysis will directly inform national policy on vaccination revival, hospital preparedness, and early-warning systems.

### 2. About the Federal Ministry of Health  

The Ministry is shifting from emergency response to long-term resilience. After multiple waves, transmission is currently near zero, yet vaccination coverage has stalled for nearly two years. The Minister needs evidence-based recommendations that can be presented to the President and National Assembly.

### 3. Your Dataset  

You will work with the full OWID COVID-19 dataset. Filter immediately to Nigeria rows only (`iso_code == "NGA"`).

Key columns include:  
- **Time & Cases**: `date`, `new_cases`, `new_cases_smoothed`, `total_cases_per_million`, `reproduction_rate`  
- **Deaths**: `new_deaths`, `new_deaths_smoothed`, `total_deaths_per_million`  
- **Healthcare Pressure**: `hosp_patients_per_million`, `icu_patients_per_million`, `weekly_hosp_admissions_per_million`, `hospital_beds_per_thousand`  
- **Vaccination**: `people_vaccinated_per_hundred`, `people_fully_vaccinated_per_hundred`, `total_boosters_per_hundred`, `new_vaccinations_smoothed`  
- **Context**: `population`, `median_age`, `diabetes_prevalence`

**Data Quality Note**: Expect missing values, long periods of zeros, and outliers. Proper cleaning is part of the challenge.

### 4. The Nigeria COVID Resilience Framework  

To answer the Minister’s three questions, you will use a **Resilience Quadrant** model based on cases, vaccination coverage, and healthcare load:

| Quadrant       | Definition                                      | Implication for Nigeria                            |
|----------------|-------------------------------------------------|----------------------------------------------------|
| **Q1: Stable** | Low cases + High vaccination                    | Strong protection, low risk                        |
| **Q2: Fragile** | Low cases + Low vaccination                     | Quiet now, but highly vulnerable                   |
| **Q3: Recovering** | Rising cases + Improving vaccination            | Early warning — act fast                           |
| **Q4: High Risk** | High cases + Low vaccination + High hospital load | System under severe pressure                       |

Your task is to classify Nigeria’s data into these quadrants and use them to answer the Minister’s exact questions.

### 5. Engagement Objectives  

Your analysis must explicitly address the three questions posed by the Honourable Minister:

**Objective 1: What’s happening right now, and how fast is it moving?**  
Analyse current transmission levels, smoothed case trends, reproduction rate, and recent changes. Determine whether Nigeria is in a truly stable period or a deceptive lull. Identify any early warning signals.

**Objective 2: Will the health system hold, or will it collapse?**  
Evaluate hospital and ICU occupancy against Nigeria’s limited bed capacity. Assess how close the system came to collapse during past waves and calculate current buffer capacity.

**Objective 3: Who needs the vaccine most urgently, and are we reaching them?**  
Diagnose the vaccination stall, calculate coverage gaps (including one-dose-only population), link to demographic risk factors, and recommend priority groups and practical interventions.

**Supporting Objectives**
- Build a clean, reproducible Nigeria-only dataset.  
- Create compelling visualisations suitable for a Ministerial briefing.  
- Synthesise findings into clear policy recommendations.

### 6. Project Phases  

**Phase 1**: Data Exploration & Cleaning – Load, filter to Nigeria, clean, and derive key metrics (including Resilience Quadrant).  
**Phase 2**: Epidemic Curve & Wave Analysis – Visualise trends and answer “What’s happening right now?”.  
**Phase 3**: Healthcare Stress Test & Vaccination Diagnosis – Directly tackle Objectives 2 and 3.  
**Phase 4**: Insight Synthesis – Combine everything into a coherent briefing for the Minister.

### 7. Deliverables  

- **D1** Clean, commented notebook/script producing the Nigeria dataset.  
- **D2** Epidemic curve and current situation dashboard.  
- **D3** Dataset with Resilience Quadrant column + quadrant distribution visuals.  
- **D4** Healthcare capacity stress-test charts.  
- **D5** Vaccination gap analysis and priority recommendations.
- **D6** One-page Executive Briefing Memo in plain English for the Minister (addressing the three questions + top 3 insights and recommended actions).

### 8. What Good Looks Like  

- **Rigour**: Every answer backed by data and visuals.  
- **Clarity**: Charts readable by non-technical leaders in under 10 seconds.  
- **Relevance**: Direct answers to the Minister’s three questions.  
- **Impact**: Actionable recommendations that could shape national policy.