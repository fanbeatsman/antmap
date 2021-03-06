import json
import urllib, urllib2
import sys

steam_api_key='8A25A8C1113B170BAA6F962ADDDF410A'
base_url_steam='http://api.steampowered.com'
base_url_dota='https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/'

def get_profile_picture(steam_id):
	'''if kwargs["vanityurl"]:
		
	        steam_id_query_url="{0}/ISteamUser/ResolveVanityURL/v0001/?key={1}&vanityurl={2}".format(
	           base_url_steam,
	           steam_api_key,
	           vanityurl
	            )
	
		
	#Get steam id
	try:
                player_id_json=json.loads((urllib2.urlopen(steam_id_query_url).read()))
                #if steam_id["response"]["message"]!="No match":
                steam_id_x64=int(player_id_json["response"]["steamid"])

        except:
                print "Error in getting steam id: ", sys.exc_info()[0]
'''
	
	steam_id_x64=steam_id
	picture_query_url="{0}/ISteamUser/GetPlayerSummaries/v0002/?key={1}&steamids={2}".format(
	    base_url_steam,
	    steam_api_key,
	    steam_id_x64
	    )
	picture_url=None 
	player_json={}
	try:
		player_json=json.loads((urllib2.urlopen(picture_query_url).read()))
		picture_url=player_json["response"]["players"][0]["avatarfull"]
	except:
                print "Error in retrieving profile picture: ", sys.exc_info()[0]
	
	return picture_url



def get_steam_id(vanityurl, **kwargs):
        """
        Get a player's steam id from their steam name/ vanity URL
        """
        return None


def get_stats(vanityurl, **kwargs):
		

	dota_api_key=steam_api_key
	base_url='http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'
	root_url='https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/'
	player='Mr.Puck'

	steam_id_query_url="{0}?key={1}&vanityurl={2}".format(
	    base_url,
	    dota_api_key,
	    vanityurl
	    )
	try:
                steam_id=json.loads((urllib2.urlopen(steam_id_query_url).read()))
		#if steam_id["response"]["message"]!="No match":
		steam_id=int(steam_id["response"]["steamid"])
			
			
	except:
		print "Error in getting steam id: ", sys.exc_info()[0]
	
	query_url="{0}?key={1}".format(
	    root_url,
	    dota_api_key
	    )
	
	results=[]
	json_response=None
	try:
		response=urllib2.urlopen(query_url).read()
		json_response=json.loads(response)

		for result in json_response['result']['matches']:
			results.append([
			result.keys()
			#'hero_id': result['hero_id'],
			#'account_id': result['account_id']
			])
	except urllib2.URLError, e:
		print "Error: ", e

	return steam_id_query_url
			    
