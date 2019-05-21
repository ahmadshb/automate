def Enhancement():
    enhancement = [
        [
            #1x Cost
            #Potential 1
            [0.363, 0.434],
            #Potential 2
            [0.181, 0.217],
            #Potential 3
            [0.121, 0.145],
            #Potential 4
            [0.06, 0.072],
            #Potential 5
            [0.045, 0.054]
        ],
        [
            #2x Cost
            #Potential 1
            [0.181, 0.217],
            #Potential 2
            [0.09, 0.109],
            #Potential 3
            [0.06, 0.072],
            #Potential 4
            [0.03, 0.036],
            #Potential 5
            [0.022, 0.027]
        ]
    ]

    return enhancement


def GoldCost():
    #Cost of enhancement per %
    gold_cost = [5000, 10000, 15000, 30000, 40000]
    return gold_cost


def Specials():
    special_missions = [
        [
            #Special Set Title, Shifter
            ["Spidey's Rogues Gallery", "Vulture", "Speed"],
            #Mission 1
            ["The Lullaby of Sandman", "Sandman", "Combat"],
            #Mission 2
            ["Beauty and the Beasts", "Lizard", "Combat"],
            #Mission 3
            ["The Hunter and the Hunted", "Kraven The Hunter", "Speed"],
            #Mission 4
            ["Time is Running Out", "Rhino", "Combat"],
            #Mission 5
            ["The A.I.M. is clear", "Mysterio", "Blast"]
        ],
        [
            #Special Set Title, Shifter
            ["Inhumans", "Inferno", "Blast"],
            #Mission 1
            ["Inhuman Visitor", "Gorgon", "Combat"],
            #Mission 2
            ["Karnak Lights up Broadway", "Karnak", "Speed"],
            #Mission 3
            ["Crystal Palace", "Crystal", "Blast"],
            #Mission 4
            ["Savage Is as Savage Does", "Moon Girl", "Blast"],
            #Mission 5
            ["Homecoming", "Maximus", "Blast"]
        ],
        [
            #Special Set Title, Shifter
            ["New Avengers", "Gwenpool", "Speed"],
            #Mission 1
            ["We'll Always Have Paris", "White Tiger", "Combat"],
            #Mission 2
            ["Jungle Boogie", "Wiccan", "Blast"],
            #Mission 3
            ["A Green Monster in Shanghai.", "Hulkling", "Combat"],
            #Mission 4
            ["Baked Alaska", "Songbird", "Blast"],
            #Mission 5
            ["New York State of Mind", "Squirrel Girl", "Speed"]
        ]
    ]
    return special_missions


