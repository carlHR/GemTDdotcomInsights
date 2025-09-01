--------------------------------------------------------------------------------
# Gemtowerdefense.com v0.6.2 Insights

What changes from each difficulty settings:
   - Easy:     -5 armour. (Max armour possible: -5 + 18 = 13)
   - Normal:    0 armour. (Max armour possible:  0 + 18 = 18)
   - Hard:      8 armour. (Max armour possible:  8 + 18 = 26)
   - Extreme:  12 armour. (Max armour possible: 12 + 18 = 30)
   - Survival: 16 armour. (Max armour possible: 16 + 18 = 34)

--------------------------------------------------------------------------------
# Score

Each enemy increases score by 1 regardless of dificulty.
When a round ends, each difficulty increases it by: WaveLvl x DifficultyMod.
DifficultyMod is:
   - Easy:      1
   - Normal:    2
   - Hard:      4
   - Extreme:   8
   - Survival: 16



Simple Score calculator from level, assuming that you beated all enemies
during all waves and never took any damage. Open your browser console, and
type this in:

```
function scoreCalculator(waveLevel, diff=16) {
   let score = 10 * waveLevel;

   for (let i = 1; i <= waveLevel; ++i) {
      score += (diff * i);
   }

   return score;
}
```

If someone (and there is some) that got a score higher than the formula
provided, they're probably cheating. The only way to prevent cheaters imo,
would be to host the game ON THE SERVER. But realistically, who cares right.

--------------------------------------------------------------------------------
# Gem Quality

Gem quality chances are divided into: Chipped, Flawed, Normal, Flawless, 
Perfect, and Gold Upgrade to next step.
   1. 100%,  0%,  0%,  0%,  0%,  20gp
   2.  70%, 30%,  0%,  0%,  0%,  50gp
   3.  60%, 30%, 10%,  0%,  0%,  80gp
   4.  50%, 30%, 20%,  0%,  0%, 110gp
   5.  40%, 30%, 20%, 10%,  0%, 140gp
   6.  30%, 30%, 30%, 10%,  0%, 170gp
   7.  20%, 30%, 30%, 20%,  0%, 200gp
   8.  10%, 30%, 30%, 30%,  0%, 230gp
   9.   0%, 30%, 30%, 30%, 10%, -----

--------------------------------------------------------------------------------
# Gems

Status are categorized by tower quality: Chipped to Great;
Status are separated by Damage, Cooldown, Range, Info.



Amethyst (Magenta)
   1. (  8 -  13);  800; 143; Attacks air only;
   2. ( 17 -  25); 1000; 161; Attacks air only;
   3. ( 29 -  40); 1000; 179; Attacks air only;
   4. ( 59 -  75); 1000; 186; Attacks air only;
   5. (139 - 150); 1000; 215; Attacks air only;
   6. (349 - 400); 1000; 236; Attacks air only;



Aquamarine (Cyan)
   1. (  5 -   8); 350; 50; Fast attack speed;
   2. ( 11 -  15); 350; 52; Fast attack speed;
   3. ( 23 -  30); 350; 54; Fast attack speed;
   4. ( 47 -  55); 350; 61; Fast attack speed;
   5. ( 99 - 120); 350; 79; Fast attack speed;
   6. (279 - 280); 350; 86; Fast attack speed;



Diamond (White)
   1. (  7 -  12);  800;  72; Ground only. Has 25% chance to deal 2x damage;
   2. ( 15 -  18); 1000;  79; Ground only. Has 25% chance to deal 2x damage;
   3. ( 29 -  37); 1000;  86; Ground only. Has 25% chance to deal 2x damage;
   4. ( 57 -  65); 1000;  93; Ground only. Has 25% chance to deal 2x damage;
   5. (139 - 150); 1000; 107; Ground only. Has 25% chance to deal 2x damage;
   6. (299 - 350); 1000; 122; Ground only. Has 25% chance to deal 2x damage;



