# 📊 Data Analyst Salary Analysis

Exploratory Data Analysis (EDA) of global **Data Analyst / Data Science** salaries. This is a practical, portfolio-ready project that walks through loading, cleaning, analyzing, and visualizing a salary dataset to answer questions that matter to anyone entering or growing in the data field.

---

## 🎯 Project Goals

This project answers real questions using data:

- How does salary scale with **experience level** (Entry → Mid → Senior)?
- Which **job titles** command the highest pay?
- Which **countries / company locations** pay the most?
- Does **remote work** correlate with higher salaries?

## 📁 Repository Structure

```
data-analyst-salary-analysis/
├── data/
│   └── data_analyst_salaries.csv   # Dataset (40 records, 9 columns)
├── analysis/
│   └── salary_analysis.py          # EDA: load, clean, analyze, visualize
├── reports/                        # Generated charts (created on run)
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
└── README.md
```

## �dataset Dataset

The dataset contains anonymized salary records with the following columns:

| Column | Description |
| --- | --- |
| `work_year` | Year the salary was recorded |
| `experience_level` | EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| `employment_type` | FT (Full-time), PT (Part-time) |
| `job_title` | Role title (Data Analyst, Data Scientist, etc.) |
| `salary_usd` | Annual salary in USD |
| `employee_residence` | Country code of the employee |
| `remote_ratio` | 0 = on-site, 50 = hybrid, 100 = fully remote |
| `company_location` | Country code of the company |
| `company_size` | S (Small), M (Medium), L (Large) |

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/SnakeEye-sudo/data-analyst-salary-analysis.git
   cd data-analyst-salary-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis:
   ```bash
   python analysis/salary_analysis.py
   ```

The script prints summary statistics and saves a chart to `reports/salary_by_experience.png`.

## 🔍 Key Insights

- **Experience pays off:** Senior roles earn substantially more than entry-level positions across every market.
- **Title matters:** ML Engineer and Data Scientist roles top the pay scale, ahead of generalist Data Analyst roles.
- **Location drives pay:** US-based roles lead, followed by Canada and the UK; the same title can pay very differently by country.
- **Remote correlation:** Fully remote roles tend to align with higher average salaries in this dataset.

## 🛠️ Tech Stack

- **Python 3** — core language
- **pandas** — data loading, cleaning, aggregation
- **matplotlib** — visualization

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> Built by **Sangam Krishna** ([@SnakeEye-sudo](https://github.com/SnakeEye-sudo)) — Web App Developer & Data Analyst.
# 📊 Data Analyst Salary Analysis

Exploratory Data Analysis (EDA) of global **Data Analyst / Data Science** salaries. This is a practical, portfolio-ready project that walks through loading, cleaning, analyzing, and visualizing a salary dataset to answer questions that matter to anyone entering or growing in the data field.

---

## 🎯 Project Goals

This project answers real questions using data:

- How does salary scale with **experience level** (Entry → Mid → Senior)?
- Which **job titles** command the highest pay?
- Which **countries / company locations** pay the most?
- Does **remote work** correlate with higher salaries?

## 📁 Repository Structure

```
data-analyst-salary-analysis/
├── data/
│   └── data_analyst_salaries.csv   # Dataset (40 records, 9 columns)
├── analysis/
│   └── salary_analysis.py          # EDA: load, clean, analyze, visualize
├── reports/                        # Generated charts (created on run)
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
└── README.md
```

## 🗂️ Dataset

The dataset contains anonymized salary records with the following columns:

| Column | Description |
| --- | --- |
| `work_year` | Year the salary was recorded |
| `experience_level` | EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| `employment_type` | FT (Full-time), PT (Part-time) |
| `job_title` | Role title (Data Analyst, Data Scientist, etc.) |
| `salary_usd` | Annual salary in USD |
| `employee_residence` | Country code of the employee |
| `remote_ratio` | 0 = on-site, 50 = hybrid, 100 = fully remote |
| `company_location` | Country code of the company |
| `company_size` | S (Small), M (Medium), L (Large) |

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/SnakeEye-sudo/data-analyst-salary-analysis.git
   cd data-analyst-salary-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis:
   ```bash
   python analysis/salary_analysis.py
   ```

The script prints summary statistics and saves a chart to `reports/salary_by_experience.png`.

## 🔍 Key Insights

- **Experience pays off:** Senior roles earn substantially more than entry-level positions across every market.
- **Title matters:** ML Engineer and Data Scientist roles top the pay scale, ahead of generalist Data Analyst roles.
- **Location drives pay:** US-based roles lead, followed by Canada and the UK; the same title can pay very differently by country.
- **Remote correlation:** Fully remote roles tend to align with higher average salaries in this dataset.

## 🛠️ Tech Stack

- **Python 3** — core language
- **pandas** — data loading, cleaning, aggregation
- **matplotlib** — visualization

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> Built by **Sangam Krishna** ([@SnakeEye-sudo](https://github.com/SnakeEye-sudo)) — Web App Developer & Data Analyst.
# data-analyst-salary-analysis
📊 Exploratory Data Analysis of global Data Analyst / Data Science salaries — pandas, data cleaning, insights &amp; visualizations. A practical, portfolio-ready DA project.
