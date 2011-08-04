import random
import pprint
import operator

pp = pprint.PrettyPrinter(indent=4)

notR = 1900

nTimes = 1000000

# player : [race, elo, vt, vz, vp]

maps = {
    "Bel'Shir Beach": {"TvZ": 40.9, "ZvP": 55, "PvT": 45 },
    "Crevasse": {"TvZ": 56.4, "ZvP": 53.1, "PvT": 44},
    "Crossfire" : {"TvZ": 36.7, "ZvP": 60, "PvT": 52.6},

    "Dual Sight" : {"TvZ": 48.4, "ZvP": 55.6, "PvT": 48},
    "Metalopolis" : {"TvZ": 52.9 , "ZvP": 44.4, "PvT": 38.7},
    "Tal'Darim Altar" : {"TvZ": 53.8, "ZvP": 35.7, "PvT": 42.1},

    "Xel'Naga Caverns" : {"TvZ": 55, "ZvP": 46.4, "PvT": 45.5},
    "Xel'Naga Fortress" : {"TvZ": 38.5, "ZvP":58.3, "PvT":38.1},
    "Terminus" : {"TvZ": 69, "ZvP": 76.2, "PvT": 48},
}

for k, v in maps.iteritems():
    v["TvT"] = 50
    v["PvP"] = 50
    v["ZvZ"] = 50

    v["ZvT"] = 100-v["TvZ"]
    v["TvP"] = 100-v["PvT"]
    v["PvZ"] = 100-v["ZvP"]

