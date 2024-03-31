from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import openai
from openai import OpenAI

openai.api_key = "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"


def generate_reviews(prompt, count=1):
    reviews = []

    for i in range(count):
        review_generated = False
        while not review_generated:
            try:
                # Generate a response using the ChatCompletion method
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )

                review = response.choices[0].message['content'].strip()
                word_count = len(review.split())
                print("word count:", word_count)

                # Check if the word count is within the desired range
                if 15 <= word_count <= 70:
                    print("counted")
                    reviews.append(review)
                    review_generated = True

            except openai.OpenAIError as err:
                print(f"Encountered an error: {err}")

        # Optional: Add a slight variation to the prompt for next iteration
        prompt += " Provide another perspective."

    return reviews


prompt_text = "Write a 25 word positive review for a wireless earbud highlighting its battery life."
num_datapoints = 5
generated_reviews = generate_reviews(prompt_text, num_datapoints)

for idx, review in enumerate(generated_reviews):
    print(f"Review {idx + 1}: {review}")
