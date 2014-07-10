import json
import urllib, urllib2
from bushstats.steam_id import simplified_steam_id

def get_steam_id(vanityurl, **kwargs):
	"""
	Get a player's steam id from their steam name/ vanity URL
	"""
	return None
	

def get_stats(vanityurl, **kwargs):
		

	dota_api_key='8A25A8C1113B170BAA6F962ADDDF410A'
	base_url='http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/'
	root_url='https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/'
	player='Mr.Puck'

	steam_id_query_url="{0}?key={1}&vanityurl={2}".format(
	    base_url,
	    dota_api_key,
	    vanityurl
	    )
	try:
                steam_id=(urllib2.urlopen(steam_id_query_url).read())
		if steamd_id["response"]["message"]!="No match":
			steam_id=int(steam_id["response"]["steamid"])
			
			
	except urllib2.URLError, e:
		print "Error in getting steam id: ", e
	
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
			    