players = {
    # Group A
    "NesTea": ["Z", 2298, {"T":2126, "Z":2256, "P":2185}],
    "Kyrix": ["Z", 1972, {"T":1950, "Z":1971, "P":2059}],
    "MMA": ["T", 2084, {"T":2083, "Z":2091, "P":1932}],
    "Happy": ["T", 2070, {"T":2039, "Z":2061, "P":1986}],

    # Group B
    "MC": ["P", 2162, {"T":2122, "Z":2073, "P":2073}],
    "MVP": ["T", 2149, {"T":2144, "Z":2159, "P":2044}],
    "Polt": ["T", 2223, {"T":2089, "Z":2053, "P":2183}],
    "Noblesse": ["T", 2039, {"T":2080, "Z":2002, "P":1982}],

    # Group C
    "Bomber": ["T", 2241, {"T":2212, "Z":2078, "P":2200}],
    "viOlet": ["Z", 2031, {"T":1937, "Z":2096, "P":2016}],
    "HuK": ["P", 2048, {"T":2073, "Z":2034, "P":1925}],
    "Killer": ["P", 2055, {"T":2067, "Z":2038, "P":1968}],

    # Group D
    "CoCa": ["Z", 2042, {"T":1930, "Z":1956, "P":2104}],
    "Keen": ["T", 2061, {"T":2011, "Z":2011, "P":2032}],
    "NaDa": ["T", 2116, {"T":2121, "Z":2037, "P":2049}],
    "Alicia": ["P", 2135, {"T":2079, "Z":2033, "P":2056}],

    # Group E
    "Byun": ["T", 2110, {"T":2120, "Z":1991, "P":2038}],
    "Zenio": ["Z", 2052, {"T":1989, "Z":2127, "P":1935}],
    "asd": ["T", 2086, {"T":2054, "Z":2067, "P":1970}],
    "Puzzle": ["P", 2182, {"T":2126, "Z":2029, "P":2116}],

    # Group F
    "TricKsteR": ["P", 2048, {"T":1954, "Z":2071, "P":2021}],
    "Ryung": ["T", 2150, {"T":2110, "Z":2067, "P":1990}],
    "aLive": ["T", 2085, {"T":2046, "Z":2057, "P":2111}],
    "TOP": ["T", 2127, {"T":2123, "Z":2049, "P":2013}],

    # Group G
    "HongUn": ["P", 2061, {"T":2044, "Z":2029, "P":1979}],
    "Virus": ["T", 1982, {"T":1976, "Z":1986, "P":1953}],
    "Clide": ["T", 2016, {"T":2051, "Z":1989, "P":1968}],
    "SuperNoVa": ["T", 2054, {"T":2005, "Z":2039, "P":2034}],

    # Group H
    "LoSirA": ["Z", 2147, {"T":2029, "Z":2068, "P":2162}],
    "Ensnare": ["T", 2026, {"T":1986, "Z":2034, "P":2064}],
    "July": ["Z", 2045, {"T":2063, "Z":1948, "P":2035}],
    "Genius": ["P", 1979, {"T":2027, "Z":1954, "P":2012}],

    # Code A Players
    "FruitDealer": ["Z", 1980, {"T":2014, "Z":2014, "P":1939}],
    "Maru": ["T", notR, {"T":notR, "Z":notR, "P":notR}],
    "Banbanssu": ["P", 1943, {"T":1860, "Z":1985, "P":2003}],
    "GanZi": ["T", 2035, {"T":1989, "Z":2052, "P":1983}],

    # used international figures and scaled them down by 0.88
    # "SaSe": ["P", 2330, {"T":2251, "Z":2086, "P":2185}],
    "SaSe": ["P", 2050, {"T":1980, "Z":1835, "P":1922}],
    "Sniper": ["Z", notR, {"T":notR, "Z":notR, "P":notR}],
    "Check": ["Z", 1961, {"T":1897, "Z":1964, "P":2008}],
    # scaled down from intl by 0.88:
    "Naniwa": ["P", 2013, {"T":1962, "Z":1865, "P":1927}],

    "sC": ["T", 2076, {"T":2039, "Z":1998, "P":2085}],
    "Extreme": ["P", notR, {"T":notR, "Z":notR, "P":notR}],
    "Tails": ["P", 2041, {"T":2048, "Z":1995, "P":2047}],
    "Taeja": ["T", 2067, {"T":1981, "Z":2003, "P":2079}],

    "DongRaeGu": ["Z", 2208, {"T":2155, "Z":2024, "P":2076}],
    "Inca": ["P", 2057, {"T":2009, "Z":1907, "P":2149}],
    "anypro": ["P", 1955, {"T":1890, "Z":1991, "P":2026}],
    "JYP": ["P", 2092, {"T":1940, "Z":2028, "P":2050}],

    "Tassadar": ["P", 1996, {"T":1928, "Z":2078, "P":1990}],
    "Fenix": ["T", 1855, {"T":1825, "Z":1826, "P":1811}],
    "Yoda": ["T", 1985, {"T":2008, "Z":1994, "P":1936}],
    "TheBest": ["T", 2077, {"T":1985, "Z":1989, "P":1953}],

    "BoxeR": ["T", 1970, {"T":1998, "Z":1900, "P":1998}],
    "Leenock": ["Z", 2071, {"T":2158, "Z":2001, "P":1904}],
    "Dream": ["T", 2008, {"T":1954, "Z":2010, "P":2044}],
    "Maka": ["T", 2076, {"T":2009, "Z":2040, "P":2097}],

    "Jinro": ["T", 1980, {"T":2000, "Z":1935, "P":2055}],
    "Lucky": ["Z", 2017, {"T":1997, "Z":2004, "P":2000}],
    "Luvsic": ["Z", 1962, {"T":1930, "Z":2000, "P":2025}],
    "Jjakji": ["T", 2180, {"T":2051, "Z":2125, "P":2149}],

    "YuGiOh": ["Z", 1970, {"T":2020, "Z":1984, "P":1984}],
    # scaled down from intl by 0.88:
    "Thorzain": ["T", 1958, {"T":1901, "Z":1841, "P":1932}],
    "MarineKing": ["T", 2047, {"T":1968, "Z":2139, "P":2027}],
    "Hack": ["T", 2060, {"T":2001, "Z":1967, "P":2047}],

    # teams
    # SlayerS

    # Prime

           
           }

def elo(a, b):
    return 1/(1 + 10 ** ((b-a)/400))


def get_matchup(A, B):
    return players[A][0] + "v" + players[B][0]

