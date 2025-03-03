from datasets import load_dataset

# Load English-French dataset
dataset = load_dataset("opus_books", "en-fr")

# Print a sample
print(dataset["train"][0])
