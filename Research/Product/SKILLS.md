# Product research skills

Before starting product research, read this guide and tell the user which skill you will use and why.
A skill is a reusable set of instructions for an agent.
Choose the skill based on the scope of the research question.

| Research scope | Suggested skill | When to use it |
| --- | --- | --- |
| General research | `customer-research` | Explore a large market, investigate customer needs, or develop an early idea. |
| Specific research | `market-research` | Investigate a specific app, competitor, solution, or focused topic. |

For broad questions, start with `customer-research`.
When the question narrows to a specific subject, use `market-research`.
If the work needs both skills, explain the role of each before starting.

## Sources and installation

Install the selected skill if it is unavailable.
For `customer-research`, use [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills):

```sh
npx skills add https://github.com/coreyhaines31/marketingskills --skill customer-research
```

For `market-research`, use [affaan-m/ecc](https://github.com/affaan-m/ecc):

```sh
npx skills add https://github.com/affaan-m/ecc --skill market-research
```

Read the selected skill's `SKILL.md` before applying its instructions.
In the study's `README.md`, record the research scope and the skills used.
Keep each study's notes, sources, and results in its own directory under `Research/Product/`.
