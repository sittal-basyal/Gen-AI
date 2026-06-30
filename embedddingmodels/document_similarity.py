from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model='gemini-embedding-2',
    output_dimensionality=300
    )

documents = [
    'Artificial intelligence enables computers to learn from data and make decisions.',
    'Python is a popular programming language for AI and data science.',
    'The Earth revolves around the Sun once every year.',
    'Regular exercise improves physical health and mental well-being.',
    'Plants use photosynthesis to produce food from sunlight.'
]

query = ['Which programming language is commonly used for artificial intelligence?']

vectors_doc = embedding.embed_documents(documents)

vectors_query = embedding.embed_query(query)
 
scores = cosine_similarity([vectors_query],vectors_doc)[0]

index , score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]

print(documents[index])
print(score)