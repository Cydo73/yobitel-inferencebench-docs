# Audit: five things worth fixing in InferenceBench

**Status: Draft.** Written 2026-10-23 for the Yobitel team. Every finding comes from a dated screenshot or saved page recorded in the [verification log](verification_log.md). I have tried to keep each fix small and specific.

InferenceBench is useful, and the cost columns are consistent with each other. The product pages promise that every number is traceable to a published configuration, so these gaps matter. Here is what I found while writing the documentation.

## 1. Value is described four ways

* The footnote under the product page table says quality x tokens/$ x latency.
* The methodology card says tokens per dollar weighted by quality and latency percentiles.
* The FAQ says throughput, time to first token and inter token latency are rolled into Value.
* The leaderboard computes quality divided by output $/M. For example, Qwen 2.5 7B is 70 divided by $0.20, which is 350.0. DeepSeek R1 is 88 divided by $2.50, which is 35.2. Speed is blank on every row I checked.

**Suggested fix:** publish one formula with a worked example, and link to it from the footnote. The methodology card says weighting formulas are published in the open, but I could not find them.

## 2. Pricing freshness does not match

The methodology card says pricing is re pulled every 6 hours. The data freshness line on the leaderboard says pricing is 5 months old, latency is 5 months old and quality benchmarks are 2 years old.

**Suggested fix:** reconcile the two statements, or explain what each one measures.

## 3. The ROI calculator gives two answers

* For GTE Qwen2 7B, the recommendation is one A10G at about $285 a month and $0.51 per million tokens. The economics panel below shows $31.7K a month and $0.05 per million, using a B200 NVL (pair) at $4.18 an hour.
* Profit per million ignores input tokens, while monthly profit includes them. On the Llama 3.1 70B page, $59.1K profit divided by 76.7 billion output tokens is about $0.77 per million, but the page shows $0.38.
* Break even utilization is 281.5% on the GTE Qwen2 7B page, which cannot happen, and nothing explains it.
* The GPU card says "Cheapest at $10.50/hr" and "No cloud providers found" at the same time.

**Suggested fix:** show which GPU each panel uses, count input revenue in profit per million and break even figures, and explain what a value above 100% means.

## 4. The Workload Matcher lists results outside the limits you set

With a limit of $75 per hour and $30,000 per month, rows 2 to 4 showed $98.32 to $98.35 per hour and about $71,774 per month. Time to first token showed 0 ms on every row, despite a 10,000 ms limit. The top pick delivers 17,529 tokens per second for a workload that averages about 89.

**Suggested fix:** filter or flag rows that break the limits, show real time to first token or hide the column, and say how hardware is sized.

## 5. The submission form and the FAQ disagree, and errors do not help

The FAQ says submissions include batch size, sequence length, KV cache size and system prompt. The Share Your Configuration form has Title, Description, Model, GPU, Nodes, GPUs / Node, Precision and Tags. I may have found a different route from the one the FAQ describes.

The form shows browser default errors such as "Value must be less than or equal to 64." They do not name the field, and the limit is not shown beforehand. The information icons next to some columns failed to load their values when I clicked them.

**Suggested fix:** show limits beside each field, write custom error messages that name the field, and make the form match the FAQ or the other way round.

## What I built

I wrote and tested a documentation set that covers the Workload Matcher, the form, the leaderboard columns and the ideas behind Value and throughput. Every page states how far it was verified.
