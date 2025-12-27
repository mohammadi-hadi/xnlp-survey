# Explainability in Practice: A Survey of Explainable NLP

[![Paper](https://img.shields.io/badge/Paper-Journal%20of%20Information%20Science-blue)](paper/XNLP_Survey.pdf)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Data](https://img.shields.io/badge/Data-Available-green)](#structured-data)

This repository contains supplementary materials for the survey paper **"Explainability in Practice: A Survey of Explainable NLP Across Various Domains"** published in the *Journal of Information Science*.

## Overview

As Natural Language Processing (NLP) models grow more complex and are deployed in high-stakes domains, the need for **Explainable NLP (XNLP)** has become critical. This survey provides a comprehensive analysis of explainability techniques across diverse application domains, examining how different fields conceptualize, implement, and evaluate explanations.

### Key Contributions

- **Cross-Domain Analysis**: First systematic comparison of XNLP requirements across seven major application domains
- **Technique Taxonomy**: Hierarchical classification of explanation methods from traditional ML to LLMs
- **Evaluation Framework**: Domain-specific evaluation requirements and standardized metrics
- **Practical Insights**: Empirical evidence on explanation effectiveness in real-world deployments

## Repository Structure

```
xnlp-survey-package/
├── README.md                           # This file
├── LICENSE                             # CC BY 4.0 License
├── CITATION.cff                        # Citation metadata
│
├── paper/
│   ├── XNLP_Survey.pdf                 # Full survey paper
│   └── bibtex/
│       └── references.bib              # Complete bibliography (200+ references)
│
├── data/
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

## Citation

If you use this survey or its resources in your research, please cite:

```bibtex
@article{xnlp_survey_2025,
  title={Explainability in Practice: A Survey of Explainable {NLP} Across Various Domains},
  author={[Authors]},
  journal={Journal of Information Science},
  year={2025},
  publisher={SAGE Publications}
}
```

See [`CITATION.cff`](CITATION.cff) for machine-readable citation metadata.

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

- **Paper**: © Authors, published by SAGE Publications
- **Supplementary Materials**: CC BY 4.0

## Contributing

We welcome contributions to improve and extend these resources:

1. **Corrections**: Open an issue for any errors in the data
2. **Updates**: Submit PRs to add new papers, tools, or resources
3. **Extensions**: Suggest additional domains or techniques to cover

## Contact

For questions about the survey or this repository, please:
- Open a [GitHub Issue](../../issues)
- Contact the corresponding author (see paper for details)

---

**Last Updated**: 2025
