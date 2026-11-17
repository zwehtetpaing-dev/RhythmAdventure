# 0=S, 1=D, 2=F, 3=J, 4=K, 5=L
# Track Speed: ~150 BPM (400ms per beat)

BEATMAP_DATA = {
    "Boss_1": [
        # --- THE INTRO (First notes start at 2.1 seconds) ---
        # Because your speed is 0.5, these need 1.2 seconds to fall.
        # They will smoothly spawn completely off-screen at exactly 0.9 seconds!
        {"time": 2100, "lane": 1},  # 2.1s - D
        {"time": 2900, "lane": 4},  # 2.9s - K
        
        # --- THE MAIN VERSE (Every 400ms - Alternating) ---
        {"time": 3700, "lane": 0},  # 3.7s - S
        {"time": 4100, "lane": 5},  # 4.1s - L
        {"time": 4500, "lane": 1},  # 4.5s - D
        {"time": 4900, "lane": 4},  # 4.9s - K
        {"time": 5300, "lane": 2},  # 5.3s - F
        {"time": 5700, "lane": 3},  # 5.7s - J
        
        # --- THE RAPID STAIRCASE ---
        {"time": 6500, "lane": 0},  # 6.5s - S
        {"time": 6900, "lane": 1},  # 6.9s - D
        {"time": 7300, "lane": 2},  # 7.3s - F
        {"time": 7700, "lane": 3},  # 7.7s - J
        {"time": 8100, "lane": 4},  # 8.1s - K
        {"time": 8500, "lane": 5},  # 8.5s - L
        
        # --- THE BOSS CHORDS (Two notes at once) ---
        {"time": 9300, "lane": 2},  # 9.3s - F
        {"time": 9300, "lane": 3},  # 9.3s - J
        
        {"time": 10100, "lane": 1}, # 10.1s - D
        {"time": 10100, "lane": 4}, # 10.1s - K
        
        {"time": 10900, "lane": 0}, # 10.9s - S
        {"time": 10900, "lane": 5}, # 10.9s - L
    ]
}