def CTPs():
    ctps = [[
        'Authority', 'Realm of Kings Quest Pack Reward, Custom Gear Chest',
        '''• Applies to: Self
  Guard Break Immunity
• Critical Damage ↑ +45%
• Activation Rate: when HP is below 50%:
  Applies to: Self
  Accumulates 100% of True Damage regardless of Defense and Dodge stats.
  The total true damage accumulated cannot exceed 10% of HP. (7 sec.)
  Increases Attack by +5% for each 1% of damage taken. (7 sec.)
  Invincible (5 sec.)
  Cooldown Time 10 seconds''', 'https://i.imgur.com/IBIsuaE.png'
    ], [
        'Energy',
        'Cinematic Battle Reward (Mythic Hela, Killmonger), Story Mission 13-8 First Clear Reward, Custom Gear Chest',
        '''• Ignore Dodge +45%
• Critical Damage ↑ +45%
• Activation Rate: 10% chance when attacking
  Applies to: Self
  Increases Chain Hit damage by 30% when attacking. (5 sec.)
  Increases damage by 200% for 1 attack(s). (5 sec.)
  Cooldown Time 7 seconds''', 'https://i.imgur.com/Wp5xlsy.png'
    ], [
        'Destruction', 'New Avengers Quest Pack Reward, Custom Gear Chest',
        '''• Critical Damage ↑ +45%
• Applies to: Self
  Guard Break Immunity
• Activation Rate: 10% chance when attacking
  Applies to: Self
  30% chance to penetrate with SUPER ARMOR, BARRIER, ALL DAMAGE IMMUNE, INVINCIBLE effect. (5 sec.)
  Increases damage by 200% for 1 attack(s). (5 sec.)
  Cooldown Time 7 seconds''', 'https://i.imgur.com/J7dVhbw.png'
    ], [
        'Refinement',
        'Cinematic Battle Reward (Mythic Hulk, Shuri), Custom Gear Chest',
        '''• Max HP ↑ +34%
• Recovery Rate ↑ +90%
• Activation Rate: when HP is below 50%
  Applies to: Self
  Guard against 6 hits (6 sec.)
  20% Recovery of MAX HP.
  Cooldown Time 15 seconds''', 'https://i.imgur.com/75XVqes.png'
    ], [
        'Transcendence', 'Hidden Route Reward', '''• All Attack ↑ +40%
• Ignore Dodge +45%
• Activation Rate: when HP is below 50%
  Applies to: Self
  Decreases the effect of Reflect by 50%
  Reflects effect(s): PHYSICAL REFLECT, ENERGY REFLECT (5 sec.)
  Invincible (5 sec.)
  Cooldown Time 10 seconds''', 'https://i.imgur.com/eVtYF8p.png'
    ], [
        'Patience', 'Boost Point Stage 2 Reward', '''• Dodge ↑ +40%
• All Attack ↑ +40%
• Activation Rate: when HP is below 50%
  Applies to: Self
  Decreases the effect of Reflect by 50%
  Reflects effect(s): PHYSICAL REFLECT, ENERGY REFLECT (5 sec.)
  Invincible (5 sec.)
  Cooldown Time 10 seconds''', 'https://i.imgur.com/etw0hUL.png'
    ], [
        'Regeneration', 'Custom Gear Chest', '''• Max HP ↑ +34%
• Guard Break Immunity, Increase HP Regen by 90%
• Activation Rate: when HP is below 50%
  Applies to: Self
  Generates a Shield that is 35% of Max HP and ignores Cancel and Pierce effects (5 sec.)
  Recover 10% of Max HP
  Cooldown Time 10 seconds''', 'https://i.imgur.com/TRsLAIl.png'
    ], [
        'Rage', 'Custom Gear Chest', '''• Critical Rate ↑ +32%
• Dodge ↑ +32%
• Activation Rate: 20% chance when dealing critical attack
  Applies to: Self
  Ignores Boss's Damage Decrease by 60% (5 sec.)
  Increases 0.9% damage per 1% of Dodge Rate and Critical Rate, regardless of Guaranteed Dodge Rate and Guaranteed Critical Rate (5 sec.)
  Cooldown Time 7 seconds''', 'https://i.imgur.com/7K0Xz07.png'
    ], ['Veteran', '???', '???', 'https://i.imgur.com/CcJgA5g.png']]
    return ctps


