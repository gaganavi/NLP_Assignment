from datasets import load_dataset

# Load the dataset
ds = load_dataset("open-phi/textbooks", split="train")

# Print available column names
print("Available columns in dataset:", ds.column_names)
