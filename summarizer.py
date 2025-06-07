from transformers import pipeline

# Load the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_summary(text):
    summary = summarizer(text, max_length=60, min_length=30, do_sample=False)
    return summary[0]['summary_text']
