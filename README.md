# LLM Evaluation Workflow

## Overview
This project demonstrates a structured workflow for evaluating LLM outputs.

The goal is to move from subjective judgment to repeatable, measurable evaluation.

View the full evaluation sheet (including formulas and scoring logic):  
[Google Sheets](https://docs.google.com/spreadsheets/d/1CdNGnFg9NNCkMsi3x-WZ0bDqAIAitCfNEJnj1avaS84/edit?usp=sharing)

---

## Automation

This workflow includes a simple script (`run_eval.py`) that automates prompt execution using the Gemini API.

The script:
- Reads inputs from a structured CSV file
- Sends prompts to the model programmatically
- Writes model outputs back to a new CSV file for evaluation

This removes the need for manual copy/paste and enables batch evaluation at scale.

Note: API keys are stored securely using environment variables (`.env`) and are not included in this repository.

---

## Workflow

1. Input → user query  
2. Prompt → instruction given to the model  
3. Output → model response  
4. Evaluation:  
   - Assign PASS / FAIL  
   - Tag issues using predefined categories  

---

## Issue Taxonomy

- Too verbose  
- Wrong classification  
- Format incorrect  
- Missing information  
- Hallucination  

---

## Metrics

Outputs are analyzed using simple aggregation:

- Count of each issue type  
- Percentage of total failures  

Example insight:  
- 50% of outputs were too verbose → indicates a need for tighter prompt constraints  

---

## Why this matters

This approach enables:

- Consistent evaluation across outputs  
- Identification of dominant failure patterns  
- Data-driven prompt iteration  

---

## Example

| Input | Prompt | Output | Issue |
|------|--------|--------|-------|
| I want to cancel | Classify intent | "The user intent is..." | Too verbose |

---

## Takeaway

Instead of evaluating outputs ad hoc, this workflow introduces structure, repeatability, and basic quantitative analysis.
