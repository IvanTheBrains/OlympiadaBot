import telebot
import requests


headers = {"user-agent":"Mozilla/5.0 (Linux; Android 7.0; BLN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36","content-type":"application/json", "accept":"application/json"}
url = "https://online.olimpiada.ru/smt-portal/register/login"

token = "YOUR TOKEN"
bot = telebot.TeleBot(token)


print("[STATUS] Running...")


@bot.message_handler(commands=['start', 'help'])
def reply_to_commands(message):
	if message.from_user.first_name:
		user = message.from_user.first_name
	elif message.from_user.username:
		user = message.from_user.username
	else:
		user = "User"

	if message.text == "/start":
		msg = f'Hello <b>{user}</b>.' + '\n' + 'Send me your registration code to get the results of the Olympiada.'
		bot.send_message(message.chat.id, msg, parse_mode="HTML")
	if message.text == "/help":
		link = '<a href="https://online.olimpiada.ru">online.olimpiada</a>'
		msg = f'Dear {user},\nYou should have received the code for this {link} website.'
		bot.send_message(message.chat.id, msg, parse_mode="HTML")


@bot.message_handler(func=lambda message: ("sch" in message.text) == True)
def send_result(message):
	token = message.text
	payload = {"token":token}
	getID = requests.post(url=url, json=payload, headers=headers)
	try:
		contest_id = getID.json()['canPassTest']['liContestId']
		session_id = getID.json()['canPassTest']['liSessionId']
		get_json = f'https://online.olimpiada.ru/smt-portal/test?regQuizId={contest_id}&sid={session_id}'

		info = requests.get(url=get_json, headers=headers)

		title = info.json()['tsContest']['title']
		username = info.json()['tsUser']['userName']
		login_key = info.json()['tsUser']['login']
	except:
		warning_msg = "Invalid key. Please try again!"
		bot.send_message(message.chat.id, warning_msg)
	try:
		user_score = info.json()['tsInfo']['contents'][1]['contents']['userScore']
		max_score = info.json()['tsInfo']['contents'][0]['contents']['contestMaxScore']

		title = '📛 ' + '<u>' + title + '</u>'
		name = '👨‍🎓 Username: ' + username
		login_key = '🆔 Your key: ' + login_key
		score = '❗️ Your score: ' + str(user_score)
		max_score = '🏆 Maximum score: ' + str(max_score)

		full_info = [name, login_key, score, max_score]
		result_msg = title

		for each in full_info:
			result_msg += ('\n' + each)

		bot.send_message(message.chat.id, result_msg, parse_mode="HTML")
	except NameError:
		pass


@bot.message_handler(content_types = ['text'])
def edit_message(message):
	msg = 'That is not a key! Type /help for help.'
	bot.send_message(message.chat.id, msg, parse_mode="HTML")


bot.polling()