def Missions():
    missions = [
        #['mission name', max entries, energy cost at s1bp, bpcost, 'img_name', 'config_name]
        ['Memory Mission', 3, 8, 4, 'memory_mission', 'memory_mission'],
        ['Dark Dimension', 3, 8, 4, 'dark_dimension', 'dark_dimension'],
        [
            "Veiled Secret: Magneto's Might", 2, 4, 4, 'veiled_secret',
            'magnetos_might'
        ],
        [
            "Veiled Secret: Rise Of The Phoenix", 2, 4, 4, 'veiled_secret',
            'rise_of_the_phoenix'
        ],
        ["Mutual Enemy", 2, 4, 4, 'mutual_enemy', 'mutual_enemy'],
        [
            "Stupid X-Men: Chrome-Plated Comrade", 3, 4, 4, 'stupid_x-men',
            'chrome-plated_comrade'
        ],
        [
            "Stupid X-Men: Psy-Locked Out", 3, 4, 4, 'stupid_x-men',
            'psy-locked_out'
        ],
        [
            "The Big Twin: Cutting Cable", 3, 4, 4, 'the_big_twin',
            'cutting_cable'
        ],
        [
            "The Big Twin: Ending the Stryfe", 3, 4, 4, 'the_big_twin',
            'ending_the_stryfe'
        ],
        [
            "Beginning of the Chaos", 2, 4, 4, 'beginning_of_the_chaos',
            'beginning_of_the_chaos'
        ],
        [
            "New Faces: Inhuman Princess", 3, 4, 4, 'new_faces',
            'inhuman_princess'
        ],
        ["New Faces: Mean & Green", 3, 4, 4, 'new_faces', 'mean_green'],
        [
            "Twisted World: Latverian Champion", 3, 4, 4, 'twisted_world',
            'latverian_champion'
        ],
        [
            "Twisted World: In the Shadow of Doom", 3, 4, 4, 'twisted_world',
            'in_the_shadow_of_doom'
        ],
        ["Doom's Day", 2, 4, 4, 'dooms_day', 'dooms_day'],
        ["Daily Mission", 2, 6, 4, 'daily_mission', 'daily_mission'],
        ["Special Mission", 20, 5, 4, 'special_mission', 'special_mission'],
        ["Co-Op Play", 5, 0, 0, 'co-op_play', ''],
    ]
    return missions


