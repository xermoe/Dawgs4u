# Author: Guillermo Garcia Jr
# Instructor: Eric Pogue
# Final Class Project - "Dawgs4u"
# See README file or Class Project Proposal for what the goal of this project is.
# In short, it is a Python matchmaker for aligning human personalities with Dog personalities.

import webbrowser

print("Hello! This is a python code that asks a series of questions to determine the best Dawg for you!")
print("Please answer each question honestly and to the best of your knowledge")

class Dog:
    def __init__(self, breed, answers, summary):
        self.breed = breed
        self.answers = answers
        self.summary = summary

dog_shelters = "https://www.pawschicago.org"
# Preassigned answers, summaries for each dog breed
dog_breeds = {
    "Labrador Retriever": {
        "answers": [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
        "summary": "Labradors are friendly, outgoing, and good-natured dogs. They are known for their loyalty and love for family."
    },
    "German Shepherd": {
        "answers": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        "summary": "German Shepherds are intelligent, loyal, and versatile dogs. They are often used as working dogs in various fields."
    },
    "Golden Retriever": {
        "answers": [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4, 3],
        "summary": "Golden Retrievers are friendly, intelligent, and devoted dogs. They are known for their gentle temperament and love for fetching."
    },
    "Bulldog": {
        "answers": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        "summary": "Bulldogs are calm, courageous, and affectionate dogs. They are known for their distinctive appearance and friendly demeanor."
    },
    "Poodle": {
        "answers": [4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4],
        "summary": "Poodles are highly intelligent, active, and elegant dogs. They are known for their hypoallergenic coat and versatility in various dog sports."
    },
    "Beagle": {
        "answers": [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
        "summary": "Beagles are friendly, curious, and energetic dogs. They are known for their keen sense of smell and love for tracking scents."
    },
    "Boxer": {
        "answers": [2, 3, 4, 5, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
        "summary": "Boxers are playful, energetic, and loyal dogs. They are known for their strong build and affectionate nature towards family members."
    },
    "Dachshund": {
        "answers": [3, 4, 2, 5, 1, 2, 1, 3, 5, 4, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4, 1, 5, 3, 2, 1],
        "summary": "Dachshunds are courageous, clever, and affectionate dogs. They are known for their distinctive long body and hunting instincts."
    },
    "Shih Tzu": {
        "answers": [4, 3, 5, 2, 1, 2, 1, 3, 4, 5, 3, 5, 2, 1, 4, 4, 2, 3, 1, 5, 3, 2, 1, 4, 5],
        "summary": "Shih Tzus are affectionate, outgoing, and charming dogs. They are known for their luxurious coat and friendly disposition."
    },
    "Siberian Husky": {
        "answers": [2, 3, 4, 5, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
        "summary": "Siberian Huskies are outgoing, mischievous, and energetic dogs. They are known for their striking appearance and love for outdoor activities."
    },
    "Pomeranian": {
        "answers": [3, 4, 2, 5, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],
        "summary": "Pomeranians are lively, intelligent, and affectionate dogs. They are known for their fluffy coat and lively personality."
    },
    "Great Dane": {
        "answers": [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],
        "summary": "Great Danes are gentle giants, known for their friendly and affectionate nature. Despite their large size, they are gentle and good-natured."
    },
    "Dalmatian": {
        "answers": [2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4],
        "summary": "Dalmatians are energetic, loyal, and intelligent dogs. They are known for their distinctive spotted coat and endurance."
    },
    "Rottweiler": {
        "answers": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3],
        "summary": "Rottweilers are strong, confident, and loyal dogs. They are known for their protective nature and make excellent guardians."
    },
    "Boston Terrier": {
        "answers": [4, 5, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
        "summary": "Boston Terriers are friendly, lively, and intelligent dogs. They are known for their tuxedo-like coat markings and affectionate nature."
    },
    "Shetland Sheepdog": {
        "answers": [5, 4, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],
        "summary": "Shetland Sheepdogs are intelligent, playful, and gentle dogs. They are known for their agility and herding instincts."
    },
    "Chihuahua": {
        "answers": [3, 2, 4, 1, 5, 2, 4, 3, 1, 5, 2, 4, 3, 1, 5, 2, 4, 3, 1, 5, 2, 4, 3, 1, 5],
        "summary": "Chihuahuas are loyal, sassy, and energetic dogs. They are known for their small size and big personality."
    },
    "Bernese Mountain Dog": {
        "answers": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3],
        "summary": "Bernese Mountain Dogs are gentle, affectionate, and good-natured dogs. They are known for their striking tri-color coat and calm demeanor."
    },
    "Australian Shepherd": {
        "answers": [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4, 3],
        "summary": "Australian Shepherds are intelligent, energetic, and loyal dogs. They are known for their herding instincts and agility."
    },
    "Doberman Pinscher": {
        "answers": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3],
        "summary": "Doberman Pinschers are loyal, alert, and fearless dogs. They are known for their sleek appearance and protective nature."
    },
}

# Create Dog objects from preassigned answers and summaries
dogs = [Dog(breed, data["answers"], data["summary"]) for breed, data in dog_breeds.items()]

# 25 listed questions
questions = [
    "I prefer to stay indoors rather than go outdoors.",
    "I enjoy relaxing more than being active.",
    "I am not fond of spending time outdoors.",
    "I am not comfortable meeting new people.",
    "I prefer being alone rather than with others.",
    "I dislike physical activity.",
    "I prefer a calm environment over a lively one.",
    "I am not vocal.",
    "I find it difficult to adapt to new situations.",
    "Loyalty is not important to me.",
    "I dislike training and learning new things.",
    "I prefer having a small social circle.",
    "I am not protective of my loved ones.",
    "I struggle to handle stress.",
    "I dislike being the center of attention.",
    "I avoid taking risks or being adventurous.",
    "I prefer sticking to a routine rather than being spontaneous.",
    "I am not stubborn.",
    "I am uncomfortable around strangers.",
    "I do not enjoy cuddling.",
    "I am not curious by nature.",
    "I do not enjoy playing.",
    "I do not have a strong prey drive.",
    "I dislike being groomed.",
    "I am not territorial."
]

def get_user_answers():
    user_answers = []
    print("Please answer the following questions on a scale of highly disagree (1) to highly agree (5):")
    for i, question in enumerate(questions, start=1):
        while True:
            try:
                answer = int(input(f"{i}. {question}: "))
                if 1 <= answer <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
        user_answers.append(answer)
    return user_answers


def calculate_similarity(user_answers, dog):
    total_difference = sum(abs(user_ans - dog_ans) for user_ans, dog_ans in zip(user_answers, dog.answers))
    return total_difference

def recommend_dog(user_answers):
    min_difference = float('inf')
    recommended_dog = None
    for dog in dogs:
        difference = calculate_similarity(user_answers, dog)
        if difference < min_difference:
            min_difference = difference
            recommended_dog = dog
    return recommended_dog

def main():
    user_answers = get_user_answers()
    recommended_dog = recommend_dog(user_answers)
    print(f"I recommend a {recommended_dog.breed} for you!")
    print("Here's a short summary of the recommended dog breed:")
    print(recommended_dog.summary)
    print("If you are looking to adopt, consider the website below")
    print(dog_shelters)
    print("Would you like to open the link in your browser? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        webbrowser.open(dog_shelters)

if __name__ == "__main__":
    main()


"""""
print("Hello! The goal of this code is to use a series of questions to determine how compatible" + 
      "\nyou are with certain dog breeds. Afterwards, you will be given a recommended dog breed" + 
      "\nand a short description. Enjoy!")

user_responses = {}

questions = [
    "I enjoy spending time outdoors.",
    "I prefer a calm and quiet environment.",
    "I like to be the center of attention.",
    "I am an active person.",
    "I enjoy training and teaching new things.",
    "I prefer a dog that requires minimal grooming.",
    "I enjoy cuddling and affection.",
    "I prefer a dog that is independent and doesn't require much attention.",
    "I am patient and tolerant.",
    "I enjoy having a routine.",
    "I prefer small dogs over large dogs.",
    "I prefer large dogs over small dogs.",
    "I enjoy going for long walks or runs.",
    "I prefer a dog that is good with children.",
    "I am willing to spend time training and socializing a dog.",
    "I prefer a dog that is protective and loyal.",
    "I prefer a dog that gets along well with other animals.",
    "I enjoy solving puzzles and challenges.",
    "I am a social person and enjoy having company around me.",
    "I am willing to adapt my lifestyle to accommodate a dog."
]

response_weights = {
    '1': -2,
    '2': -1,
    '3': 0,
    '4': 1,
    '5': 2
}

question_weights = [
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2],
    [-2, -1, 0, 1, 2]
]

# User input questions and answers
for i, question in enumerate(questions, start=1):
    response = input(f"{i}. {question} (1 - Strongly Disagree, 2 - Disagree, 3 - Neutral, 4 - Agree, 5 - Strongly Agree): ")
    # Validate user input
    while response not in response_weights:
        print("Please enter a valid response (1 - 5).")
        response = input(f"{i}. {question} (1 - Strongly Disagree, 2 - Disagree, 3 - Neutral, 4 - Agree, 5 - Strongly Agree): ")
    user_responses[f"Q{i}"] = response_weights[response]

# Base for answers on the dog breed side
breeds = {
    "Labrador Retriever": [5, 4, 3, 5, 4, 4, 4, 3, 4, 4, 3, 4, 5, 5, 4, 5, 4, 4, 4, 5],
    "Golden Retriever": [4, 4, 3, 4, 3, 3, 5, 3, 4, 4, 3, 4, 4, 5, 4, 4, 4, 3, 4, 4],
    "Poodle": [3, 4, 3, 3, 5, 5, 3, 4, 4, 4, 3, 4, 3, 4, 5, 4, 3, 4, 4, 3],
    "German Shepherd": [4, 4, 3, 5, 5, 3, 4, 5, 4, 4, 3, 4, 4, 3, 4, 5, 4, 3, 4, 4],
    "Beagle": [3, 4, 3, 4, 3, 4, 4, 3, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 4, 4],
    "Bulldog": [3, 3, 4, 3, 3, 4, 3, 3, 4, 3, 4, 3, 3, 3, 3, 4, 4, 3, 3, 4],
    "Siberian Husky": [5, 4, 3, 5, 4, 3, 3, 4, 3, 3, 3, 4, 5, 4, 4, 3, 3, 5, 3, 3],
    "Boxer": [4, 4, 3, 5, 4, 4, 3, 3, 4, 3, 4, 4, 4, 4, 4, 5, 3, 4, 3, 3],
    "Dachshund": [3, 4, 3, 3, 4, 5, 3, 3, 4, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 4],
    "Shih Tzu": [3, 3, 4, 3, 3, 4, 4, 4, 3, 4, 3, 4, 3, 5, 4, 3, 3, 3, 3, 4],
    "Rottweiler": [4, 4, 3, 5, 4, 3, 3, 4, 4, 4, 3, 4, 5, 3, 4, 5, 3, 4, 4, 4],
    "Pug": [2, 3, 5, 2, 3, 3, 5, 3, 3, 3, 3, 3, 2, 4, 3, 3, 3, 3, 3, 3],
    "Great Dane": [5, 3, 2, 4, 3, 4, 3, 3, 4, 3, 3, 4, 4, 4, 3, 5, 3, 3, 3, 5],
    "Doberman Pinscher": [5, 4, 3, 5, 5, 3, 3, 4, 4, 4, 3, 4, 5, 3, 4, 5, 3, 3, 4, 4],
    "Australian Shepherd": [5, 3, 4, 5, 5, 4, 3, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 4, 4, 5]
}

compatibility_scores = {}
for breed, scores in breeds.items():
    compatibility_scores[breed] = sum([user_responses[f"Q{i+1}"] * question_weights[i][j] for i, j in enumerate(scores)])

# Compatibility calculation
recommended_breed = max(compatibility_scores, key=compatibility_scores.get)

# Recommended breed to the user
print(f"\nBased on your personality, I recommend a {recommended_breed}.")

# Brief summary of the recommended breed
breed_summary = {
    "Labrador Retriever": "Labrador Retrievers are friendly, outgoing, and high-spirited dogs. They are known for their loyalty and intelligence.",
    "Golden Retriever": "Golden Retrievers are gentle, friendly, and intelligent dogs. They are great with families and make excellent companions.",
    "Poodle": "Poodles are highly intelligent, active, and trainable dogs. They come in various sizes and are known for their hypoallergenic coats.",
    "German Shepherd": "German Shepherds are confident, courageous, and smart dogs. They are loyal and protective companions.",
    "Beagle": "Beagles are friendly, curious, and merry dogs. They are great with children and have a strong sense of smell.",
    "Bulldog": "Bulldogs are calm, courageous, and affectionate dogs. They are known for their distinctive wrinkled face and gentle disposition.",
    "Siberian Husky": "Siberian Huskies are friendly, outgoing, and energetic dogs. They are known for their striking appearance and endurance.",
    "Boxer": "Boxers are playful, energetic, and loyal dogs. They are great with families and have a strong, muscular build.",
    "Dachshund": "Dachshunds are curious, brave, and clever dogs. They have a long body and short legs, making them distinctive and adorable.",
    "Border Collie": "Border Collies are intelligent, energetic, and highly trainable dogs. They excel in activities like agility and herding.",
    "Shih Tzu": "Shih Tzus are affectionate, outgoing, and playful dogs. They are great companions and are known for their luxurious coat.",
    "Rottweiler": "Rottweilers are confident, loyal, and protective dogs. They are great guardians and are known for their strength and endurance.",
    "Pug": "Pugs are charming, affectionate, and mischievous dogs. They are great companions and thrive on human companionship.",
    "Great Dane": "Great Danes are gentle, friendly, and affectionate giants. They are known for their calm demeanor and love for their family.",
    "Doberman Pinscher": "Doberman Pinschers are loyal, alert, and intelligent dogs. They are great protectors and excel in obedience training.",
    "Australian Shepherd": "Australian Shepherds are intelligent, versatile, and energetic dogs. They excel in various dog sports and activities."
}

print(f"\nHere's a brief summary of the {recommended_breed}:")
print(breed_summary[recommended_breed])
"""""