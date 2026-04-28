# OPERATION INSIGHT
## A Data Intelligence Brief
### Commissioned by the Office of the Illinois Attorney General

---

> *"Data is not just numbers. In the hands of the right people, it is the difference between a city that reacts to crime and one that prevents it."*
>
> — Office of the Illinois Attorney General

---

## BACKGROUND

The Office of the Illinois Attorney General has launched **Operation Insight** — a data-driven initiative to understand, profile, and respond to crime patterns across the city of Chicago.

For over two decades, the Chicago Police Department has recorded every reported crime incident in the city through its CLEAR (Citizen Law Enforcement Analysis and Reporting) system. That data — spanning from **2001 to the present** and containing over **7 million incident records** — has largely been used for internal police reporting.

The Attorney General's office believes this data holds far greater value. Used properly, it can:

- Reveal how crime has evolved over two decades
- Expose which communities carry a disproportionate burden of criminal activity
- Identify patterns that traditional policing has failed to act on
- Inform smarter, fairer policies on resource allocation and criminal justice reform
- Support evidence-based decisions on correctional facility capacity

To lead this effort, the Attorney General's office has engaged a data science team — **your team** — to conduct a comprehensive analysis and deliver a structured intelligence report.

This is not an academic exercise. The findings from this project will be presented to the Attorney General, shared with the Illinois State Legislature, and used to guide real policy decisions.

---

## YOUR ROLE

You are a **Data Scientist** at a public policy analytics consultancy. Your team has been contracted by the Office of the Illinois Attorney General to analyse the Chicago Crime dataset and produce an **intelligence report** that answers the key questions outlined in this brief.

You will work with real, messy, historical data. You will clean it, explore it, model it where appropriate, and translate your findings into clear, evidence-based recommendations that a non-technical audience — lawyers, legislators, policy advisors — can understand and act on.

---

## THE DATASET

| Property | Detail |
|---|---|
| **Source** | Chicago Police Department CLEAR System |
| **Coverage** | 2001 to Present |
| **Volume** | 7+ million incident records |
| **Format** | Migrated from CSV to MySQL database |
| **Key Fields** | Incident type, date, location, district, arrest outcome, domestic flag, community area |

### Key Columns Reference

| Column | Description |
|---|---|
| `id` | Unique identifier for each incident |
| `case_number` | CPD case reference number |
| `incident_date` | Date and time the incident occurred |
| `primary_type` | High-level crime category (e.g., THEFT, BATTERY, HOMICIDE) |
| `description` | Specific sub-type of the crime |
| `location_description` | Type of location where crime occurred (e.g., STREET, RESIDENCE) |
| `arrest` | Whether an arrest was made (True/False) |
| `domestic` | Whether the incident was domestic in nature (True/False) |
| `district` | Police district where the incident occurred |
| `community_area` | One of 77 defined community areas in Chicago |
| `year` | Year the incident was recorded |
| `latitude` / `longitude` | Geo-coordinates of the incident |

---

## OBJECTIVES

The Attorney General's office has defined **five core intelligence objectives** for this engagement. Your analysis must address all five.

---

### OBJECTIVE 1 — Crime Trends Over Time
**"Has Chicago become safer or more dangerous over the past two decades?"**

The office needs a clear, evidence-based answer to the most politically charged question about Chicago: is crime getting better or worse? But they want nuance, not a headline.

**Expectations:**
- Analyse year-on-year crime volume from 2001 to the most recent year in the dataset
- Identify which years saw the sharpest increases and decreases in crime, and investigate possible explanations (e.g., economic downturns, policy changes, the COVID-19 pandemic)
- Breakdown trends by broad crime category — is violent crime trending differently from property crime?
- Identify which crime types have grown the most and which have declined the most over the period

**Key questions to answer:**
- What was the peak year for crime in Chicago, and what was happening then?
- How did crime change during the COVID-19 pandemic years (2020–2021)?
- Which crime categories are on a long-term upward trend and require urgent policy attention?

