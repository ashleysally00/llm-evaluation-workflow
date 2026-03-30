# LLM Evaluation Workflow

## Overview
This project provides a structured workflow for evaluating and comparing LLM outputs across multiple models.

The core problem it solves: **manually copy/pasting prompts into multiple models is tedious and error-prone.** By scripting prompt execution across APIs, outputs can be collected systematically and evaluated using a consistent framework.

View the full evaluation sheet: __Google Sheets__
> Note: Scoring logic and aggregation formulas are in progress.

---

## Automation

Two scripts send the same prompts to different models programmatically:

| Script | Model | Description |
|--------|-------|-------------|
| `run_prompts.py` | Gemini 2.5 Flash | Sends prompts to Gemini API |
| `run_prompts_claude.py` | Claude Haiku | Sends prompts to Anthropic API |

Both scripts:
- Read inputs from the same `Prompt Set.csv` file
- Send each prompt to the model via API
- Write model outputs to a new CSV file for evaluation

This enables side-by-side model comparison without manual copy/paste.

Note: API keys are stored securely using environment variables (`.env`) and are not included in this repository.

---

## Workflow

1. **Input** → user query
2. **Prompt** → instruction given to the model
3. **Output** → model response (collected automatically via script)
4. **Evaluation**:
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
> 50% of outputs were too verbose → indicates a need for tighter prompt constraints

---

## Why This Matters

Manual evaluation of LLM outputs is inconsistent and doesn't scale. This workflow introduces:
- **Automation** — prompt execution across multiple models without copy/paste
- **Consistency** — same prompts, same evaluation criteria across models
- **Comparability** — structured output enables side-by-side model analysis
- **Iteration** — failure patterns inform prompt improvements

---

## Example

| Input | Prompt | Output | Issue |
|-------|--------|--------|-------|
| I want to cancel | Classify intent | "The user intent is..." | Too verbose |
