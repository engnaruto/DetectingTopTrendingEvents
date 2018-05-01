import json

def check_keys(tweet_obj):
	keys = ['text', 'id', 'timestamp_ms', 'created_at']
	for key in keys:
		if key not in tweet_obj:
			return False

	return True

if __name__ == '__main__':
	# with open('data_encoded.json', 'r') as data_file:
	# 	tweets = []
	# 	corrupted_num = 0
	# 	keys_corrupt = 0
	# 	for tweet in data_file:
	# 		try:
	# 			tweet_obj = json.loads(tweet)
	# 			if (check_keys(tweet_obj)): 
	# 				tweets.append(tweet_obj)
	# 			else:
	# 				keys_corrupt += 1

	# 		except json.decoder.JSONDecodeError as e:
	# 			corrupted_num += 1
	# 			pass
		
	# 	with open('data_corrected.json', 'w') as data_correct:
	# 		json.dump(tweets, data_correct, ensure_ascii=False)

	# 	print("Tweet with less keys = ", keys_corrupt)
	# 	print("Tweet decode corrupt = ", corrupted_num)
	
	with open('data_corrected.json', 'r') as data_correct:
		data_obj = json.load(data_correct)
		print(len(data_obj))
		for tweet in data_obj:
			for key in tweet.keys():
				print(key, " => ", tweet[key])

			print("--------------------------")