Emerald (Green)
   1. (  3 -   7); 1000;  72; Applies effects for 3s: 15% slow, 2 poison dmg/s;
   2. (  9 -  13); 1000;  79; Applies effects for 4s: 20% slow, 3 poison dmg/s;
   3. ( 14 -  25); 1000;  86; Applies effects for 5s: 25% slow, 5 poison dmg/s;
   4. ( 29 -  38); 1000; 100; Applies effects for 6s: 35% slow, 8 poison dmg/s;
   5. ( 79 -  90); 1000; 114; Applies effects for 8s: 50% slow, 16 poison dmg/s;
   6. (199 - 240); 1000; 129; Applies effects for 20s: 75% slow, 
      25 poison dmg/s;



Opal (Dark)
   1. (  4 -   5);  800;  86; Attack speed aura +10%. Effect doesn't stack;
   2. (  9 -  10); 1000; 100; Attack speed aura +15%. Effect doesn't stack;
   3. ( 19 -  20); 1000; 114; Attack speed aura +20%. Effect doesn't stack;
   4. ( 39 -  40); 1000; 129; Attack speed aura +25%. Effect doesn't stack;
   5. ( 84 -  85); 1000; 143; Attack speed aura +35%. Effect doesn't stack;
   6. (179 - 180); 1000; 215; Attack speed aura +50%. Effect doesn't stack;



Ruby (Red)
   1. (  7 -   9); 1000; 114; Attacks cause splash damage;
   2. ( 12 -  16); 1000; 114; Attacks cause splash damage;
   3. ( 19 -  25); 1000; 114; Attacks cause splash damage;
   4. ( 37 -  45); 1000; 114; Attacks cause splash damage;
   5. ( 79 - 104); 1000; 129; Attacks cause splash damage;
   6. (139 - 140);  750; 129; Attacks cause splash damage;



Sapphire (Blue)
   1. (  4 -   8); 1000;  72; Attacks slow target's movement speed;
   2. (  9 -  13); 1000; 107; Attacks slow target's movement speed;
   3. ( 15 -  21); 1000; 114; Attacks slow target's movement speed;
   4. ( 29 -  40); 1000; 122; Attacks slow target's movement speed;
   5. ( 59 -  75); 1000; 200; Attacks slow target's movement speed;
   6. (199 - 200); 1000; 286; Attacks slow target's movement speed;



Topaz (Yellow)
   1. (  3 -   4);  800;  72; Attacks 3 targets;
   2. (  7 -   8); 1000;  72; Attacks 3 targets;
   3. ( 13 -  14); 1000;  72; Attacks 4 targets;
   4. ( 24 -  25); 1000;  72; Attacks 4 targets;
   5. ( 74 -  75); 1000;  86; Attacks 5 targets;
   6. (249 - 250); 1000; 100; Attacks 7 targets;

--------------------------------------------------------------------------------
# Towers

Each tower is categorized from the tower name, and its corresponding recipe.
Each tower status is divided into: Damage, Attack Speed, Range, Upgrade Cost, 
Effect Description.
Each number corresponds to the tower upgrade level in sequence.



Malachite: (Chipped:Opal + Chipped:Aquamarine + Chipped:Emerald)
   1. ( 5 -  6); 350; 107; 25gp; Attack 3x targets;
   2. (10 - 11); 350; 114; 280gp; Attack 4x targets;
   3. (44 - 45); 350; 114; -----; Attack all targets;



Silver: (Chipped:Topaz + Chipped:Sapphire + Chipped:Diamond)
   1. ( 19 -  21); 1000; 79; 25gp; Silver attacks slow targets with splash area;
   2. ( 39 -  40); 1000; 93; 300gp; Sterling Silver attacks slow targets with 
      splash area;
   3. (149 - 150); 1000; 107; Silver Knight attacks slow targets with splash 
      area;



StarRuby: (Chipped:Amethyst + Chipped:Ruby + Flawed:Ruby)
   1. ( 10 - 11); 250; 38; 30gp; Any enemy within 37.895 range will receive 
      40 dmg/s.
   2. ( 12 - 13); 250; 72; 290gp; Any enemy within 71.500 range will receive 
      50 dmg/s.
   3. ( 64 - 65); 500; 86; -----; Any enemy within 85.800 range will receive 
      100 dmg/s.



