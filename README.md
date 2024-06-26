# Scope 3 Emissions Estimation using NLP

## Overview

Large corporations are under significant pressure to align with the Sustainable Development Goals (SDGs), in particular goal 13, which targets the mitigation of climate change and its effects. A critical aspect of this endeavour involves reducing Scope 3 emissions within enterprises, as these emissions contribute to over ninety percent of the emission inventory.

## Challenges

- **Tracking Scope 3 Emissions**: Accurately tracking Scope 3 emissions presents difficulties due to the need to gather data from numerous suppliers throughout the supply chain.
- **Carbon Attribution**: Estimating carbon percentage in products is vital in understanding their impact on the environment and implementing measures to mitigate it.
- **Data and Domain Knowledge**: Achieving precise carbon attribution on a large scale demands both detailed supply chain data and domain knowledge.

## Proposed Framework

We propose an innovative framework that utilizes specialized natural language processing (NLP) models tailored to the domain to calculate Scope 3 emissions. This framework uses financial transactions to track purchased services and goods. 

### Key Components

- **Zero-shot Learning Tasks**: Provide a nuanced understanding of SBERT's capabilities in different prediction scenarios.
  - **Emission Type Identification**: High accuracy, precision, recall, and F1-scores.
  - **Supply Chain Stage Identification**: Strong results.
  - **Impact Assessment** and **Geographical Region Identification**: Slightly lower scores, suggesting areas for model improvement.

- **Supervised Learning Tasks**: Highlight the effectiveness of various algorithms in emission estimation.
  - **Gradient Boosting Regression**: Excels in Emission Quantity Prediction.
  - **Logistic Regression** and **Support Vector Machines**: Perform well in Emission Type Identification.
  - **Binary Relevance** and **Label Powerset methods**: Show potential in Impact Assessment.
  - **Conditional Random Fields** and **Hidden Markov Models**: Effective for Supply Chain Stage Identification.

## Comparative Analysis of BERT Fine-Tuning

### Methods Evaluated

- **Multi-Task Learning (MTL)**
  - **Performance**: Most effective method.
  - **Metrics**: Lowest errors and highest R-squared coefficient.
  
- **Traditional Supervised Fine-Tuning (TSFT)**
  - **Performance**: Competitive results.
  - **Metrics**: Slightly less accurate than MTL.
  
- **Domain-Adversarial Training (DAT)**
  - **Performance**: Competitive results.
  - **Metrics**: Slightly less accurate than MTL.
  
- **Transfer Learning with Pre-trained Models (TLPM)**
  - **Performance**: Less effective.
  - **Inference**: Direct fine-tuning may not be as beneficial as multi-task learning or domain-adversarial training for emission estimation tasks.

## Insights and Recommendations

- **Leveraging Strengths**: By leveraging the strengths of each approach and addressing their limitations, stakeholders can develop more accurate and robust models for environmental impact assessment and sustainability planning.
- **Model Improvement**: Continuous evaluation and refinement of models are necessary to enhance their predictive accuracy and explanatory power.

This comparative analysis delivers key insights into the performance of different methodologies for supply chain emission estimation, providing a foundation for developing effective and sustainable solutions.