---

### OBJECTIVE 2 — Geographic Crime Profiling
**"Where in Chicago is crime most concentrated, and are the same communities always bearing the burden?"**

The Attorney General is preparing a resource allocation proposal for the Illinois State Legislature. To justify where additional police resources, social services, and community investment should go, the office needs evidence of geographic crime concentration.

**Expectations:**
- Identify the top 10 most crime-affected police districts
- Identify the top 10 most crime-affected community areas
- Determine whether the same districts and community areas consistently appear at the top year after year, or whether crime hotspots shift over time
- Analyse which types of crime are most prevalent in the highest-crime areas

**Key questions to answer:**
- Which district has consistently been the most dangerous in Chicago?
- Are there any community areas that were previously high-crime but have improved significantly?
- Is crime in Chicago geographically concentrated or spread evenly across the city?

---

### OBJECTIVE 3 — Arrest Rate Analysis
**"When crimes are committed, is the system actually holding people accountable?"**

One of the most important measures of a justice system's effectiveness is not just how many crimes occur — but how many result in arrests. A low arrest rate can indicate under-resourcing of police, lack of community trust, or systemic failures in the justice pipeline.

**Expectations:**
- Calculate the overall arrest rate for all crimes across the full dataset
- Calculate arrest rates broken down by crime type — which crimes have the highest and lowest arrest rates?
- Analyse how arrest rates have changed over time — is the system getting better or worse at making arrests?
- Analyse arrest rate differences across police districts — are some districts significantly underperforming?

**Key questions to answer:**
- What percentage of reported crimes in Chicago result in an arrest?
- Which crime types are most likely to result in an arrest? Which are least likely?
- Is there a district where the arrest rate is significantly lower than the city average, and what might that suggest?
- Has the arrest rate improved or declined over the last decade?

---

### OBJECTIVE 4 — Domestic Violence Intelligence
**"What does the data tell us about the scale and nature of domestic crime in Chicago?"**

The Attorney General's office is developing a dedicated domestic violence policy framework. They need data to understand the true scale of domestic incidents, how they are distributed, and whether the justice system is responding adequately to them.

**Expectations:**
- Calculate the proportion of all incidents that are flagged as domestic
- Identify which crime types are most commonly classified as domestic incidents
- Analyse domestic incident trends over time — is domestic crime increasing or decreasing?
- Compare arrest rates for domestic vs. non-domestic incidents — does a domestic flag increase or decrease the likelihood of an arrest?
- Identify which districts have the highest rates of domestic incidents

**Key questions to answer:**
- What share of Chicago's crime is domestic in nature?
- Are domestic incidents more or less likely to result in an arrest compared to non-domestic crimes?
- Which community areas have the highest domestic incident rates?
- Has domestic crime increased or decreased since 2001?

---

### OBJECTIVE 5 — Correctional Capacity & Resource Planning
**"Based on crime trends and arrest rates, what can the data tell us about the future demand on correctional facilities and policing resources?"**

The Illinois Department of Corrections is a key partner in this initiative. They need forward-looking intelligence to plan correctional facility capacity, staffing, and rehabilitation programme investment.

**Expectations:**
- Estimate average annual arrests over the most recent five-year period
- Identify seasonal patterns in crime — which months and times of day see the highest crime volumes?
- Identify which crime types are most likely to result in incarceration (use arrest as a proxy)
- Based on the trend analysis from Objective 1, project whether arrest volumes are likely to increase or decrease in the near future
- Identify which crime types should be the focus of rehabilitation and diversion programmes based on volume and recurrence patterns

**Key questions to answer:**
- What is the average number of arrests per year in Chicago across the most recent five years?
- What time of day sees the highest crime volume, and what does this mean for shift planning?
- Which months consistently show the highest crime rates? (seasonal planning)
- Based on current trends, should the Department of Corrections plan for more or fewer inmates over the next five years?