PinkDiamond: (Perfect:Diamond + Normal:Diamond + Normal:Topaz)
   1. (149 - 175); 750; 114; 175gp; Attacks ground only. Has 10% chance to
      deal 5x damage. 
   2. (174 - 195); 650; 122; -----; Attacks ground only. Has 10% chance to
      deal 8x damage.



Jade: (Perfect:Emerald + Flawless:Sapphire + Flawed:Topaz)
   1. (29 - 35); 500; 114;  45gp; Applies effects for 2s: Slow 50%, 5 poison
      dmg/s.
   2. (49 - 50); 500; 114; 250gp; Applies effects for 3s: Slow 50%, 10 poison 
      dmg/s.
   3. (54 - 55); 350; 122; -----; Applies effects for $s: Slow 50%, 10 poison 
      dmg/s. 5% chance to deal 4x damage. 1% chance to stun. 5% chance to gain 
      gold on hit.



RedCrystal: (Flawless:Emerald + Normal:Ruby + Flawed:Amethyst)
   1. (49 -  75); 800; 186; 100gp; Gives -4 armour to air units within large 
      area. Can only attack air units.
   2. (74 - 100); 800; 200; 100gp; Gives -5 armour to air units within large 
      area. Can only attack air units.
   3. (99 - 125); 800; 215; -----; Gives -6 armour to air units within large 
      area. Can only attack air units.



Gold: (Perfect:Amethyst + Flawless:Amethyst + Flawed:Diamond)
   1. (159 - 190); 1000; 114; 210gp; 25% chance to deal 2x damage. Applies -5 
      armour to targets it attacks;
   2. (159 - 200);  750; 114; -----; 30% chance to deal 2x damage. Applies -8 
      armour to targets it attacks;



ParaibaTourmaline: (Perfect:Aqua + Flawless:Opal + Flawed:Emerald + Flawed:Aqua)
   1. (25 - 105); 850; 112; 350gp; Gives -4 armour to ground units within 86 
      range. Has 33% chance to cast 100 damage frost nova.
   2. (125 - 204); 680; 129; -----; Gives -6 armour to ground units within 93 
      range; Has 33% chance to cast 125 damage frost nova.



BlackOpal: (Perfect:Opal + Flawless:Diamond + Normal:Aquamarine)
   1. (24 - 25); 1000; 114; 300gp; Gives 30% more damage to towers within 143 
      range;
   2. (49 - 50); 1000; 143; -----; Gives 40% more damage to towers within 171 
      range;



DarkEmerald: (Perfect:Emerald + Flawless:Sapphire + Flawed:Topaz)
   1. (89 - 150); 800; 79; 250gp; Has 12.5% chance to stun for 1 second per 
      attack;
   2. (98 - 200); 700; 100; -----; Has 15.0% chance to stun for 2 seconds per 
      attack;



Uranium-235: (Perfect:Topaz + Normal:Sapphire + Flawed:Opal)
   1. (47 - 48); 250; 64; 190gp; Slows all targets by 50%. Burn enemies for 190 
      dmg/s.
   2. (64 - 65); 250; 86; -----; Slows all targets by 50%. Burn enemies for 260 
      dmg/s.



YellowSapphire: (Perfect:Sapphire + Flawless:Topaz + Flawless:Ruby)
   1. (99 - 100); 1000; 114; 210gp; Attacks slow targets within a huge splash
      area.
   2. (99 - 100); 1000; 114; -----gp; Attacks slow targets within a huge splash
      area. Provides 5% damage bonus to nearby towers.



BloodStone: (Perfect:Ruby + Flawless:Aquamarine + Normal:Ruby)
   1. ( 67 -  68); 500; 100; 310gp; Attacks 10 targets. Does 135 damage per
      second to nearby enemies and has splash damage.
   2. (159 - 240); 800; 100; -----; 15% chance to deal 3x damage. Possess 10
   mana points, and restores 2 mp/s. Has 10% chance to cast Flame Strike spell,
   which costs 5 mp. It lasts 10s, dealing 100 damage each second (that's
   what the script does, at least).