def Collections():
    collections = [
        [
            [
                #Sorcerer Supreme
                [
                    "Cloak of Levitation",
                    "Dimension Chest: 6★ ISO-8 (Awakened)"
                ],
                ["Magical Fabric", 30, "Mysterious Ambush"],
                ["Ancient Thread and Needle", 4, "Dark Advent"],
                ["Levitation Spell Seal", 15, "Increasing Darkness"]
            ],
            [
                ["Sling Ring", "25 Biometrics: Clea"],
                ["Ancient Metal", 100, "Road to the Monastery"],
                ["Teleportation Spell Seal", 25, "Dark Advent"],
                ["Dimensional Power Source", 25, "Increasing Darkness"],
            ],
            [
                ["Book of Cagliostro", "Extreme Obelisk"],
                ["Chains of Restraint", 50, "Mysterious Ambush"],
                ["Mystic Pages", 30, "Power of the Dark"],
                ["Sealing Spell", 25, "Monastery in Trouble"],
            ],
            [
                ["Axe of Angarruumus", "100 Norn Stones of Chaos"],
                ["An Old Tree", 8, "Road to the Monastery"],
                ["Magical Metal", 1, "Mysterious Ambush"],
                ["Blessing of the Moon", 1, "Power of the Dark"],
            ],
            [
                ["Dragon Fang", "100 Rank 1 Black Anti-Matter"],
                ["Extradimensional Dragon Tusk", 20, "Dark Advent"],
                ["Carving Mallet", 5, "Monastery in Trouble"],
                ["Dragonslaying Spell", 15, "Power of the Dark"],
            ],
        ],
        [
            #X-Men
            [
                ["Adamantium", "200 Phoenix Feathers"],
                ["Special Container", 50, "Weathering the Storm"],
                ["Liquid Adamantium", 20, "Magneto's Might"],
                ["Adamantium Syringe", 20, "Rise of the Phoenix"],
            ],
            [
                ["Blackbird", "Extreme Obelisk"],
                ["Light Metal", 100, "Magneto's Might"],
                ["Jet Engine", 30, "Blindsided!"],
                ["Instrument Panel", 20, "Weathering the Storm"],
            ],
            [
                ["Cyclops' Visor", "Selector: X-Genes x50"],
                ["Visor Frame", 50, "Friends and Enemies"],
                ["Output Control Dial", 50, "Going Rogue"],
                ["Optical Glass", 15, "Weathering the Storm"],
            ],
            [
                ["Image Inducer", "6★ Mega Rank Up Ticket"],
                ["Portable Device", 1, "Friends and Enemies"],
                ["Hologram Projector", 10, "Rise of the Phoenix"],
                ["Activation Button", 10, "Going Rogue"],
            ],
            [
                ["Crimson Gem of Cyttorak", "200 M'Kraan Crystals"],
                ["Crimson Trace", 30, "Going Rogue"],
                ["Crimson Cosmic Dimension", 35, "Friends and Enemies"],
                ["Power of Cyttorak", 45, "Blindsided!"],
            ],
            [
                ["Phoenix Force", "Enchanted Uru Chest: Mythic"],
                ["Traces of Phoenix Force", 5, "Blindsided!"],
                [
                    "Forces of Creation and Destruction", 15,
                    "Rise of the Phoenix"
                ],
                ["New Host", 10, "Magneto's Might"],
            ]
        ],
        [
            #X-Force
            [
                ["Submachine Gun", "25 X-Genes: Colossus"],
                ["Breechblock", 30, "Chrome-Plated Comrade"],
                ["High-Capacity Magazine", 80, "Aw Man, This Guy?"],
                ["Safety Device", 50, "Domino Falls"],
            ],
            [
                ["Cable's Gene", "Uniform Upgrade Ticket: Mythic"],
                ["Genetic Blueprint", 15, "Chrome-Plated Comrade"],
                ["Sample Container", 30, "Aw Man, This Guy?"],
                ["A Special Chromosome", 15, "Psy-Locked Out"],
            ],
            [
                ["Katana", "Extreme Obelisk"],
                ["Hammer and Anvil", 30, "Domino Falls"],
                ["Quality Metal", 30, "Ending the Stryfe"],
                ["Ancient Production Method", 25, "Cutting Cable"],
            ],
            [
                ["Time Travel Device", "250 Phoenix Feathers"],
                ["Time Travel Device Blueprint", 15, "Psy-Locked Out"],
                ["Fusion Energy Reactor", 15, "Cutting Cable"],
                ["Quantum Mechanics", 10, "Ending the Stryfe"],
            ]
        ],
        [
            #First Family
            [
                ["Fantasti-Flare", "Enchanted Uru Chest: Mythic"],
                ["Flare Gun", 40, "Clobberin' Time"],
                ["Signal Flare", 50, "Hothead"],
                ["Special Smoke", 30, "Inhuman Princess"],
            ],
            [
                ["Doombot", "Dimension Chest: 6★ ISO-8"],
                ["Doombot", 5, "In the Shadow of Doom"],
                ["Dismantle Device", 20, "Inhuman Princess"],
                ["Doombot Schematics", 10, "Latverian Champion"],
            ],
            [
                ["Unstable Molecule", "25 Biometrics: Victorious"],
                ["Substance Molecule", 30, "Mean and Green"],
                ["Uniform Fabric", 30, "In the Shadow of Doom"],
                ["Fantastic Four Uniform", 50, "Clobberin' Time"],
            ],
            [
                ["Baxter Building Blueprint", "Rank 6 Black Anti-Matter"],
                ["Archived Blueprint File", 20, "Latverian Champion"],
                ["Architecture Certification", 30, "Hothead"],
                ["Mr. Fantastic's Plans", 10, "Mean and Green"]
            ]
        ]
    ]

    return collections


