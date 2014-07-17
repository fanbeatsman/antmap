import random
import urllib, urllib2
import json


def generate_random_steamid():
	response = []
        image = "http://media.steampowered.com/steamcommunity/public/images/avatars/fe/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb.jpg"
        steam_id = 0
        while (response == []):
                first_32bit_integer = random.randint((-53687),1073741800)
                constant = 76561198000000000
                first_32bit=random.getrandbits(32)
                second_20bit=random.getrandbits(20)
                third_4bit=random.getrandbits(4)
                fourth_8bit=random.getrandbits(8)


                steam_id = (1 << 56 )+(1 << 52)+(1 << 32)+(first_32bit_integer)

                steam_response="http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8A25A8C1113B170BAA6F962ADDDF410A&steamids={0}".format(steam_id)
                steam_response_json=json.loads(urllib2.urlopen(steam_response).read())
                response = steam_response_json["response"]["players"]
        return steam_id
	
def generate_random_steamid_wpicture():
	response = []
	image = "http://media.steampowered.com/steamcommunity/public/images/avatars/fe/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb.jpg"
	steam_id = 0
	while (response == [] or image == "http://media.steampowered.com/steamcommunity/public/images/avatars/fe/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb.jpg"):
		first_32bit_integer = random.randint((-53687),1073741800)
		constant = 76561198000000000	
		first_32bit=random.getrandbits(32)
		second_20bit=random.getrandbits(20)
		third_4bit=random.getrandbits(4)
		fourth_8bit=random.getrandbits(8)

	
		steam_id = (1 << 56 )+(1 << 52)+(1 << 32)+(first_32bit_integer)

		steam_response="http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8A25A8C1113B170BAA6F962ADDDF410A&steamids={0}".format(steam_id)
		steam_response_json=json.loads(urllib2.urlopen(steam_response).read())
		response = steam_response_json["response"]["players"]
		if response !=[]:
			image = steam_response_json["response"]["players"][0]["avatar"]
	return steam_id

def get_person_name(steam_id):
	person_name_response="http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8A25A8C1113B170BAA6F962ADDDF410A&steamids={0}".format(steam_id)
	person_name_response_json=json.loads(urllib2.urlopen(person_name_response).read())
	person_name=person_name_response_json["response"]["players"][0]["personaname"]
	return person_name

def get_games_owned(steam_id):
	games_owned_response="http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=8A25A8C1113B170BAA6F962ADDDF410A&include_appinfo=1&include_played_free_games=1&steamid={0}".format(steam_id)
	games_owned_response_json=json.loads(urllib2.urlopen(games_owned_response).read())
	return games_owned_response_json



def main():
	get_games_owned(generate_random_steamid())

if __name__ =="__main__":
	random_names=[get_person_name(generate_random_steamid()),get_person_name(generate_random_steamid()),get_person_name(generate_random_steamid())]
	random_names.append("fan")
#	random.shuffle(random_names)
	print random_names
