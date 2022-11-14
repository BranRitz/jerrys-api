from survey_api import models
# beg_people = ["sister", "brother", "grandmother", "grandfather", "mother", "father", "daughter", "son", "married", "baby", "wife", "husband", "boyfriend", "girlfriend", "fiance", "birthday", "party", "holiday"]
# adv_people = ["They are married.", "She is pregnant.", "I have 6 children.", "I love my wife.", "My birthday is July 7th.", "I am a father.", "I have 2 sisters.", "I have 1 brother.", "When is the party?", "Happy birthday."]
# beg_food = ["knife", "fork", "spoon", "plate", "hungry", "empty", "water", "thirsty", "more", "check", "chicken", "steak", "greens", "tea", "coffee", "salt", "hot", "server"]
# adv_food = ["I'd like to order.", "I am hungry.", "I am thirsty.", "I am full.", "I am done.", "Can I have more water?", "I'd like coffee.", "I do not like this tea.", "I'd like fried chicken.", "This needs salt.", "Can I have a knife?", "I need a spoon."]
# beg_outdoors = ["road", "tree", "squirrel", "bush", "plant", "rain", "sun", "cloud", "flood", "house", "car", "dog", "cat", "walk", "run", "weather", "hot", "humid", "grass", "flower"]
# adv_outdoors = ["You drive on a road.", "Look at the squirrel.", "He has a dog.", "She has a cat.", "Let's get in the car.", "The sun is out.", "Is it going to rain?", "It is cloudy.", "It is humid.", "The grass needs water.", "The tree looks big."]
# beg_me = ["yes", "no", "dad", "hurt", "arm", "leg", "head", "arm", "teeth", "pain", "bathroom", "knee", "foot", "hand", "face", "heart", "ear", "mind", "happy", "sad", "angry", "excited", "frustrated"]
# adv_me = ["I am a dad.", "My arm is sore.", "My teeth hurt.", "My hand is in pain.", "I am going to the bathroom.", "My ear hurts.", "I feel frustrated.", "That makes me happy.", "I feel sad.", "I am excited.", "It's in my hand.", "I don't know."]
#
# models.WordLists.objects.create(category="people", level="beg", word_list=beg_people)
# models.WordLists.objects.create(category="food", level="beg", word_list=beg_food)
# models.WordLists.objects.create(category="outdoors", level="beg", word_list=beg_outdoors)
# models.WordLists.objects.create(category="me", level="beg", word_list=beg_me)
# models.WordLists.objects.create(category="people", level="adv", word_list=adv_people)
# models.WordLists.objects.create(category="food", level="adv", word_list=adv_food)
# models.WordLists.objects.create(category="outdoors", level="adv", word_list=adv_outdoors)
# models.WordLists.objects.create(category="me", level="adv", word_list=adv_me)
#

course = models.Courses.objects.create(professor="newacct", course_name="CDX1311", status="active", students=["bkuritz", "cdavis"])
models.Surveys.objects.create(owner="newacct", status="open", name="fruits", questions=["Do you like apples?", "Do you like bananas?"], course=course)
models.Surveys.objects.create(owner="newacct", status="open", name="pets", questions=["Do you like dogs?", "Do you like cats?"], course=course)
models.Surveys.objects.create(owner="newacct", status="closed", name="sports", questions=["Do you like football?", "Do you like baseball?"], course=course)

