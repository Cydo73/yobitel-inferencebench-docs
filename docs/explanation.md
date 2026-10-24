# Explanation

**Status: Partly verified.** The Value section describes what was observed. The roofline section explains a general idea and paraphrases the product page.

## What the Value score tells you

On the leaderboard, Value is quality per dollar. Take a model's quality score and divide it by its output price per million tokens. A model with quality 70 and an output price of $0.20 scores 350.0. A model with quality 88 and a price of $2.50 scores 35.2.

A higher Value means more quality for each dollar of output. It does not reward speed, because speed is not part of the sum on the leaderboard. It also ignores input price, so a model with cheap output and expensive input can look better than it is.

## How the site describes Value

The product pages describe Value in three different ways:

* The footnote under the table says quality multiplied by tokens per dollar multiplied by latency.
* The methodology card says tokens per dollar weighted by quality and latency percentiles.
* The FAQ says the score rolls throughput, time to first token, inter token latency and cost into one number.

None of these matches the sum seen on the leaderboard. Until the site settles on one definition, use Value to build a shortlist and then compare Quality, the two prices and your own workload before you choose.

## Why throughput is a prediction

The methodology card says predicted throughput comes from a roofline model, combined with kernel level profiling and checked against published performance data. The ROI calculator also labels its benchmark source as roofline.

A roofline model asks what limits a GPU. Either it cannot do arithmetic fast enough, or it cannot read data from memory fast enough. When a model writes text one token at a time, each token needs the model weights to be read from memory, so memory bandwidth is usually the limit. The model uses the GPU's bandwidth and the model's size to estimate the best speed it can reach.

This means the throughput numbers are estimates of what is possible, not timings from a real run. Real systems usually do worse, which is one reason the calculator includes utilization and overhead settings.

## Why monthly cost is a flat number

Cost per month in the matcher and calculator assumes the hardware runs for 730 hours, a full month. It does not fall when you send fewer requests. If your traffic is small, the matcher can recommend hardware that sits mostly idle, so compare your average tokens per second with the throughput shown.
