import random

loadout = []

tactical = ['Cloak', 'Pulse Blade', 'Grapple', 'Stim', 'A-Wall', 'Phase Shift', 'Holo Pilot']
ordnance = ['Frag Grenade', 'Arc Grenade', 'Firestar', 'Gravity Star', 'Electric Smoke Grenade', 'Satchel']
primary = {
    'Assault Rifle': ['R-201 Carbide', 'R-101 Carbide', 'Hemlock BF-R', 'G2A5', 'V-47 Flatline'],
    'Submachine Gun': ['CAR', 'Alternator', 'Volt', 'R-97'],
    'Light Machine Gun': ['Spitfire', 'L-STAR', 'X-55 Devotion'],
    'Sniper Rifle': ['Kraber-AP Sniper', 'D-2 Double Take', 'Longbow-DMR'],
    'Shotgun': ['EVA-8 Auto', 'Mastiff'],
    'Grenadier': ['Sidewinder SMR', 'EPG-1', 'R-6P Softball', 'EM-4 Cold War'],
    'Pistol': ['Wingman Elite', 'SA-3 Mozambique']
}
secondary = {
    'Pistol': ['RE-45 Auto', 'Hammond P2016', 'B3 Wingman'],
    'Anti-Titan': ['Charge Rifle', 'MGL Mag Launcher', 'LG-97 Thunderbolt', 'Archer']
}
backup = {
    'Pistol': ['RE-45 Auto', 'Hammond P2016', 'B3 Wingman'],
    'Anti-Titan': ['Charge Rifle', 'MGL Mag Launcher', 'LG-97 Thunderbolt', 'Archer']
}
kit_1 = ['Power Cell', 'Fast Regen', 'Ordnance Expert', 'Phase Embark']
kit_2 = ['Kill Report', 'Wallhang', 'Hover', 'Low Profile', 'Titan Hunter']

titans = ['Ion', 'Scorch', 'Northstar', 'Ronin', 'Tone', 'Legion', 'Monarch']

boosts = ['Amped Weapons', 'Ticks', 'Pilot Sentry', 'Map Hack', 'Battery Back-Up', 'Radar Jammer', 'Titan Sentry',
          'Smart Pistol', 'Phase Rewind', 'Hard Cover', 'Holo Pilot Nova', 'Dice Roll']

temp_list_1 = ['Assault Rifle', 'Submachine Gun', 'Light Machine Gun', 'Sniper Rifle', 'Shotgun', 'Grenadier', 'Pistol']
temp_list_2 = ['Pistol', 'Anti-Titan']
temp_list_3 = ['Pistol', 'Anti-Titan']

loadout.append(tactical[random.randint(0, 6)])
loadout.append(ordnance[random.randint(0, 5)])
primary_weapon_type = temp_list_1[random.randint(0, 6)]
loadout.append(primary[primary_weapon_type][random.randint(0, len(primary[primary_weapon_type]) - 1)])
secondary_weapon_type = temp_list_2[random.randint(0, 1)]
temp_list_3.remove(secondary_weapon_type)
loadout.append(secondary[secondary_weapon_type][random.randint(0, len(secondary[secondary_weapon_type]) - 1)])
loadout.append(backup[temp_list_3[0]][random.randint(0, len(backup[temp_list_3[0]]) - 1)])
loadout.append(kit_1[random.randint(0, 3)])
loadout.append(kit_2[random.randint(0, 4)])

print('Here is your pilot loadout: \n')
print(loadout[0] + ', ' + loadout[1])
print(loadout[2])
print(loadout[3])
print(loadout[4])
print(loadout[5] + ', ' + loadout[6])
print('Titan: ' + titans[random.randint(0, 6)])
print('Boost: ' + boosts[random.randint(0, len(boosts) - 1)])

print('\nPick and choose mods as you feel are necessary to give you the upper hand in battle!')