UberStone: 4x Perfect Gems of same type
   1. (500 - 2500); 500; 215; -----; Has 25% chance to deal 4x damage. Only the 
   very luck have the chance ever to this stone of pure damage.

--------------------------------------------------------------------------------
# Waves

From observation, we get 10 gold. 
When a wave finishes, we gain 9gp, and this amount increases by +2gp each 
subsequent wave.
Enemies rewards start at 1.25gp, and at each wave, the reward increases by 
+0.25gp.



Information below was extracted from the game's source code. 
It was too complex to make it by experimentation.



For better reading, either resize the page to contain the full info, or, copy
and paste the entire text into a text-editor of preference (ftlog, not Word).
Disable wrap mode. Have fun.



Enemy Status (All Difficulty Modes):
   1.  Axedwarf; Topaz;         10 hp;  0 armour; 100.00% speed;  1.25 gold; 
   2.  Axedwarf; Aquamarine;    30 hp;  0 armour; 100.00% speed;  1.50 gold; 
   3.  Axedwarf; Diamond;       55 hp;  0 armour; 100.00% speed;  1.75 gold; 
   4.  Batman;   Amethyst;      70 hp;  0 armour;  86.79% speed;  2.00 gold; 
   5.  Axedwarf; Emerald;       90 hp;  0 armour; 103.77% speed;  2.25 gold; 
   6.  Axedwarf; Emerald;      120 hp;  0 armour; 103.77% speed;  2.50 gold; 
   7.  Axedwarf; Amethyst;     178 hp;  0 armour; 107.55% speed;  2.75 gold; 
   8.  Batman;   Amethyst;     240 hp;  0 armour;  86.79% speed;  3.00 gold; 
   9.  Axedwarf; Diamond;      300 hp;  0 armour; 107.55% speed;  3.25 gold; 
   10. Axedwarf; Sapphire;     470 hp;  1 armour; 107.55% speed;  3.50 gold; 
   11. Axedwarf; Emerald;      490 hp;  1 armour; 107.55% speed;  3.75 gold; 
   12. Batman;   Amethyst;     450 hp;  1 armour;  94.34% speed;  4.00 gold; 
   13. Axedwarf; Topaz;        570 hp;  1 armour; 111.32% speed;  4.25 gold; 
   14. Axedwarf; Aquamarine;   650 hp;  1 armour; 111.32% speed;  4.50 gold; 
   15. Axedwarf; Ruby;        1000 hp;  0 armour; 111.32% speed;  4.75 gold; 
   16. Batman;   Amethyst;     725 hp;  1 armour;  94.34% speed;  5.00 gold; 
   17. Axedwarf; Ruby;        1350 hp;  1 armour; 111.32% speed;  5.25 gold; 
   18. Axedwarf; Amethyst;    1550 hp;  1 armour; 113.21% speed;  5.50 gold; 
   19. Axedwarf; Sapphire;    1950 hp;  1 armour; 113.21% speed;  5.75 gold; 
   20. Batman;   Amethyst;    1350 hp;  1 armour; 105.66% speed;  6.00 gold; 
   21. Axedwarf; Diamond;     2300 hp;  2 armour; 118.87% speed;  6.25 gold; 
   22. Axedwarf; Emerald;     2530 hp;  2 armour; 118.87% speed;  6.50 gold; 
   23. Axedwarf; Ruby;        3000 hp;  2 armour; 113.21% speed;  6.75 gold; 
   24. Batman;   Amethyst;    2500 hp;  1 armour; 105.66% speed;  7.00 gold; 
   25. Axedwarf; Ruby;        3750 hp;  2 armour; 126.42% speed;  7.25 gold;  37.74% min-speed;
   26. Axedwarf; Emerald;     4500 hp;  2 armour; 128.30% speed;  7.50 gold;  45.28% min-speed;
   27. Axedwarf; Sapphire;    5000 hp;  2 armour; 128.30% speed;  7.75 gold;  52.83% min-speed;
   28. Batman;   Amethyst;    4150 hp;  2 armour; 103.77% speed;  8.00 gold;  37.74% min-speed;
   29. Axedwarf; Diamond;     6750 hp;  2 armour; 130.19% speed;  8.25 gold;  60.38% min-speed;
   30. Axedwarf; Emerald;     7150 hp;  3 armour; 132.08% speed;  8.50 gold;  67.92% min-speed;
   31. Axedwarf; Aquamarine;  8000 hp;  3 armour; 132.08% speed;  8.75 gold;  75.47% min-speed;
   32. Batman;   Amethyst;    6250 hp;  2 armour; 120.75% speed;  9.00 gold;  56.60% min-speed;
   33. Axedwarf; Ruby;        9550 hp;  3 armour; 133.96% speed;  9.25 gold;  83.02% min-speed;
   34. Axedwarf; Topaz;      10200 hp;  3 armour; 133.96% speed;  9.50 gold;  90.57% min-speed;
   35. Axedwarf; Sapphire;   11500 hp;  3 armour; 133.96% speed;  9.75 gold;  98.11% min-speed;
   36. Batman;   Amethyst;    8500 hp;  2 armour; 120.75% speed; 10.00 gold;  75.47% min-speed;
   37. Axedwarf; Topaz;      13000 hp;  3 armour; 135.85% speed; 10.25 gold; 105.66% min-speed;
   38. Axedwarf; Ruby;       15000 hp;  3 armour; 137.74% speed; 10.50 gold; 113.21% min-speed;
   39. Axedwarf; Diamond;    17000 hp;  3 armour; 141.51% speed; 10.75 gold; 120.75% min-speed;
   40. Batman;   Amethyst;   10500 hp;  2 armour; 132.08% speed; 11.00 gold;  94.34% min-speed;
   41. Axedwarf; Emerald;    19500 hp;  7 armour; 143.40% speed; 11.25 gold; 
   42. Axedwarf; Sapphire;   23000 hp; 18 armour; 147.17% speed; 16.00 gold;
   43. Axedwarf; Topaz;      26000 hp; 15 armour; 150.94% speed; 16.00 gold;
   44. Batman;   Amethyst;   13000 hp;  5 armour; 139.62% speed; 16.00 gold;
   45. Axedwarf; Ruby;       28500 hp; 15 armour; 150.94% speed; 18.00 gold;
   46. Axedwarf; Aquamarine; 30000 hp; 15 armour; 150.94% speed; 18.00 gold;
   47. Axedwarf; Diamond;    33000 hp; 15 armour; 150.94% speed; 18.00 gold;
   48. Batman;   Amethyst;   15000 hp;  5 armour; 143.40% speed; 20.00 gold;
   49. Axedwarf; Emerald;    35000 hp; 15 armour; 150.94% speed; 20.00 gold;
   50. Axedwarf; Emerald;    40000 hp; 15 armour; 150.94% speed; 20.00 gold;