def predict_result_on(map, A, B):
    pA = predict_result(A, B)

    matchup = get_matchup(A, B)
    
    modifier = float(maps[map][matchup])/100

    mpA = modifier * pA
    mpB = (1-modifier) * (1-pA)
    
    npA = mpA / (mpA + mpB)
    
    return npA

        

def predict_result(A, B):
    # return the probability of player A winning
    R_A = float(players[A][1])
    R_B = float(players[B][1])
    # print R_A, R_B
    R_A_vs = float(players[A][2][players[B][0]])
    R_B_vs = float(players[B][2][players[A][0]])
    # print R_A_vs, R_B_vs
    R_Ap = float(R_A + R_A_vs)
    R_Bp = float(R_B + R_B_vs)
    # print R_Ap, R_Bp
    E_A = elo(R_Ap, R_Bp)
    # print E_A
    return float(E_A)

def simulate_bo(n, A, B):
    pA = predict_result(A, B)

    wins = n / 2 + 1

    wA = 0
    wB = 0
    
    while (wA < wins) and (wB < wins):
        if random.random() < pA:
            wA = wA + 1
        else:
            wB = wB + 1

    if wA >= wins:
        return A
    else:
        return B  

# A plays B, C plays D
def simulate_group(A, B, C, D):
    pA = predict_result(A, B)
    pC = predict_result(C, D)
    
    w1 = B
    w2 = D

    l1 = A
    l2 = C

    if random.random() < pA:
        w1 = A
        l1 = B

    if random.random() < pC:
        w2 = C
        l2 = D

    # winner's match
    
    pWM = predict_result(w1, w2)
    
    wWM = w2
    lWM = w1

    if random.random() < pWM:
        wWM = w1
        lWM = w2

    # loser's match

    pLM = predict_result(l1, l2)

    wLM = l2
    lLM = l1

    if random.random() < pLM:
        wLM = l1
        lLM = l2
        
    # third match

    pTM = predict_result(lWM, wLM)

    second = wLM
    third = lWM

    if random.random() < pTM:
        second = lWM
        third = wLM

    return [wWM, second, third, lLM]

master = { }

def tab_add(stage, who):
    if stage not in master:
        master[stage] = { }
    else:
        if who not in master[stage]:
            master[stage][who] = 1
        else:
            master[stage][who] = master[stage][who] + 1

