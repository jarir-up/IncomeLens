# 03 Source pipeline

Serves: G-1, G-2.

Fetch official sources for Germany, Italy and France on a schedule; checksum; detect change; extract requirements into the schema with citations; auto-publish above threshold; queue conflicts and low-confidence items for the maintainer. Evaluation: extraction precision and recall against hand-labelled checklists, which are the CI gate for this step.
