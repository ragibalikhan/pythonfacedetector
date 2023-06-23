import openai
import csv

# Set your OpenAI API key
openai.api_key = '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'

# Set the input and output file paths
input_file = 'input.txt'
output_file = 'output_completions.csv'

# Set the OpenAI model
model = 'text-davinci-003'

# Load prompts from input file
prompts = []
with open(input_file, 'r') as f:
    prompts = f.readlines()
prompts = [prompt.strip().replace('\\n', '\n') for prompt in prompts]

# Generate completions
completions = []
for prompt in prompts:
    completion = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048
    )
    completions.append(completion.choices[0].text.strip())

# Write completions to CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Prompt', 'Completion'])
    for i in range(len(prompts)):
        writer.writerow([prompts[i], completions[i]])

# Print success message
print(f'Completions generated and saved to {output_file} successfully.')
