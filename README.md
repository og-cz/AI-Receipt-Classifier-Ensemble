# AI Receipt Classifier Ensemble
### CNN Ensemble (ResNet34 + EfficientNet-B0 + MobileNet-V2) + XGBoost

This project implements a hybrid machine learning pipeline to detect whether a digital receipt screenshot is real (human-generated) or AI-generated. The notebook extracts features from receipts using pretrained CNNs (ResNet34, EfficientNet-B0, MobileNetV2), trains XGBoost classifiers on these features, and combines their predictions via soft-voting for robust and highly accurate classification. It achieves an impressive **97.97% accuracy** and provides comprehensive evaluation metrics and a single-image inference block for testing new receipts.

<br>
<img src="model-results-screenshot.png" alt="model-results-screenshot.png" width="75%">
<br>

## Results
The ensemble model demonstrated strong performance on the test set, outperforming individual CNN-XGBoost models. Key evaluation metrics are as follows:

-   **Accuracy**: 97.97%
-   **Precision (weighted)**: 97.98%
-   **Recall (weighted)**: 97.97%
-   **F1-Score (weighted)**: 97.97%
-   **ROC-AUC**: 0.9974
-   **5-Fold Cross-Validation (Mean)**: 89.63% (± 2.60% Std Dev)

Individual model test accuracies:
-   **ResNet34 + XGBoost**: 89.86%
-   **EfficientNet-B0 + XGBoost**: 97.97%
-   **MobileNetV2 + XGBoost**: 99.32%

Detailed evaluation plots, including Confusion Matrices, ROC Curves, and a Model Comparison Chart, have been generated and saved.

## Tech Stack

- Python, PyTorch, torchvision, PIL
- XGBoost, scikit-learn, NumPy
- Matplotlib, Seaborn for visualization
- Google Colab for GPU acceleration

## Features

- Uses pretrained CNNs (ResNet34, EfficientNet-B0, MobileNetV2) to extract image features
- Trains XGBoost classifiers on CNN features
- Combines predictions via soft-voting ensemble for robust classification
- Can test single images or batches for real vs AI receipts

### Notes

Works best on structured receipts; unseen formats may require retraining

Can be extended with data augmentation or additional feature extractors