def simulate_gsl_august():
    # group stage
    A1, A2, A3, A4 = simulate_group("NesTea", "Kyrix", "MMA", "Happy")
    tab_add("A1", A1)
    tab_add("A2", A2)
    tab_add("A3", A3)
    tab_add("A4", A4)
    
    B1, B2, B3, B4 = simulate_group("MC", "MVP", "Polt", "Noblesse")
    tab_add("B1", B1)
    tab_add("B2", B2)
    tab_add("B3", B3)
    tab_add("B4", B4)
        
    C1, C2, C3, C4 = simulate_group("Bomber", "viOlet", "HuK", "Killer")
    tab_add("C1", C1)
    tab_add("C2", C2)
    tab_add("C3", C3)
    tab_add("C4", C4)
        
    D1, D2, D3, D4 = simulate_group("CoCa", "Keen", "NaDa", "Alicia")
    tab_add("D1", D1)
    tab_add("D2", D2)
    tab_add("D3", D3)
    tab_add("D4", D4)
        
    E1, E2, E3, E4 = simulate_group("Byun", "Zenio", "asd", "Puzzle")
    tab_add("E1", E1)
    tab_add("E2", E2)
    tab_add("E3", E3)
    tab_add("E4", E4)

    F1, F2, F3, F4 = simulate_group("TricKsteR", "Ryung", "aLive", "TOP")
    tab_add("F1", F1)
    tab_add("F2", F2)
    tab_add("F3", F3)
    tab_add("F4", F4)

    G1, G2, G3, G4 = simulate_group("HongUn", "Virus", "Clide", "SuperNoVa")
    tab_add("G1", G1)
    tab_add("G2", G2)
    tab_add("G3", G3)
    tab_add("G4", G4)

    H1, H2, H3, H4 = simulate_group("LoSirA", "Ensnare", "July", "Genius")
    tab_add("H1", H1)
    tab_add("H2", H2)
    tab_add("H3", H3)
    tab_add("H4", H4)

    # Ro16
    Ro8_A = simulate_bo(3, A1, B2)
    Ro8_E = simulate_bo(3, A2, B1)

    Ro8_B = simulate_bo(3, C1, D2)
    Ro8_F = simulate_bo(3, C2, D1)

    Ro8_C = simulate_bo(3, E1, F2)
    Ro8_G = simulate_bo(3, E2, F1)

    Ro8_D = simulate_bo(3, G1, H2)
    Ro8_H = simulate_bo(3, G2, H1)

    tab_add("Ro8_A", Ro8_A)
    tab_add("Ro8_B", Ro8_B)
    tab_add("Ro8_C", Ro8_C)
    tab_add("Ro8_D", Ro8_D)

    tab_add("Ro8_E", Ro8_E)
    tab_add("Ro8_F", Ro8_F)
    tab_add("Ro8_G", Ro8_G)
    tab_add("Ro8_H", Ro8_H)

    # Ro8
    Ro4_A = simulate_bo(5, Ro8_A, Ro8_B)
    Ro4_B = simulate_bo(5, Ro8_C, Ro8_D)
    
    Ro4_C = simulate_bo(5, Ro8_E, Ro8_F)
    Ro4_D = simulate_bo(5, Ro8_G, Ro8_H)

    tab_add("Ro_4_A", Ro4_A)
    tab_add("Ro_4_B", Ro4_B)
    tab_add("Ro_4_C", Ro4_C)
    tab_add("Ro_4_D", Ro4_D)

    #Ro4
    Fin_A = simulate_bo(5, Ro4_A, Ro4_B)
    Fin_B = simulate_bo(5, Ro4_C, Ro4_D)

    tab_add("Z_Fin_A", Fin_A)
    tab_add("Z_Fin_B", Fin_B)

    #finals
    Winner = simulate_bo(7, Fin_A, Fin_B)

    tab_add("Z_Winner", Winner)

    return Winner