Extreme Difficulty Changes:
   1. (Just to make a list. Markdown requires to insert 1.)
   11. Axedwarf;   600 hp;
   12. Batman;           ;
   13. Axedwarf;   700 hp;
   14. Axedwarf;   800 hp;
   15. Axedwarf;  1200 hp;
   16. Batman;           ;
   17. Axedwarf;  1450 hp; 122.64% speed;  37.74% min-speed;
   18. Axedwarf;  1850 hp; 122.64% speed;  41.51% min-speed;
   19. Axedwarf;  2350 hp; 132.08% speed;  45.28% min-speed;
   20. Batman;           ;              ;  37.74% min-speed;
   21. Axedwarf;  3150 hp; 150.94% speed;  52.83% min-speed;
   22. Axedwarf;  3500 hp; 158.49% speed;  60.38% min-speed;
   23. Axedwarf;  4300 hp; 166.04% speed;  67.92% min-speed;
   24. Batman;           ;              ;  52.83% min-speed;
   25. Axedwarf;  5250 hp; 164.15% speed;  75.47% min-speed;
   26. Axedwarf;  6300 hp; 166.04% speed;  83.02% min-speed;
   27. Axedwarf;  7900 hp; 167.92% speed;  90.57% min-speed;
   28. Batman;           ;              ;  60.38% min-speed;
   29. Axedwarf;  9000 hp; 169.81% speed;  98.11% min-speed;
   30. Axedwarf; 11000 hp; 171.70% speed; 105.66% min-speed;
   31. Axedwarf; 12750 hp; 173.58% speed; 113.21% min-speed;
   32. Batman;           ;              ;  67.92% min-speed;
   33. Axedwarf; 14500 hp; 175.47% speed; 116.98% min-speed;
   34. Axedwarf; 16500 hp; 177.36% speed; 120.75% min-speed;
   35. Axedwarf; 19000 hp; 179.25% speed; 124.53% min-speed;
   36. Batman;           ;              ;                  ;
   37. Axedwarf; 21000 hp; 181.13% speed; 128.30% min-speed;
   38. Axedwarf; 23000 hp; 183.02% speed; 132.08% min-speed;
   39. Axedwarf; 25000 hp; 184.91% speed; 135.85% min-speed;
   40. Batman;             128.30% speed;  83.02% min-speed; for some reason, this wave is easier on this difficulty.



