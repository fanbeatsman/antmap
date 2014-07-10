def simplified_steam_id_32():
	steam_id = {

	'Eos': 76561198076771425,
	'Mr.Puck': 76561198047117344,
	'Zeph': 76561198086292791,
	'[.]Om nom nom nom nom': 76561198055039295,
	'[.]MickleThePickle': 76561198075589659,
	'[.]Hoang': 76561198089098210,
	'silly bear': 76561198082388214,
	'Masatenko': 76561198039423970,
	'[#]ToeKnee': 76561198094762363,
	'Biggaj': 7020619,
	}

	simplified_steam_id = {
	
	'eos': 76561198076771425,
	'Mr.Puck': 76561198047117344,
	'zeph': 76561198086292791,
	'om': 76561198055039295,
	'mickleThePickle': 76561198075589659,
	'hoang': 76561198089098210,
	'sillybear': 76561198082388214,
	'masatenko': 76561198039423970,
	'toeKnee': 76561198094762363,
	'biggaj': 7020619,
	}
	
	simplified_steam_id_32 = simplified_steam_id
	for key, value in simplified_steam_id.iteritems():
		simplified_steam_id_32[key] = value - 76561197960265728 	
	
	return simplified_steam_id_32
 
