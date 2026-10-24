# How to share a configuration

**Status: Partly verified.** The fields and two error messages were recorded on 2026-10-23. Nothing was submitted during testing, so what happens after you submit is not documented here.

Use this guide to fill in the Share Your Configuration form.

## Before you start

* Sign in to InferenceBench.
* Know the model, GPU, number of nodes, GPUs per node and precision of the setup you want to share.

## Steps

1. Open the **Community** menu and choose the option for sharing a configuration. The form is titled **Share Your Configuration**.
2. Enter a **Title**.
3. Enter a **Description**.
4. Choose a **Model** from the list. The list is long, is not sorted alphabetically, and cannot be searched.
5. Choose a **GPU** from the list.
6. Enter the number of **Nodes** as a whole number.
7. Enter the number of **GPUs / Node**.
8. Choose a **Precision**.
9. Optionally add **Tags**, separated by commas. The placeholder example is `production, chat, budget`.
10. Select **Submit Configuration**, or **Cancel** to leave without saving.

## Fields

| Field | Type | Rules found in testing |
| --- | --- | --- |
| Title | Text | Not recorded |
| Description | Text area | Not recorded |
| Model | Dropdown | Includes text, embedding, audio and vision models |
| GPU | Dropdown | Entries such as B200 SXM, H100 SXM, A100 80GB SXM, A10G. Only the NVL72 entries say "(per GPU)" |
| Nodes | Number | Whole numbers only. Maximum 64. Minimum not recorded |
| GPUs / Node | Number | Limit not recorded |
| Precision | Dropdown | bf16 was the value used. Other options not recorded |
| Tags | Text | Comma separated |

## Error messages

The form uses messages from your browser, so the wording and look can differ between browsers and languages. The messages below were seen in Google Chrome on Windows 11.

| What you entered | Message |
| --- | --- |
| 088899 in Nodes | Value must be less than or equal to 64. |
| 1.5 in Nodes | Please enter a valid value. The two nearest valid values are 1 and 2. |

The messages do not name the field. Look for the highlighted field to see which one they refer to.

```{note}
The FAQ says community submissions include model quantization, batch size, sequence length, KV cache size and system prompt. The form tested here has none of the last three. It may be a different route from the one the FAQ describes.
```