Survival Difficulty Changes:
   1. (Just to make a list. Markdown requires to insert 1.)
   11. Axedwarf;   650 hp;
   12. Batman;     550 hp;
   13. Axedwarf;   800 hp;
   14. Axedwarf;   925 hp;
   15. Axedwarf;  1350 hp;
   16. Batman;     850 hp;
   17. Axedwarf;  1650 hp; 122.64% speed;  37.74% min-speed;
   18. Axedwarf;  2000 hp; 122.64% speed;  41.51% min-speed;
   19. Axedwarf;  2500 hp; 132.08% speed;  45.28% min-speed;
   20. Batman;    1550 hp;              ;  37.74% min-speed;
   21. Axedwarf;  3250 hp; 150.94% speed;  52.83% min-speed;
   22. Axedwarf;  4100 hp; 158.49% speed;  60.38% min-speed;
   23. Axedwarf;  5000 hp; 166.04% speed;  67.92% min-speed;
   24. Batman;    2850 hp;              ;  52.83% min-speed;
   25. Axedwarf;  6250 hp; 164.15% speed;  75.47% min-speed;
   26. Axedwarf;  7750 hp; 166.04% speed;  83.02% min-speed;
   27. Axedwarf;  9500 hp; 167.92% speed;  90.57% min-speed;
   28. Batman;    5000 hp;              ;  56.60% min-speed;
   29. Axedwarf; 10500 hp; 169.81% speed; 105.66% min-speed;
   30. Axedwarf; 13000 hp; 171.70% speed; 113.21% min-speed;
   31. Axedwarf; 16000 hp; 173.58% speed; 116.98% min-speed;
   32. Batman;    7500 hp;              ;  60.38% min-speed;
   33. Axedwarf; 19500 hp; 175.47% speed; 120.75% min-speed;
   34. Axedwarf; 23500 hp; 177.36% speed; 124.53% min-speed;
   35. Axedwarf; 28000 hp; 179.25% speed; 128.30% min-speed;
   36. Batman;   10000 hp; 132.08% speed;
   37. Axedwarf; 32000 hp; 181.13% speed; 132.08% min-speed;
   38. Axedwarf; 38000 hp; 183.02% speed; 135.85% min-speed;
   39. Axedwarf; 45000 hp; 184.91% speed; 139.62% min-speed;
   40. Batman;   13500 hp; 143.40% speed;
   - Waves 41+:
      - Enemies have 45000 base hp. At each wave starting from 41 onwards, they increase the hp by 10%.
         - So, on wave 41, they get 110% x 45000 hp = 49500.
         -     on wave 42, they get 120% x 45000 hp = 54000.
         -     on wave 50, they get 200% x 45000 hp = 90000.
         - and so on...
      - At each 4th wave (flying wave), their max hp decreases to 1/3.
      - At each 50th wave, enemies are immune to stun.
      - Armor is set to 3.
      - Weakness is set to Amethyst.
      - Speed is set to 207.55%
      - Minimum Speed is set to 147.17%
      - Rewards 25 gold when defeated

