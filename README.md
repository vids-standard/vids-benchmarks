# VIDS Benchmarks

Compliance analysis data from the VIDS paper ([arXiv:2604.17525](https://arxiv.org/abs/2604.17525)).

Four major public medical imaging datasets scored against 22 VIDS compliance dimensions. Average compliance: 29%. Average gap: 71%.

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

## Data

`data/compliance_scores.json` contains per-dimension scores for all four datasets across 22 dimensions in six categories. Each dimension is scored as satisfied (1.0), partial (0.5), or absent (0.0). Partial scores are assigned only when information is present but not in a machine-readable or standardized form.

## Methodology

From Section 5.1 of the paper: scoring was performed against predefined criteria for each dimension using publicly available dataset artifacts. All scoring decisions are reproducible from the datasets' published documentation and file structures. The 22 dimensions correspond to the information that VIDS makes structured and machine-readable.

## Datasets Analyzed

| Dataset | Subjects | Modality | Source |
|---------|----------|----------|--------|
| LIDC-IDRI | 1,018 | Chest CT | [TCIA](https://www.cancerimagingarchive.net/) |
| BraTS | Multi-institutional | Brain MRI | [BraTS Challenge](https://www.synapse.org/brats) |
| CheXpert | 224,316 | Chest X-ray | [Stanford ML Group](https://stanfordmlgroup.github.io/competitions/chexpert/) |
| MSD | 2,633 | Multi-modality | [Medical Segmentation Decathlon](http://medicaldecathlon.com/) |

## License

CC BY 4.0

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
