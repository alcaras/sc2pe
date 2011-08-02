import random
import pprint

pp = pprint.PrettyPrinter(indent=4)

# player : [race, elo, vt, vz, vp]

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
           
           }

def elo(a, b):
    return 1/(1 + 10 ** ((b-a)/400))


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
       
def mass_sim(times):
    for i in range(0, times+1):
        simulate_gsl_august()
    return master

mass_sim(10000000)

pp.pprint(master)    


    


