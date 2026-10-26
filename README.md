# Question Answering with Transformers

## Project Overview
This project builds an extractive Question Answering (QA) system
using a pretrained DistilBERT model fine-tuned on SQuAD.

Given a context passage and a question, the model extracts the
most likely answer span from the passage.

## Objectives
- Use a pretrained Transformer for question answering.
- Load and explore the SQuAD v1.1 dataset.
- Generate answers from context and questions.
- Evaluate predictions using Exact Match (EM) and token-level F1.
- Save predictions and visualize evaluation results.

## Dataset
- Name: SQuAD v1.1
- Training examples: 87,599
- Validation examples: 10,570
- Source: https://huggingface.co/datasets/rajpurkar/squad

## Model
- Model: distilbert/distilbert-base-cased-distilled-squad
- Framework: Hugging Face Transformers
- Task: Extractive Question Answering

## Evaluation Method
Evaluation was performed on a sample of 100 examples from
the SQuAD validation set.

- Exact Match (EM): 84.00%
- Average F1 Score: 89.00%

Exact Match measures whether the normalized predicted answer
matches a reference answer exactly. F1 measures token overlap
between the prediction and reference answer.

## Files
- question_answering_transformers.ipynb: Project notebook
- question_answering_results.csv: Predictions and evaluation scores
- question_answering_metrics.png: Evaluation metrics chart

## Limitations
The reported metrics are based on a sample of 100 validation
examples, not the full validation set. Results may vary with
the selected examples. The model may produce incorrect answers
when the context is ambiguous or does not contain the answer.

## Bonus Features

### 1. Model Comparison
Compared two extractive question-answering models on the same 100 SQuAD validation examples:

- **DistilBERT:** Exact Match 84.00%, F1 Score 89.00%
- **BERT (SQuAD 2.0):** Exact Match 79.00%, F1 Score 86.69%

DistilBERT achieved better results and faster inference in this sample. Note that the models were trained on different SQuAD versions, so the comparison is not fully controlled.

### 2. Interactive Streamlit Web App
Built and deployed a web interface where users can enter a context passage and a question to receive an extracted answer with a model confidence score.

**Features:**
- User-provided context and questions
- AI-generated answer extraction
- Model confidence display
- Input validation

Live Demo: [[Streamlit app ](https://question-answering-transformers-34vbkgbyyrbdoc97kgagsa.streamlit.app/)]

**Technologies:** Python, Hugging Face Transformers, DistilBERT, Streamlit, PyTorch.

### Web App Testing
Tested the deployed app with two questions:
- University location: Correct answer, 92.8% confidence
- University founding period: Correct answer, 73.4% confidence

## How to Run
1. Open the notebook in Google Colab.
2. Install the required libraries.
3. Load the SQuAD dataset.
4. Load the pretrained DistilBERT QA model.
5. Run the prediction and evaluation cells.

## Author
Stewart Daniel
