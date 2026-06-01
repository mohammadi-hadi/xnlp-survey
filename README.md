<div align="center">

# Survey of Explainable NLP Applications

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20091832.svg)](https://doi.org/10.5281/zenodo.20091832)
[![arXiv](https://img.shields.io/badge/arXiv-2502.00837-b31b1b.svg)](https://arxiv.org/abs/2502.00837)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

*A cross-domain survey of explainable NLP — from traditional ML to large language models.*

</div>

## Paper

|                  |                                                                          |
| ---------------- | ------------------------------------------------------------------------ |
| **Title**        | Explainability in Practice: A Survey of Explainable NLP Across Various Domains |
| **Authors**      | Hadi Mohammadi, Robert A. Bagheri, Anastasia Giachanou, Daniel L. Oberski |
| **Affiliation**  | Utrecht University, The Netherlands |
| **Venue**        | arXiv preprint |
| **arXiv**        | [2502.00837](https://arxiv.org/abs/2502.00837) |
| **Code archive** | [10.5281/zenodo.20091832](https://doi.org/10.5281/zenodo.20091832) (this repository, snapshot v1.0-thesis) |

> This repository accompanies **Chapter 2** of the PhD thesis
> *Let Me Explain! Explainable NLP for Understanding Large Language Models* (Hadi Mohammadi, Utrecht University, 2026).

## Abstract

Natural Language Processing (NLP) has become a cornerstone in many critical sectors, including healthcare, finance, and customer relationship management. The black-box nature of advanced NLP models has created an urgent need for transparency and explainability. This survey provides a comprehensive review of explainable NLP (XNLP) with a focus on practical deployment across domain-specific contexts, examining how explanations can be designed to meet the unique demands of healthcare, finance, customer relationship management, systematic reviews, conversational AI, and beyond. The survey concludes by identifying gaps and future research directions.

## Citation

If you use this code or data, please cite **both** the paper and this code archive:

```bibtex
@article{mohammadi2025xnlp,
  title         = {Explainability in Practice: A Survey of Explainable NLP Across Various Domains},
  author        = {Mohammadi, Hadi and Bagheri, Robert A. and Giachanou, Anastasia and Oberski, Daniel L.},
  year          = {2025},
  journal       = {arXiv preprint},
  eprint        = {2502.00837},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2502.00837}
}

@software{mohammadi_xnlp_survey_2026,
  author    = {Mohammadi, Hadi and Bagheri, Robert A. and Giachanou, Anastasia and Oberski, Daniel L.},
  title     = {Survey of Explainable NLP Applications},
  year      = {2026},
  publisher = {Zenodo},
  version   = {v1.0-thesis},
  doi       = {10.5281/zenodo.20091832},
  url       = {https://doi.org/10.5281/zenodo.20091832}
}
```

---

## Overview

As Natural Language Processing (NLP) models grow more complex and are deployed in high-stakes domains, the need for **Explainable NLP (XNLP)** has become critical. This survey provides a comprehensive analysis of explainability techniques across diverse application domains, examining how different fields conceptualize, implement, and evaluate explanations.

### Key Contributions

- **Cross-Domain Analysis**: First systematic comparison of XNLP requirements across seven major application domains
- **Technique Taxonomy**: Hierarchical classification of explanation methods from traditional ML to LLMs
- **Evaluation Framework**: Domain-specific evaluation requirements and standardized metrics
- **Practical Insights**: Empirical evidence on explanation effectiveness in real-world deployments

## Repository Structure

```
xnlp-survey/
├── README.md                           # This file
├── LICENSE                             # CC BY 4.0 License
├── CITATION.cff                        # Citation metadata
│
│
├── code/
│   ├── create_figures.py               # Generates Fig. 1 (taxonomy) and Fig. 2 (decision tree)
│   └── requirements.txt                # Python dependencies (matplotlib, numpy)
│
├── data/
│   ├── ethics_reference.md             # Methodology and ethics statement
│   │
│   ├── tables/                         # Structured data from paper tables
│   │   ├── cross_domain_comparison.csv
│   │   ├── domain_evaluation_requirements.csv
│   │   ├── xnlp_applications_overview.csv
│   │   └── evaluation_metrics.csv
│   │
│   ├── taxonomy/
│   │   └── xnlp_taxonomy.json          # Hierarchical XNLP taxonomy
│   │
│   └── resources/
│       └── tools_and_datasets.json     # Links to tools and datasets
│
├── docs/                               # Project website
│   ├── index.html
│   ├── css/
│   └── js/
│
└── .github/
    └── ISSUE_TEMPLATE.md
```

## Structured Data

### Cross-Domain Comparison

The survey identifies distinct explainability requirements across seven domains:

| Domain | Primary Need | Key Methods | Unique Challenges |
|--------|--------------|-------------|-------------------|
| Medicine | Clinical actionability | RETAIN, SHAP, LIME | HIPAA/GDPR, clinical workflow integration |
| Finance | Regulatory compliance | SHAP, attention heatmaps | Adversarial gaming, real-time constraints |
| CRM | User satisfaction | Attention, rationale generation | Multi-language, personalization trade-offs |
| HR | Fair hiring | Counterfactual explanations | Legal liability, bias mitigation |
| Social Science | Content moderation | SHAP, LIME | Cultural sensitivity, annotation bias |
| Systematic Reviews | Reproducibility | Rule-based extraction | Heterogeneous corpora |
| Chatbots | User trust | Dialogue explanations | Real-time generation |

### Taxonomy

The complete XNLP taxonomy is available in [`data/taxonomy/xnlp_taxonomy.json`](data/taxonomy/xnlp_taxonomy.json), covering:

- **Modeling Techniques**: Traditional NLP → Embeddings → Transformers → LLMs
- **Explanation Methods**: Post-hoc (LIME, SHAP) vs. Intrinsic (attention, rationales)
- **Evaluation Framework**: Quantitative metrics, human-centered evaluation, benchmarks

### Tools and Resources

See [`data/resources/tools_and_datasets.json`](data/resources/tools_and_datasets.json) for curated links to:

- Explanation libraries (LIME, SHAP, Captum, TransformerLens)
- Systematic review tools (ASReview, RobotReviewer)
- Benchmarks (HateXplain, ERASER, e-SNLI)
- Pre-trained model hubs

## Key Findings

### 1. Domain-Specific Requirements
Explainability is not one-size-fits-all. Medical applications prioritize clinical validity and patient safety, while financial applications emphasize regulatory compliance and adversarial robustness.

### 2. Evaluation Gap
A disconnect exists between technical metrics (fidelity, faithfulness) and practical utility. Domain-specific validation protocols are essential.

### 3. LLM Challenges
Large language models present unique interpretability challenges:
- **Mechanistic interpretability** is advancing but remains incomplete
- **Chain-of-thought** explanations may not faithfully reflect internal reasoning
- **Explainability-by-design** approaches show promise for future development

### 4. Quantitative Evidence
Empirical studies demonstrate measurable benefits of explainability:
- RETAIN achieves AUC 0.8717 in heart failure prediction with full interpretability
- Active learning with explanations achieves 88.5% work saved in systematic reviews
- User trust in chatbots correlates strongly with perceived explanation quality

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

- **Paper**: © Authors (arXiv preprint)
- **Supplementary Materials**: CC BY 4.0

## Contributing

We welcome contributions to improve and extend these resources:

1. **Corrections**: Open an issue for any errors in the data
2. **Updates**: Submit PRs to add new papers, tools, or resources
3. **Extensions**: Suggest additional domains or techniques to cover

## Contact

- **Hadi Mohammadi** — Utrecht University
- Website: [mohammadi.cv](https://mohammadi.cv)
