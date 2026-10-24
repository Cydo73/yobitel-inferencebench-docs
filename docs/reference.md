# Reference

**Status: Partly verified.** Items marked Verified were checked by arithmetic against recorded screenshots or saved pages. Items marked Observed were seen but their definition was not found on the site. Items marked Derived come from recorded numbers and are not published by the site.

## Leaderboard columns

| Column | What it shows | Unit | Status |
| --- | --- | --- | --- |
| # | Position in the current view | Number | Observed |
| Model | Model name | Text | Observed |
| Params | Size of the model, for example 7.6B. Mixture of experts models show total size, for example 46.7B MoE | Billions | Observed |
| Quality | Overall quality score. Blank for some models | 0 to 100 | Observed |
| Input $/M | Price for input tokens | US dollars per million tokens | Observed |
| Output $/M | Price for output tokens | US dollars per million tokens | Observed |
| Speed | Tokens per second, according to the product page footnote | Tokens per second | Observed. Blank on every row recorded |
| Tokens/$ | Shown in millions (M). Definition not found. It is not 1 divided by the price | Millions | Observed |
| Context | Context window, for example 128K | Tokens | Observed |
| Providers | Number of providers offering the model | Count | Observed |
| Reasoning× | A multiplier such as 12.7×. Blank for most models. Meaning not documented | Multiplier | Observed |
| Value | Quality divided by output price | See below | Verified |
| Badge | Pareto Q×C×S, Most Popular, Best Value. Definitions not found | Label | Observed |
| Released | Month and year of release | Date | Observed |

Prices shown in orange italics with a tilde, for example $0.027~, are marked differently from other prices. The meaning is not documented.

### Value

Value equals Quality divided by Output $/M.

| Model | Quality | Output $/M | Value |
| --- | --- | --- | --- |
| Qwen 2.5 7B | 70 | $0.20 | 350.0 |
| Qwen 2.5 72B | 77 | $0.40 | 192.5 |
| Llama 3.1 70B | 75 | $0.79 | 94.9 |
| DeepSeek R1 | 88 | $2.50 | 35.2 |

Input price is not used. Models priced at $0.0000 show no Value.

## Workload Matcher results table

| Column | Meaning | Status |
| --- | --- | --- |
| GPU / Provider | GPU model and the cloud provider | Observed |
| Precision | Number format used, for example BF16 | Observed |
| VRAM | Total GPU memory across all GPUs in the row | Observed |
| GPUs | Number of GPUs | Observed |
| Cost/hr | Hourly cost of the whole setup | Observed |
| Cost/mo | Cost/hr multiplied by 730 hours | Verified |
| $/M tok | Cost/hr divided by millions of tokens produced per hour | Verified |
| Throughput | Tokens per second for the whole setup | Observed |
| TTFT | Time to first token. Showed 0 ms on every row recorded | Observed |
| Score | Weighted by the priority weights. Formula not published | Observed |

Worked example for $/M tok, first row of the recorded run: 17,529 tokens per second x 3,600 seconds = 63.1 million tokens per hour. $19.92 divided by 63.1 = $0.32.

## ROI calculator formulas

**Status: Derived.** These were worked out from two saved calculator pages (GTE Qwen2 7B and Llama 3.1 70B) and match within rounding. The site does not publish them.

| Result | Formula |
| --- | --- |
| GPU cost per month | GPU $/hr x GPUs per node x nodes x 730 |
| Total cost per month | GPU cost per month x (1 + overhead %) |
| Effective throughput | Raw throughput x utilization % |
| Output cap per month | Effective tokens per second x 3,600 x 730 |
| Cost per million output tokens | Total cost per month divided by millions of output tokens per month |
| Revenue per month | Output tokens x output price + input tokens x input price, with input tokens set by the Input:Output share |
| Break even price | Same as cost per million output tokens |
| Break even utilization | Cost per million output tokens divided by the sell price |

Worked example, Llama 3.1 70B page:

* GPU cost: $4.18 x 8 x 730 = $24,411, shown as $24.4K.
* Total cost with 30% overhead: $24,411 x 1.3 = $31,734, shown as $31.7K.
* Output cap: 29,200 tokens per second x 3,600 x 730 = about 76.7 billion tokens.
* Cost per million output tokens: $31,734 divided by 76,737 = $0.41.

A month is counted as 730 hours, which is 8,760 hours in a year divided by 12.
