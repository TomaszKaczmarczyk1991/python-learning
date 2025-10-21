max_length = 280
tweet = input("Write here...")

if len(tweet) > max_length:
    print("Your tweet is too long")
else:
    print("You posted: ", tweet)
