import random

# list of keywords
bye = ['bye', 'see', 'you', 'later', 'talk', 'soon', 'take', 'care', 'farewell', 'tomorrow', 'sounds', 'good',
       'ok', 'okay', 'k']
errorMessage = []
# weather
goodWeather = ['sunny', 'bright', 'sun', 'out', 'sky', 'blue', 'good', 'nice', 'great', 'wonderful', 'warm', 'hot']
badWeather = ['rainy', 'dark', 'rain', 'clouds', 'cloudy', 'gray', 'grey', 'bad', 'ugly', 'terrible', 'cold']
outside = ['outside', 'bike', 'biking', 'walk', 'walking', 'run', 'running', 'swim', 'swimming', 'beach', 'park']
inside = ['relax', 'relaxing', 'clean', 'cleaning', 'read', 'reading', 'tv', 'nap', 'movie', 'sleep', 'sleeping']
thanks = ['thank', 'you', 'thanks', 'I', 'will', 'for', 'sure', 'always', 'appreciate']

# cooking
cooking = ['beef', 'chicken', 'fish', 'steak', 'pork', 'pizza', 'bake', 'baking', 'fry','frying', 'fried', 'salad',
           'soup', 'noodles', 'cook', 'cooking', 'make', 'making', 'shrimp', 'lobster', 'crab', 'oysters', 'curry']
restaurant = ['restaurant', 'drive', 'driving', 'out', 'shop', 'order', 'ordering', 'walk', 'walking', 'pick', 'up']
early = ['4', '4:00', '4:15', '4:30', '4:45', '5', '5:00', '5:15', '5:30', '5:45']
sameTime = ['6', '6:00', '6:15', '6:30', '6:45', '7', '7:00', '7:15', '7:30', '7:45', '8', '8:00', '8:15', '8:30']
late = ['8:45', '9', '9:00', '9:15', '9:30', '9:45', '10', '10:00', '10:15', '10:30', '10:45', '11', '11:00']
activity = ['work', 'clean', 'chores', 'drive', 'go', 'went', 'worked', 'cleaned', 'drove', 'meet', 'met', 'traffic',
            'want', 'like', 'rather']
agreement = ['of', 'course', 'yes', 'yup', 'yeah', 'yea', 'me', 'too', 'as', 'well', 'excited', 'cant', 'wait', 'for',
             'sure']

# travel
no = ['no', 'nah', 'not', 'nope', 'none']
otherCount = ['south', 'america', 'asia', 'europe', 'africa', 'antarctica', 'australia']
sameCount = ['north', 'america']
beenLongBefore = ['canada', 'greece', 'france', 'spain']
neverBeen = ['india', 'china', 'south', 'korea', 'brazil', 'argentina', 'peru', 'italy', 'germany', 'switzerland',
             'kenya', 'morocco', 'egypt', 'australia']
beenRecently = ['japan']
plans = ['see', 'seeing', 'on', 'watch', 'watching']
agree = ['of', 'course', 'yes', 'yup', 'yeah', 'yea', 'me', 'too', 'as', 'well', 'excited', 'cant', 'wait', 'for',
         'sure']


# child responses
byeResponse = ["Talk to you later.", "Bye. Love you!", "Take care!"]
errorMessageResponse = ["I'm sorry, could you rephrase that?", "What does that mean?", "Sorry I don't understand."]
# weather
goodWeatherResponse = "That's wonderful. What are you going to do today?"
badWeatherResponse = "Darn, that's not good. So what is your plan for today?"
outsideResponse = "Sounds like fun! I hope you have a great time."
insideResponse = "Relaxing! I hope you enjoy it."
thanksResponse = "I have to go but we will talk again tomorrow."

# cooking
cookingResponse = "Sounds delicious! What time are you going to eat dinner?"
restaurantResponse = "Cool! It's nice to eat out sometimes. What are you going to make the next time you cook?"
earlyResponse = "Why do you eat so early?"
sameTimeResponse = "I eat around the same time. I can't wait to eat one of your home-cooked meals again."
lateResponse = "Why do you eat so late?"
activityResponse = "Oh I see. I guess the next time I eat with you I'll have to get used to the different timing."
agreementResponse = "Well I have to head out now but I'll talk with you again tomorrow."

# travel
noResponse = "If you could, which country would you want to visit?"
otherCountResponse = "Cool you're exploring the rest of the world! Which country will you be going to?"
sameCountResponse = "Oh nice you're staying in the same continent. But if you could visit any other continent, which" \
                    " one would it be?"
beenLongBeforeResponse = "I visited there when I was a little kid so I don't remember much. Do you have any plans yet?"
neverBeenResponse = "I've never been there before. What are you going to do while there?"
beenRecentlyResponse = "Japan was amazing! The food and service were great. Do you have any plans yet while there?"
plansResponse = "Sounds like a fun trip. You'll have to tell me about it when you get back!"
agreeResponse = "Sounds good. I have to get back to work but we will talk again tomorrow."