def simulate_gsl_august_code_a():
    # Ro32
    Ro16_A = simulate_bo(3, "FruitDealer", "Maru")
    Ro16_B = simulate_bo(3, "Banbanssu", "GanZi")

    Ro16_C = simulate_bo(3, "SaSe", "Sniper")
    Ro16_D = simulate_bo(3, "Check", "Naniwa")

    Ro16_E = simulate_bo(3, "sC", "Extreme")
    Ro16_F = simulate_bo(3, "Tails", "Taeja")

    Ro16_G = simulate_bo(3, "DongRaeGu", "Inca")
    Ro16_H = simulate_bo(3, "anypro", "JYP")

    
    Ro16_I = simulate_bo(3, "Tassadar", "Fenix")
    Ro16_J = simulate_bo(3, "Yoda", "TheBest")

    Ro16_K = simulate_bo(3, "BoxeR", "Leenock")
    Ro16_L = simulate_bo(3, "Dream", "Maka")

    Ro16_M = simulate_bo(3, "Jinro", "Lucky")
    Ro16_N = simulate_bo(3, "Luvsic", "Jjakji")
    
    Ro16_O = simulate_bo(3, "YuGiOh", "Thorzain")
    Ro16_P = simulate_bo(3, "MarineKing", "Hack")

    tab_add("Ro16_A", Ro16_A)
    tab_add("Ro16_B", Ro16_B)
    tab_add("Ro16_C", Ro16_C)
    tab_add("Ro16_D", Ro16_D)

    tab_add("Ro16_E", Ro16_E)
    tab_add("Ro16_F", Ro16_F)
    tab_add("Ro16_G", Ro16_G)
    tab_add("Ro16_H", Ro16_H)

    tab_add("Ro16_I", Ro16_I)
    tab_add("Ro16_J", Ro16_J)
    tab_add("Ro16_K", Ro16_K)
    tab_add("Ro16_L", Ro16_L)

    tab_add("Ro16_M", Ro16_M)
    tab_add("Ro16_N", Ro16_N)
    tab_add("Ro16_O", Ro16_O)
    tab_add("Ro16_P", Ro16_P)


    # Ro16
    Ro8_A = simulate_bo(3, Ro16_A, Ro16_B)
    Ro8_B = simulate_bo(3, Ro16_C, Ro16_D)
    Ro8_C = simulate_bo(3, Ro16_E, Ro16_F)
    Ro8_D = simulate_bo(3, Ro16_G, Ro16_H)

    Ro8_E = simulate_bo(3, Ro16_I, Ro16_J)
    Ro8_F = simulate_bo(3, Ro16_K, Ro16_L)
    Ro8_G = simulate_bo(3, Ro16_M, Ro16_N)
    Ro8_H = simulate_bo(3, Ro16_O, Ro16_P)

    tab_add("Ro8_A", Ro8_A)
    tab_add("Ro8_B", Ro8_B)
    tab_add("Ro8_C", Ro8_C)
    tab_add("Ro8_D", Ro8_D)

    tab_add("Ro8_E", Ro8_E)
    tab_add("Ro8_F", Ro8_F)
    tab_add("Ro8_G", Ro8_G)
    tab_add("Ro8_H", Ro8_H)

    # Ro8
    Ro4_A = simulate_bo(5, Ro8_A, Ro8_B)
    Ro4_B = simulate_bo(5, Ro8_C, Ro8_D)
    
    Ro4_C = simulate_bo(5, Ro8_E, Ro8_F)
    Ro4_D = simulate_bo(5, Ro8_G, Ro8_H)

    tab_add("Ro_4_A", Ro4_A)
    tab_add("Ro_4_B", Ro4_B)
    tab_add("Ro_4_C", Ro4_C)
    tab_add("Ro_4_D", Ro4_D)

    #Ro4
    Fin_A = simulate_bo(5, Ro4_A, Ro4_B)
    Fin_B = simulate_bo(5, Ro4_C, Ro4_D)

    tab_add("Z_Fin_A", Fin_A)
    tab_add("Z_Fin_B", Fin_B)

    #finals
    Winner = simulate_bo(7, Fin_A, Fin_B)

    tab_add("Z_Winner", Winner)
       

def mass_sim(times):
    for i in range(0, times+1):
        simulate_gsl_august_code_a()
    return master

def pct(wins):
    return float(float(wins)/nTimes * 100)

def print_stage(stage):
    print stage,
    # get the names sorted by wins
    names = sorted(master[stage].iteritems(), key=operator.itemgetter(1), reverse=True)
    for k, v in names:
        print "\t", k, "\t", pct(v) 
    print ""

def bracket32():
    print_stage("Ro16_A")
    print_stage("Ro16_B")
    print_stage("Ro16_C")
    print_stage("Ro16_D")
    
    print_stage("Ro16_E")
    print_stage("Ro16_F")
    print_stage("Ro16_G")
    print_stage("Ro16_H")

    print_stage("Ro16_I")
    print_stage("Ro16_J")
    print_stage("Ro16_K")
    print_stage("Ro16_L")

    print_stage("Ro16_M")
    print_stage("Ro16_N")
    print_stage("Ro16_O")
    print_stage("Ro16_P")

    print_stage("Ro8_A")
    print_stage("Ro8_B")
    print_stage("Ro8_C")
    print_stage("Ro8_D")

    print_stage("Ro8_E")
    print_stage("Ro8_F")
    print_stage("Ro8_G")
    print_stage("Ro8_H")

    print_stage("Ro_4_A")
    print_stage("Ro_4_B")
    print_stage("Ro_4_C")
    print_stage("Ro_4_D")

    print_stage("Z_Fin_A")
    print_stage("Z_Fin_B")

    print_stage("Z_Winner")
       

# SlayerS v. Prime
print predict_result_on("Dual Sight", "Taeja", "MarineKing")
print predict_result_on("Dual Sight", "Taeja", "MarineKing")