def HeroicQuest1():
    heroic_quest_1 = [[
        'Region 1',
        ['Story Mission', 10],
        ['Dimension Rift', 10],
        ['Daily Mission', 2],
        ['Use Gold', 300000],
        ['Special Mission', 10],
        ['World Boss Invasion (Participate)', 2],
        ['Co-Op Play Reward', 2],
        ['Daily Mission', 2],
        ['Story Mission', 10],
        ['Timeline Battle (Participate)', 3],
        ['Normal Alliance Battle', 1],
        ['Villain Siege', 2],
        ['Special Mission (Hidden Route)', 2],
        ['Upgrade Cards', 10],
        ['Dimension Rift', 10],
        ['World Boss (Clear)', 3],
        ['Special Mission', 10],
        ['Use Energy', 50],
        ['World Boss (Clear)', 3],
        ['Dimension Rift', 10],
        ['Villain Siege (Hard)', 1],
        ['World Boss Invasion (Co-Op Mission)', 2],
        ['Story Mission', 10],
        ['Upgrade Cards', 10],
        ['Normal Alliance Battle (50 000+ Points)', 1],
        ['Story Mission (Chapter 5-10)', 1],
        ['Timeline Battle (Wins)', 10],
        ['Daily Mission', 2],
        ['Use Energy', 50],
        ['Special Mission (Hidden Route)', 2],
        ['Co-Op Play Reward', 2],
        ['Upgrade Custom Gears', 2],
        ['Villain Siege', 2],
        ['Story Mission', 10],
        ['Co-Op Play Reward', 2],
        ['Normal Alliance Battle', 2],
        ['World Boss Invasion (Co-Op Mission)', 2],
        ['Use Gold', 300000],
        ['Special Mission', 10],
        ['Villain Siege (Hard)', 1],
        ['Upgrade Cards', 10],
        ['World Boss (Participate)', 3],
        ['Story Mission (Chapter 5-10) (With Arachknight)', 1],
        ['Daily Mission', 2],
        ['Clear Unexpected Support', 1],
    ], [
        'Region 2',
        ['Co-Op Play Reward', 2],
        ['World Boss (Clear)', 3],
        ['Story Mission', 10],
        ['Use Gold', 300000],
        ['Special Mission', 10],
        ['World Boss (Clear)', 3],
        ['Use 50 Energy', 1],
        ['Daily Mission', 2],
        ['Dimension Rift', 10],
        ['World Boss Invasion (Participate)', 2],
        ['Villain Siege', 2],
        ['Story Mission', 10],
        ['Special Mission (Hidden Route)', 2],
        ['Upgrade Cards', 10],
        ['Dimension Rift', 10],
        ['Timeline Battle (Participate)', 3],
        ['Co-Op Play Reward', 2],
        ['Normal Alliance Battle', 2],
        ['World Boss (Participate)', 3],
        ['Special Mission', 10],
        ['Villain Siege (Hard)', 1],
        ['Use Energy', 50],
        ['Timeline Battle (Participate)', 1],
        ['World Boss Invasion (Co-Op Mission)', 2],
        ['Normal Alliance Battle (50 000+ Points', 1],
        ['Daily Mission', 2],
        ['Story Mission (Chapter 6-3)', 1],
        ['Use Gold', 300000],
        ['Story Mission', 10],
        ['Special Mission', 15],
        ['Dimension Rift', 10],
        ['Villain Siege', 2],
        ['Upgrade Custom Gears', 2],
        ['Story Mission (Chapter 6-3) (With Arachknight)', 1],
        ['Use Energy', 50],
        ['Normal Alliance Battle', 1],
        ['Use Gold', 300000],
        ['World Boss Invasion (Co-Op Mission)', 2],
        ['Story Mission', 10],
        ['Upgrade Cards', 10],
        ['Timeline Battle (Win)', 10],
        ['Special Mission', 10],
        ['Normal Alliance Battle (50 000+ Points)', 1],
        ['Daily Mission', 2],
        ['Clear Unexpected Support', 1],
    ], [
        'Region 3', ['Special Mission', 10], ['Use Energy',
                                              50], ['Villain Siege (Hard)',
                                                    1], ['Upgrade Cards', 10],
        ['Dimension Rift', 10], ['Co-Op Play Reward', 2], ['Daily Mission', 2],
        ['Normal Alliance Battle', 1], ['Villain Siege (Hard)', 1], [
            'Story Mission', 10
        ], ['Use Gold', 300000], ['Daily Mission', 2], ['Villain Siege', 2], [
            'World Boss (Participate)', 3
        ], ['Dimension Rift', 10], ['Co-Op Play Reward', 2], [
            'World Boss Invasion (Participate)', 2
        ], ['Story Mission', 10], ['Special Mission (Hidden Route)',
                                   2], ['Dimension Rift',
                                        10], ['Timeline Battle (Win)', 10],
        ['World Boss Invasion (Co-Op Reward)', 2], []
    ]]
    return heroic_quest_1


def HeroicQuest2():
    heroic_quest_2 = []
    return heroic_quest_2