#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs


import uservar
from .addonvar import addon_profile,translatePath,addon,addon_icon,addon_name,addon_path
from .utils import Log,DialogBusy

file = translatePath(os.path.join(addon_profile,'whitelist.json'))

HOME = 10000

def ReadWhiteList():
	with open(file, 'r') as f:
		data = json.load(f)
	return data


def WhiteListAddons(data):
	#Get all addons in white list
	addons = data.get('whitelist')
	return addons

def IsinWhitelist(addonID):
	#Check whitelist for addon
	if addonID in WhiteListAddons(ReadWhiteList()):
		return True
	else:
		return False

def GetSysAddons():
	addons = xbmc.executeJSONRPC(json.dumps({"jsonrpc":"2.0","method":"Addons.GetAddons","params":{"enabled":True},"id":"1"}))
	addons = json.loads(addons)['result']['addons']
	return addons


def ContextMenu():
	addons = ','.join(WhiteListAddons(ReadWhiteList()))
	addons.replace(' ','')
	xbmcgui.Window(HOME).setProperty('WHITELIST',addons)

def ReloadWhitelistProperty(addons: list):
	a = ','.join(addons)
	a.replace(' ','')
	xbmcgui.Window(HOME).setProperty('WHITELIST',a)

def AddWhiteList(addonID):
	Log(f'adding {addonID} to whitelist')
	addons = WhiteListAddons(ReadWhiteList())
	Log(addons)
	if addonID not in addons:
		addons.append(addonID)
	with open(file,'w') as f:
		json.dump({'whitelist':addons},f,indent=4)
	if IsinWhitelist(addonID):
		xbmcgui.Dialog().notification(addon_name, f"{xbmcaddon.Addon(addonID).getAddonInfo('name')} {addon.getLocalizedString(30067)} {addon_name} {addon.getLocalizedString(30068)}",addon_icon)
		ReloadWhitelistProperty(addons)
	else:
		xbmcgui.Dialog().notification(addon_name, f"{xbmcaddon.Addon(addonID).getAddonInfo('name')} {addon.getLocalizedString(30070)} {addon_name} {addon.getLocalizedString(30068)}",addon_icon)



def RemoveWhiteList(addonID):
	Log(f'Removing {addonID} from whitelist')
	addons = WhiteListAddons(ReadWhiteList())
	if addonID in addons:
		addons.remove(addonID)
	with open(file,'w') as f:
		json.dump({'whitelist':addons},f,indent=4)
	if not IsinWhitelist(addonID):
		xbmcgui.Dialog().notification(addon_name,f"{xbmcaddon.Addon(addonID).getAddonInfo('name')} {addon.getLocalizedString(30069)} {addon_name} {addon.getLocalizedString(30068)}",addon_icon)
		ReloadWhitelistProperty(addons)
	else:
		xbmcgui.Dialog().notification(addon_name,f"{xbmcaddon.Addon(addonID).getAddonInfo('name')} {addon.getLocalizedString(30071)} {addon_name} {addon.getLocalizedString(30068)}",addon_icon)


