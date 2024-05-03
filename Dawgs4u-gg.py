# Author: Guillermo Garcia Jr
# Instructor: Eric Pogue
# Final Class Project - "Dawgs4u"
# See README file or Class Project Proposal for what the goal of this project is.
# In short, it is a Python matchmaker for aligning human personalities with Dog personalities.

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

# User input questions and answers
for i, question in enumerate(questions, start=1):
    response = input(f"{i}. {question} (1 - Strongly Disagree, 2 - Disagree, 3 - Neutral, 4 - Agree, 5 - Strongly Agree): ")
    # Validate user input
    while response not in ['1', '2', '3', '4', '5']:
        print("Please enter a valid response (1 - 5).")
        response = input(f"{i}. {question} (1 - Strongly Disagree, 2 - Disagree, 3 - Neutral, 4 - Agree, 5 - Strongly Agree): ")
    user_responses[f"Q{i}"] = int(response)

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
    "Border Collie": [5, 4, 3, 5, 5, 4, 4, 4, 4, 4, 3, 4, 5, 5, 4, 5, 5, 4, 4, 5]
}

compatibility_scores = {}
for breed, scores in breeds.items():
    compatibility_scores[breed] = sum([user_responses[f"Q{i+1}"] * scores[i] for i in range(len(scores))])

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
    "Border Collie": "Border Collies are intelligent, energetic, and highly trainable dogs. They excel in activities like agility and herding."
}

print(f"\nHere's a brief summary of the {recommended_breed}:")
print(breed_summary[recommended_breed])
