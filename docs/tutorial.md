# Tutorial: choose a GPU for your model with the Workload Matcher

**Status: Partly verified.** The steps and numbers come from one recorded run on 2026-10-23. Options that were not on screen during that run are marked.

By the end of this tutorial you will have run the Workload Matcher once, read its three recommendation cards, and know which numbers to check before you trust a result.

You need a free InferenceBench account, signed in, and about 15 minutes.

## Step 1: Open the matcher

In the top menu, open **Calculators** and choose **Workload Matcher**.

You should see a form with sections for workload, model, configuration and budget preferences.

## Step 2: Choose a workload

Select the workload type that matches your job. In the recorded run, the workload was **Training**.

```{note}
The other workload options were not recorded. Check the list on your screen. In the recorded run, the results showed inference style measures (tokens per second, time to first token, dollars per million tokens) even though Training was selected.
```

## Step 3: Choose a model

Pick a model. The recorded run used Yi 1.5 34B. The page then shows the model details:

| Detail | Value |
| --- | --- |
| Parameters | 34.4B |
| Architecture | dense |
| Context | 200,000 |
| Precision | BF16 |

## Step 4: Set the configuration

Enter these values. The page offers BF16, FP16, FP8, INT8 and INT4 as precision options.

| Setting | Value used |
| --- | --- |
| Batch size | 45 |
| Concurrent requests | 20 |
| Max sequence length | 200000 |
| Average input tokens | 512 |
| Average output tokens | 256 |
| Requests per day | 10000 |

## Step 5: Set your budget preferences

| Setting | Value used |
| --- | --- |
| Max budget per hour | $75 |
| Max budget per month | $30,000 |
| Max latency | 10,000 ms |
| Spot instance tolerance | 30% (0% means on demand only, 100% means fully spot tolerant) |

The priority weights must total 100. The recorded run used:

| Weight | Value |
| --- | --- |
| Cost | 10 |
| Performance | 45 |
| Reliability | 20 |
| Latency | 10 |
| Quality | 15 |

```{note}
The name of the button that starts the match was not recorded. Use the button at the end of the form.
```

## Step 6: Read the three cards

The top of the results shows three cards. In the recorded run:

| Card | GPU and provider | Cost per hour | Tokens per second | Score |
| --- | --- | --- | --- | --- |
| Best Overall | H100 SXM x8, Lambda Labs | $19.92 | 17529 | 94.0 |
| Best Budget | H100 SXM x4, Lambda Labs | $9.96 | 8765 | 53.5 |
| Best Performance | H100 SXM x8, Lambda Labs | $19.92 | 17529 | 94.0 |

## Step 7: Read the model quality card

The card shows an overall quality of 72 out of 100, with these parts: MMLU 76.8%, HumanEval 44.0%, GSM8K 78.0%, MT-Bench 7.9 out of 10, and HellaSwag not available.

## Step 8: Read the precision options

The page lists how each precision changes the result for this model.

| Precision | Quality | VRAM | Cost | Speed |
| --- | --- | --- | --- | --- |
| BF16 (current) | 100.0% | 69 GB | baseline | baseline |
| FP16 | 100.0% | 69 GB | baseline | baseline |
| FP8 | 99.4% | 34 GB | 50% cheaper | 1.5x faster |
| INT8 | 97.8% | 34 GB | 50% cheaper | 1.5x faster |
| INT4 (best value) | 95.4% | 17 GB | 75% cheaper | 2.5x faster |

## Step 9: Check the table before you trust it

Scroll to the table of GPUs and providers. Before you pick a row, run three checks.

1. **Compare each cost with your budget.** In the recorded run, rows 2 to 4 cost $98.32 to $98.35 per hour and about $71,774 per month. Both are above the limits entered in Step 5, yet the rows were still listed. Row 10 was under the hourly limit but cost $35,887 per month, above the monthly limit.
2. **Compare throughput with what you need.** 10,000 requests per day at 768 tokens each is about 7.7 million tokens a day, or roughly 89 tokens per second on average. The top row delivers 17,529 tokens per second. How the matcher sizes hardware is not explained, so decide whether you need that much headroom.
3. **Check how the monthly cost is built.** It equals the hourly cost multiplied by 730 hours, whatever your request volume. For example, $19.92 x 730 = $14,542.

You have now run a full match and checked it. For the meaning of every column, see the [reference](reference.md).
