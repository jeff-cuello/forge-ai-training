---
name: review-training-change
description: Prepare review evidence for a completed change in the synthetic routing lab. Use when asked to summarize its diff and verification results.
---

# Review a training change

Read the requirement and inspect the change. Record the changed files, the behavior corrected, commands run, actual results, and remaining uncertainty. Run the checks when the environment permits them. If a check cannot run, record that limit rather than reporting a pass.

Do not edit the implementation, publish a pull request, or approve the work. Refer a request for those actions to the human's task instructions. Return a short review record. Link each requirement to the results that show whether it was met.

For the helper exercise, inspect `summarize_checks.py` in this directory. Test it with known passing and failing records before using its counts. The helper counts the results you give it. It does not prove that anyone ran a test or that the tests cover every requirement.