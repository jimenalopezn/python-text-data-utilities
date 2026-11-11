# Python Data Processing & Text Analytics Utilities

## Overview
A collection of lightweight Python command-line tools designed for parsing text files, executing statistical analysis, and performing word frequency calculations with execution timing diagnostics.

---

## Key Features & Achievements
* **Engineered robust file parsing algorithms** handling invalid data entries and missing file exceptions dynamically without runtime crashes.
* **Calculated population descriptive statistics** including Mean, Median, Mode, Variance, and Standard Deviation directly from numerical text inputs.
* **Implemented text sanitation workflows** removing punctuation noise and standardizing casing for precise word frequency analytics.
* **Integrated execution time tracking** (`time` module) and automated file logging for benchmark output persistence.

---

## Technical Stack
* **Language:** Python 3.x
* **Core Libraries:** `sys`, `time` (Standard Library)
* **Capabilities:** File I/O, Exception Handling, String Sanitation, Descriptive Statistics, CLI Argument Parsing

---

## Utility Scripts

### 1. Statistical Calculator (`computeStatistics.py`)
Calculates descriptive statistics from a text file containing numerical data.

```bash
python computeStatistics.py numbers.txt
