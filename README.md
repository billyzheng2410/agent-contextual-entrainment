# Agent Contextual Entrainment

An English-language research archive tracing contextual influences from token preferences to stateful tool actions. It contains the project's Colab notebooks, including developmental versions, follow-up cells, protocol diagnostics, and mechanistic interventions. Historical notebook outputs are retained.

The experiments use a controlled ordering environment with three tools: `check_stock`, `reserve_item`, and `create_order`. They distinguish local token scores, freely chosen actions, recovery after controlled query histories, attempted reservations/orders, and the final persistent order state.

## Start here

- [v7.3: execution repair and mechanism study](notebooks/agent_entrainment_v7p3_execution_mechanism_full.ipynb) is the latest complete experimental design.
- [Notebook catalog](NOTEBOOKS.md) lists every retained notebook and snapshot, including output counts.
- [Machine-readable inventory](notebook-inventory.json) records source groups and SHA-256 hashes for traceability.
- [Validation report](validation.json) records packaging checks. These checks do not constitute a new model run.

## What is preserved

This is an **English archival edition**, not a claim that the translated files were rerun. Existing output blocks, execution counts, numerical observations, and embedded image/audio/video payloads are retained. Chinese prose, comments, diagnostic messages, and textual output annotations are translated. Any detected credentials are redacted. Newly added authentication cells have no execution output.

Notebooks with different saved outputs or different source revisions remain separate. Exact duplicate files are omitted. The main `notebooks/` directory prefers saved Drive copies where available; `snapshots/` retains distinct local, prepared, or bundled versions. Some prepared notebooks never had saved outputs, and remain without outputs. A saved notebook may contain intermediate logs even when a separate result archive is complete.

Embedded code/data bundles are inspected as well as visible cells. Digest references affected by translation are updated in the English edition. Historical checkpoint identities and recorded scientific results are not represented as newly generated results. **Use a new run label or output directory when running translated code. Do not mix its checkpoints with an original run.** Original local and Drive files are not overwritten by this publication process.


Colab-specific output extension fields that are not part of the standard notebook schema are preserved under cell metadata (`english_archive_output_extensions`), indexed by output position. All 54 notebooks validate against the notebook schema; no output block is removed. Run `python tools/verify_archive.py` to check file hashes, notebook counts, and saved output counts without model calls.

## Experimental progression

| Version | Purpose |
|---|---|
| Early memory prototypes | Establish Colab compatibility, memory handling, and the agent/tool interface. |
| v1 layered / v2 behavioral | Separate contextual changes in model predictions, memory, and agent behavior. |
| v3 | Introduce conflicting factual context; include follow-up and generalization appendices. |
| v4 | Extend cities, attributes, task wording, and simple baselines. |
| v5 / v5.1 | Repair required action fields and measure incorrect reservation/order attempts as well as accepted orders. |
| v6 pilot | Transfer a fixed shared-head hypothesis to the ordering agent. |
| v6.1 / v6.2 | Align SKU scoring and develop local top-10/top-80 comparisons. These are development experiments. |
| v6.3 | Confirm behavior and controlled recovery on new scenarios. |
| v6.4 A+B | Test first-step head interventions and explore their consequences during recovery. |
| v6.5 | Independently confirm a frozen recovery comparison on 96 new scenarios. |
| v6.6 | Evaluate a strong API model with native tools, including a Responses API configuration. |
| v6.7 | Bridge the strong model to a text-based tool protocol. |
| v6.8 | Patch request/history information and follow effects through actual orders. |
| v6.9 | Explore semantic routes; a restricted supplement is also packaged with v7.0/v7.1. |
| v7.0 | Factor query order, catalog order, field labels, and the current goal, with an expanded random-head reference. |
| v7.1 | Accelerate the full design while preserving its assigned experimental grid. |
| v7.2 | Diagnose normal tool execution and protocol failures. |
| v7.3 | Repair the execution interface, retain semantic product choice, and add matched free-decoding controls. |

Older versions are included for research provenance, not endorsed as interchangeable implementations. Failed or diagnostic runs remain visible; results from different prompts, protocols, or cohorts should not be pooled as one experiment.

## Running in Colab

1. Open the desired `.ipynb` in Google Colab. Read its installation and configuration cells before running it.
2. For gated Hugging Face models, obtain model access and add `HF_TOKEN` under **Colab Secrets**, with notebook access enabled. Authentication reads the secret and calls `huggingface_hub.login(..., add_to_git_credential=False)` before model access. Never paste tokens into source cells or outputs.
3. API notebooks use `OPENAI_API_KEY` in Colab Secrets. Review the selected model, API endpoint, run stage, and spending limit before executing any paid calls. Packaging this repository does not execute those calls.
4. Select the hardware and package versions specified by that notebook. If an installation cell requests a runtime restart, restart and follow its documented resume sequence.
5. Mount your own Drive, choose a **fresh** run label/output location, run technical checks, and then execute the intended stage. Preserve the same configuration when resuming that new run.
6. Verify the exported result archive and report status. `PARTIAL`, a directory, or a filename alone is not completion. Automatic disconnection applies only where the notebook explicitly implements it after saving and verifying its archive.

Some early append-only notebooks require the parent notebook's live variables. Their filenames include `append`; they are not standalone replacements. Standalone versions embed their required source and task assets.

## Reading the results

Treat the independent **scenario/world** as the resampling unit. Multiple labels, templates, head sets, probes, and trajectories within a world are paired conditions, not additional independent samples. Development, confirmation, technical smoke tests, and diagnostic subsets have different purposes.

Keep these endpoints separate:

- A logit margin or fixed-prefix score is not an observed action.
- A forced query history measures conditional recovery, not the natural frequency of making the initial mistake.
- An attempted reservation/order is not an accepted final order.
- A locally corrected action may still be followed by an incorrect final order.
- Workflow-constrained execution and unrestricted text generation are different protocols.

### Verified v7.3 result context

The original completed v7.3 archive contains 96 formal worlds, 64,896 formal score probes, and 7,680 formal tool trajectories, plus separately identified pilot/readiness/free-decoding units. Its two co-primary contrasts use world-paired bootstrap intervals with a frozen seed and family adjustment.

The query-versus-catalog contrast favors the candidate heads relative to the 19 fixed random sets, while the label-transfer contrast is opposite the initially expected direction. This does not identify a dedicated recent-item channel. Goal-interchange patches can change final orders, including a counter-directional improvement, but are not established as a general repair. Under the repaired execution interface, the 8B Instruct model is substantially more accurate than the 8B Base model; matched free-decoding controls show that interface execution failures must be analyzed separately from semantic errors.

The earlier GPT comparisons provide a behavioral boundary under their tested protocols. They do not replicate internal head interventions, and v7.3 does not add a new GPT run.

## Reproducibility and scope

This repository packages notebooks and their saved outputs. It does not include model weights, private credentials, or every large external result ZIP. Embedded reference data already required by a notebook are retained. Access to historical Drive paths depends on the file owner's permissions; configure your own paths for a new run.

The English conversion was assisted by a locally executed [OPUS-MT Chinese-to-English model](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en), with terminology overrides and structural validation. No notebook text was submitted to an online translation API. Numerical results and binary display payloads are checked separately from translated prose.

No new blanket license is assigned by this archival upload. Third-party code, models, and datasets retain their respective licenses and access conditions. The repository owner can add a project license before broader redistribution.
