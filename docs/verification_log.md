# Verification log: InferenceBench

Tester: Mumpe Cydrone
Date started: 2026-10-23
Browser and device: Google Chrome on a Windows 11 laptop (8th generation processor)
Signed in: yes
Site tested: inferencebench.io

## Procedure 1: Workload Matcher

**Goal:** get a GPU recommendation for a 34B model and note how the results behave.
**Started at:** Calculators menu, Workload Matcher.
**Screenshots:** Screenshot_2026-10-23_135649.png and Screenshot_2026-10-23_135713.png.

Steps taken:

1. Created an account and signed in.
2. Opened Calculators, then Workload Matcher.
3. Selected the Training workload.
4. Selected the model. Details shown: 34.4B parameters, dense, context 200,000, BF16.
5. Set the configuration: batch size 45, concurrent requests 20, max sequence length 200000, average input tokens 512, average output tokens 256, requests per day 10000. The page offered BF16, FP16, FP8, INT8 and INT4.
6. Set the budget: $75 per hour, $30,000 per month, max latency 10,000 ms, spot tolerance 30%. Weights: cost 10, performance 45, reliability 20, latency 10, quality 15.

Result:

* Best Overall: H100 SXM x8, Lambda Labs, $19.92 per hour, 17529 tok/s, score 94.0.
* Best Budget: H100 SXM x4, Lambda Labs, $9.96 per hour, 8765 tok/s, score 53.5.
* Best Performance: same as Best Overall.
* Model quality 72 out of 100 (MMLU 76.8, HumanEval 44.0, GSM8K 78.0, MT-Bench 7.9, HellaSwag not available).

Matched what I expected: partly. Rows 2 to 4 and row 10 broke the budget limits. TTFT showed 0 ms on every row.
To fill in: the exact button used to run the matcher, and which precisions were ticked.
**Status:** Verified for the steps and numbers recorded. Behaviour questions are open.

## Procedure 2: ROI calculator

**Goal:** check whether the calculator's numbers add up.
**Started at:** Calculators menu, ROI calculator (page title "Calculator, GPU Inference ROI").
**Saved pages:** Calculator___GPU_Inference_ROI___InferenceBench.html (GTE Qwen2 7B) and Calculator___GPU_Inference_ROI___InferenceBench2.html (Llama 3.1 70B).

Result: GPU cost, the 30% overhead total and the monthly output cap all matched their formulas. Several other figures did not add up, listed in the audit.
To fill in: whether Apply This Configuration was clicked, and the price entered.
**Status:** Partly verified.

## Procedure 3: Share Your Configuration form

**Goal:** find which fields the form has and how it handles invalid input.
**Started at:** Community menu, Share Your Configuration.
**Screenshots:** 141928, 142728, 142748 and 142755 (2026-10-23).

Steps taken:

1. Filled in test values (Model Qwen 2.5 14B, GPU B200 SXM, bf16).
2. Entered 088899 in Nodes: "Value must be less than or equal to 64."
3. Entered 1.5 in Nodes: "Please enter a valid value. The two nearest valid values are 1 and 2."
4. Opened the Model and GPU dropdowns and recorded the visible options.

Not yet done: the minimum for Nodes, the limit for GPUs / Node, an empty Title, the Precision options, the rest of the dropdown lists, and whether submissions are public.
Nothing was submitted.
**Status:** Partly verified.

## Procedure 4: Definitions and tooltips

**Goal:** find the site's own definitions for the columns and badges.
**Screenshots:** 144954, 145001, 145035 and 145041 (2026-10-23, 14:49 to 14:50), showing the Methodology and FAQ sections of the InferenceBench page on yobitel.com.

Result: the information icons next to the column names failed to load their values when clicked. Still to recheck in a second browser. The Methodology and FAQ sections were captured instead. A set of definitions pasted from an AI generated overview was rejected because it is not the site's own wording and conflicts with the leaderboard.
**Status:** Partly verified.
