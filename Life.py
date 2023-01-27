import re 
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0 
    has_required_words = True
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognised_words))
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    #Response ---------------------------------------------------
    response("Hello!", ["hello", "hi", "sup", "hey", "howdy"], single_response=True)
    response("Fine", ["how", "are", "you", "doing", "whatsup" ], required_words=["how"])
    response("See you later!", ["bye", "goodbye"], single_response=True)
    response("Ok, see you later!", ["i", "gotta", "to", "go", "gonna", "got",],required_words=["go"])
    response("My name is Jack", ["what", "is", "your", "name"],required_words=["name"]) 
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    return best_match
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
while True:
    print("Bot: " + get_response(input("You: ")))