--------------------------------------------------------------------------------
# Questions I had, and solved by inspecting the code by myself

I mean, this is not written anywhere afaik, besides by carefully reading the 
source code. So, I'll document it here.



How RNG works?
   - Read about `xorshift`. I did had my doubts about this... Yes, some of you 
     might be cheating with this one! Just set a known seed and voila! Its not
     random anymore.



How Armor and Damage calculation actually works?
   - First, the game ONLY IMPLEMENTS AMETHYST weakness. Yes, its described that 
     certain mobs have Sapphire weakness, or Ruby, but they don't. It's only 
     Amethyst that's implemented on the game, and it matters because all waves 
     from 41+ have Amethyst weakness. So here's how it works:
      - If the enemy is weak to Amethyst, and the tower is Amethyst, it receives 
        175% damage.
      - If the enemy is weak to Amethyst, and the tower is not Amethyst, it 
        receives 80% damage.
      - If the enemy is not weak to Amethyst, the tower type doesn't matter. 
        Damage multiplier is 100%.
   - Armor caps from -10 to +35, based on the armor tables.
      - If armor is between (-10, -1), then the modifier is between 
        (146.10%, 106.00%);
      - If armor is between (  0, 35), then the modifier is between 
        (100.00%,  32.30%); "aka aprox 1/3 of damage"
      - For example:
         - Enemies with  0 armor will receive 100.00% damage;
         - Enemies with  5 armor will receive  80.60% damage;
         - Enemies with 10 armor will receive  64.90% damage;
         - Enemies with 16 armor will receive  52.60% damage;
         - Enemies with 20 armor will receive  46.70% damage;
   - Tower Level above 1 increases damage by +10%. So, a tower of level 2 deals 
     +10%, while a tower of level 6 deals +50%. 
   - Damage auras (BlackOpal, StarSapphire) don't stack. There's no need to 
     place multiple of them nearby.
   - Critical Damage is applied last, after all reductions. So the number 
     displayed on red, is the real damage being dealt to the enemy.
   - The steps to calculate damage are:
      - `(BaseDamage x {WeaknessModifier} x {ArmorModifier} x {TowerLevel}) x {AuraDamageModifier} x {CritDamageModifier}.`



What are the gem-types of each tower, to counter enemies weaknesses?
   - Gold:                   Amethyst    <-- end game towers
   - EgyptianGold:           Amethyst    <-- end game towers
   - UberStone:              Amethyst    <-- end game towers (good luck though)
   - RedCrystal:             Amethyst    <-- end game towers
   - RedCrystalFacet:        Amethyst    <-- end game towers
   - RoseQuartzCrystal:      Amethyst    <-- end game towers
   - Jade:                   Aquamarine
   - AsianJade:              Aquamarine
   - LuckyAsianJade:         Aquamarine
   - ParaibaTourmaline:      Aquamarine
   - ParaibaTourmalineFacet: Aquamarine
   - Malachite:              Emerald
   - VividMalachite:         Emerald
   - MightyMalachite:        Emerald
   - DarkEmerald:            Emerald
   - EnchantedEmerald:       Emerald
   - PinkDiamond:            Diamond
   - GreatPinkDiamond:       Diamond
   - BlackOpal:              Opal
   - MysticBlackOpal:        Opal
   - BloodStone:             Ruby
   - AncientBloodStone:      Ruby
   - StarRuby:               Ruby
   - BloodStar:              Ruby
   - FireStar:               Ruby
   - YellowSapphire:         Sapphire
   - StarYellowSapphire:     Sapphire
   - Silver:                 Sapphire
   - SterlingSilver:         Sapphire
   - SilverKnight:           Sapphire
   - Uranium235:             Topaz
   - Uranium238:             Topaz
