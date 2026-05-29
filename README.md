# VIDS Benchmarks

Compliance analysis data from the VIDS paper ([arXiv:2604.17525](https://arxiv.org/abs/2604.17525)).

Four major public medical imaging datasets scored against 22 VIDS compliance dimensions. Average compliance: 29%. Average gap: 71%.

**Analysis date:** 2026-04-21. Scoring reflects the publicly documented state of each dataset as of that date. Scores are reproducible from the published artifacts and methodology described below.

## Reproduce Table 4

```bash
python verify_scores.py
```

Output:

```
Category               LIDC-IDRI       BraTS    CheXpert         MSD    VIDS
------------------------------------------------------------------------
Structure (6)                1.5         2.0         1.5         1.5       6
Imaging (3)                  1.0         2.0         1.0         2.0       3
Annotation (4)               1.5         2.0         1.0         2.0       4
Provenance (5)               1.0         0.5         0.0         0.0       5
Quality (2)                  1.0         1.0         0.0         0.0       2
ML Readiness (2)             0.0         1.0         1.0         1.0       2
------------------------------------------------------------------------
Total (22)                   6.0         8.5         4.5         6.5      22
Percentage                   27%         39%         20%         30%    100%
```

## Datasets analyzed

The following dataset versions were assessed. Where datasets have multiple releases, the version current as of the analysis date is used. Each dataset is publicly hosted at the source registry shown.

| Dataset | Version assessed | Subjects | Modality | Source |
|---|---|---|---|---|
| LIDC-IDRI | TCIA reference release (static since 2011) | 1,018 | Chest CT | [The Cancer Imaging Archive](https://www.cancerimagingarchive.net/collection/lidc-idri/) |
| BraTS | BraTS 2024 (most recent challenge release before analysis date) | Multi-institutional | Brain MRI | [BraTS Challenge / Synapse](https://www.synapse.org/brats) |
| CheXpert | v1.0 (original Stanford ML Group release) | 224,316 radiographs / 65,240 patients | Chest X-ray | [Stanford ML Group](https://stanfordmlgroup.github.io/competitions/chexpert/) |
| MSD | Medical Segmentation Decathlon, Tasks 01–10 reference release | 2,633 | Multi-modality (CT, MR) | [medicaldecathlon.com](http://medicaldecathlon.com/) |

Subsequent dataset releases may score differently. The `verify_scores.py` script and the per-dimension data in `data/compliance_scores.json` allow re-evaluation against newer dataset versions if desired; instructions appear below under "Re-running the analysis."

## Data

`data/compliance_scores.json` contains per-dimension scores for all four datasets across 22 dimensions in six categories. Each dimension is scored as satisfied (1.0), partial (0.5), or absent (0.0). Partial scores are assigned only when information is present but not in a machine-readable or standardized form — for example, provenance described in a companion paper but absent from the dataset files themselves.

The file's `metadata` block records the analysis date, scoring scale, and methodology reference. All dimension definitions are included inline.

## Methodology

Scoring was performed against predefined criteria for each of the 22 VIDS compliance dimensions. The full methodology is documented in **Section 5.1 of the paper** ([arXiv:2604.17525](https://arxiv.org/abs/2604.17525)). All scoring decisions are reproducible from the datasets' published documentation and file structures. The 22 dimensions correspond to the information that VIDS makes structured and machine-readable.

The 22 dimensions span six categories:

- **Structure (6 dimensions)** — dataset organization, marker, registry, and documentation
- **Imaging (3)** — format standardization and per-image metadata
- **Annotation (4)** — derivative organization and annotation files
- **Provenance (5)** — annotator identity, tool, date, credentials, and QC
- **Quality (2)** — inter-annotator agreement and class distribution
- **ML Readiness (2)** — splits and leakage prevention

Each dimension definition, scoring criterion, and per-dataset scores is inline in `data/compliance_scores.json`.

## Re-running the analysis

To score a different version of these datasets, or a different dataset entirely, against the same 22 VIDS dimensions:

1. Use the dimension definitions and scoring criteria documented inline in `data/compliance_scores.json`.
2. Apply the same scoring scale (satisfied = 1.0, partial = 0.5, absent = 0.0).
3. The `verify_scores.py` script computes category totals, percentages, and the gap figure from any compatibly structured input file.

The full operational validator for VIDS-structured datasets — distinct from this benchmark scoring — is available as `pip install vids-validator` and at [github.com/vids-standard/vids-standard](https://github.com/vids-standard/vids-standard).

## Scope

This repository contains the benchmark data and reproduction script for the compliance analysis presented in the VIDS paper. It does not host the datasets themselves; each must be obtained from its original source registry under that source's terms.

Compliance percentages reflect documentation completeness against the VIDS specification at the time of analysis. They are not assessments of clinical correctness, fitness for a specific intended use, or regulatory clearance of any system trained on these datasets.

## License

Compliance analysis data: CC BY 4.0
Verification script: Apache License 2.0

## Citation

```bibtex
@misc{muthu2026vids,
  title   = {VIDS: A Verified Imaging Dataset Standard for Medical AI},
  author  = {Muthu, Joan S. and Shalen, John},
  year    = {2026},
  eprint  = {2604.17525},
  archivePrefix = {arXiv},
  primaryClass  = {eess.IV},
  url     = {https://arxiv.org/abs/2604.17525}
}
```
