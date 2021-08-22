# The Simp City - NP ASG  PRG I
Ngee Ann Polytechnic - Programming I (PRG I) Assignment 

## Usage

Program main entrance are at Main.py. 

```powershell
> py {*relative path*}/Main.py
```

---

## Objective

You're the mayor of Simp City, and your goal is to make your city the happy and wealthiest it can be, i.e. score the most points.

This city-building strategy game takes {row}*{col} turns to complete. In your {row}x{col} city, you will build one of 2 randomly picked structures each turn. You can build anyplace in the city in the 1st turn. You can only build on squares that are connected to existing buildings in subsequent turns. The other structure, which you did not construct, is discarded.

Each structure receives a separate score. The goal of the game is to create a city with as many points as possible.

---

## Features

- 7 buildings in total, (BCH, FAC, HSE, SHP, HWY, PRK, MON)
- Choose building pool, (an option to allow the player to choose which 5 building to use during a single game)
- Always show remaining building at the right side of the screen
- Customize the city size, for example 4x4, 5x6, 7x8



Documentation are as follow of PEP257 guideline.

---

## Introduction to Game

### Main menu

```
Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game
3. Show highest scores
```

### High Scores  (Option 3)

```
-----------HIGH SCORES---------------
Size  Pos  Player               Score
----  ---  ------               -----
4*4   1    Never                56
4*4   2    Gonna                53
4*4   3    Give                 52
4*4   4    You                  52
4*4   5    Up                   51
4*4   6    Gonna                50
4*4   7    cOSMI                50
4*4   8    cOS                  50
4*4   9    Cosmi                50
5*5   1    Never                56
5*5   2    Gonna                53
5*5   3    Give                 52
5*5   4    You                  52
5*5   5    Up                   51
5*5   6    Gonna                50
5*5   7    Let                  49
5*5   8    You                  49
5*5   9    Down                 48
6*6   1    Never                56
6*6   2    Gonna                53
6*6   3    Give                 52
6*6   4    You                  52
6*6   5    Up                   51
6*6   6    Gonna                50
6*6   7    Let                  49
6*6   8    You                  49
6*6   9    Down                 48

-------------------------------------
```

### New game (Option 1)

```
Please indicate how many [ row  ] to be generated: 4
Please indicate how many [column] to be generated: 4
No.  Type
---  ----
1.   BCH
2.   FAC
3.   HSE
4.   SHP
5.   HWY
6.   PRK
7.   MON
```

### In game

```
Turn 1
+-----+-----+-----+-----+-----+                                             Building       Remaining
|     |  A  |  B  |  C  |  D  |                                             --------       ---------
+-----+-----+-----+-----+-----+                                             PRK            7
|  1  |     |     |     |     |                                             MON            7
+-----+-----+-----+-----+-----+                                             HWY            7
|  2  |     |     |     |     |                                             SHP            7
+-----+-----+-----+-----+-----+                                             HSE            7
|  3  |     |     |     |     |
+-----+-----+-----+-----+-----+
|  4  |     |     |     |     |
+-----+-----+-----+-----+-----+
1. Build a HWY
2. Build a HWY
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu
```

### See Current Score

```
Turn 16
+-----+-----+-----+-----+-----+                                             Building       Remaining
|     |  A  |  B  |  C  |  D  |                                             --------       ---------
+-----+-----+-----+-----+-----+                                             SHP            4
|  1  | SHP | SHP | HSE | FAC |                                             HSE            2
+-----+-----+-----+-----+-----+                                             FAC            6
|  2  | BCH | HSE | HSE | BCH |                                             BCH            4
+-----+-----+-----+-----+-----+                                             HWY            4
|  3  | BCH | SHP | HSE | HSE |
+-----+-----+-----+-----+-----+
|  4  | HWY | HWY | HWY |     |
+-----+-----+-----+-----+-----+
1. Build a SHP
2. Build a SHP
3. See remaining buildings
4. See current score

5. Save game
0. Exit to main menu
Your choice? 4

HSE: 1 + 5 + 5 + 3 + 3 = 17
FAC: 1 = 1
SHP: 2 + 2 + 3 = 7
HWY: 3 + 3 + 3 = 9
BCH: 3 + 3 + 3 = 9
PRK:  = 0
MON:  = 0
Total = 43
```

---

## Scores

### Beach  (BCH)

> If a beach (BCH) is created in column A or column D, it receives 3 points; otherwise, it receives 1 point.
>
> ```
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | FAC |                                             HSE            3
> +-----+-----+-----+-----+-----+                                             FAC            6
> |  2  | BCH | HSE | HSE | BCH |                                             BCH            3
> +-----+-----+-----+-----+-----+                                             HWY            3
> |  3  | BCH | SHP | BCH | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | HWY | HWY | HWY | HWY |
> +-----+-----+-----+-----+-----+
> 
> BCH: 3 + 3 + 3 + 1 = 10
> 
> BCH at A2: 3 pts
> BCH at D2: 3 pts
> BCH at A3: 3 pts
> BCH at C3: 1 pts
> ```



### Factory (FAC)

> A Factory (FAC) receives one point for each factory (FAC) in the city, up to a maximum of 4 points for the first four factories; subsequent factories receive just one point. For example:
>
> - If the city has three factories, each will receive 3 points, for a total of 3+3+3 = 9 points.
> - If the city has 5 factories, the first four will receive 4 points each, while the 5th will receive 1 point, for a total of 4+4+4+4+1 = 17 points.
>
> ```
> # When there are only 1 factory in the city.
> 
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | FAC |                                             HSE            2
> +-----+-----+-----+-----+-----+                                             FAC            6
> |  2  | BCH | HSE | HSE | BCH |                                             BCH            4
> +-----+-----+-----+-----+-----+                                             HWY            3
> |  3  | BCH | SHP | HSE | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | HWY | HWY | HWY | HWY |
> +-----+-----+-----+-----+-----+
> 
> FAC: 1 = 1
> 
> FAC at D1.
> ```
>
> ```
> # When there are 4 factory in the city.
> 
> +-----+-----+-----+-----+-----+                                             Building       Remaining      
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | FAC |                                             HSE            3
> +-----+-----+-----+-----+-----+                                             FAC            3
> |  2  | FAC | HSE | FAC | BCH |                                             BCH            5
> +-----+-----+-----+-----+-----+                                             HWY            4
> |  3  | BCH | SHP | HSE | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | HWY | HWY | FAC | HWY |
> +-----+-----+-----+-----+-----+
> 
> FAC: 4 + 4 + 4 + 4 = 16
> 
> FAC at D1, A2, C2, C4.
> ```
>
> ```
> # When there are 5 factory in the city.
> 
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | FAC |                                             HSE            3
> +-----+-----+-----+-----+-----+                                             FAC            2
> |  2  | FAC | HSE | FAC | BCH |                                             BCH            5
> +-----+-----+-----+-----+-----+                                             HWY            5
> |  3  | BCH | SHP | HSE | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | FAC | HWY | FAC | HWY |
> +-----+-----+-----+-----+-----+
> 
> FAC: 4 + 4 + 4 + 4 + 1 = 17
> 
> FAC at D1, A2, C2, A4, C4.
> ```



### House  (HSE)

> If a house (HSE) is located adjacent to a factory (FAC), it receives only 1 point. Otherwise, each nearby house (HSE) or business (SHP) receives 1 point, and each adjacent beach receives 2 points (BCH).
>
> ** Only FAC, HSE, SHP are identified when calculating the score for house, the rest of the building are ignored.
>
> ```
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | FAC |                                             HSE            2
> +-----+-----+-----+-----+-----+                                             FAC            6
> |  2  | BCH | HSE | HSE | BCH |                                             BCH            4
> +-----+-----+-----+-----+-----+                                             HWY            3
> |  3  | BCH | SHP | HSE | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | HWY | HWY | HWY | HWY |
> +-----+-----+-----+-----+-----+
> 
> HSE: 1 + 5 + 5 + 3 + 3 = 17
> 
> HSE at C1: 1 pts, where => 1 (FAC, right) # 1 factory found at the right side, it only score 1 pts
> HSE at B2: 5 pts, where => 1 (SHP, Above) + 1 (SHP, Bottom) + 2 (BCH, Left) + 1 (HSE, Right)
> HSE at C2: 5 pts, where => 1 (HSE, Above) + 1 (HSE, Bottom) + 1 (HSE, Left) + 2 (BCH, Right)
> HSE at C3: 3 pts, where => 1 (HSE, Above) + 1 (SHP, Left) + 1 (HSE, right)
> HSE at C4: 3 pts, where => 2 (BCH, Above) + 1 (HSE, Left)
> ```

### Shop (SHP)

> A Shop (SHP) scores 1 point per different type of building adjacent to it
>
> ** Same type of adjacent building are ignored.
>
> ```
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | FAC |                                             HSE            2
> +-----+-----+-----+-----+-----+                                             FAC            6
> |  2  | BCH | HSE | HSE | BCH |                                             BCH            4
> +-----+-----+-----+-----+-----+                                             HWY            3
> |  3  | BCH | SHP | HSE | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | HWY | HWY | HWY | HWY |
> +-----+-----+-----+-----+-----+
> 
> SHP: 2 + 2 + 3 = 7
> 
> SHP at A1: 2 pts, where => 1 (BCH, Bottom) + 1 (SHP, Right)
> SHP at B1: 2 pts, where => 1 (HSE, Bottom) + 1 (SHP, Left) # HSE located at the right side are ignored.
> SHP at B3: 3 pts, where => 1 (HSE, Above) + 1 (HWY, Bottom) + 1 (BCH, Left)
> ```

### Highway (HWY)

> For each connected highway (HWY) in the same row (not column), a highway (HWY) receives 1 point.
>
> ```
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            6
> |  1  | SHP | HWY | HSE | FAC |                                             HWY            0
> +-----+-----+-----+-----+-----+                                             HSE            3
> |  2  | BCH | HSE | HSE | BCH |                                             FAC            6
> +-----+-----+-----+-----+-----+                                             BCH            4
> |  3  | BCH | HWY | HWY | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | HWY | HWY | HWY | HWY |
> +-----+-----+-----+-----+-----+
> 
> HWY: 1 + 2 + 2 + 4 + 4 + 4 + 4 = 21
> 
> HWY at B1: 1 pts
> HWY at B3, C3: 2 pts each, where => HWY B3, C3 are connected.
> HWY at A4, B4, C4, D4: 4 pts each, where => HWY A4, B4, C4, D4 are connected.
> ```

### Park  (PRK)

> The score for the park is calculated based on the number of parks that are connected to one another (both horizontally and vertically). The table below shows how a Park's score is determined.
>
> | Size      | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 8+        |
> | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --------- |
> | **Score** | 1    | 3    | 8    | 16   | 22   | 23   | 24   | 25   | 17 + size |
>
> ** Note that the above number is for the entire Park, not for each individual Park building; so, a 4-square Park receives a total score of 16, not 16 for each individual building.
>
> ```
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            6
> |  1  | SHP | PRK | HSE | HSE |                                             PRK            1
> +-----+-----+-----+-----+-----+                                             HSE            3
> |  2  | PRK | PRK | HSE | PRK |                                             MON            5
> +-----+-----+-----+-----+-----+                                             HWY            4
> |  3  | MON | HWY | HWY | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | PRK | PRK | MON | HWY |
> +-----+-----+-----+-----+-----+
> 
> PRK: 8 + 1 + 3 = 12
> 
> PRK for 'island park B1, A2, B2: Total 8 pts.
> PRK for 'island park D2: Total 1 pts.
> PRK for 'island park A4, B4: Total 3 pts.
> ```

### Monument (MON)

> It receives 1 point if it is not constructed on a corner square (i.e., A1, A4, D1 or D4). It is worth 2 points if it is built on a corner square. If the city has at least 3 monuments built on corner squares, each one receives 4 points (including those that are not built on corner squares)
>
> ```
> When no MON found at the corner of the city.
> 
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            6
> |  1  | SHP | PRK | HSE | HSE |                                             PRK            1
> +-----+-----+-----+-----+-----+                                             HSE            3
> |  2  | PRK | PRK | HSE | PRK |                                             MON            5
> +-----+-----+-----+-----+-----+                                             HWY            4
> |  3  | MON | HWY | HWY | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | PRK | PRK | MON | HWY |
> +-----+-----+-----+-----+-----+
> 
> MON: 1 + 1 = 2
> 
> MON at A3, C4: 1 pts each
> ```
>
> ```
> When 0 < x <= 2 MON found at the corner of the city. In this case 2 MON found at the corner of the city.
> 
> +-----+-----+-----+-----+-----+                                             Building       Remaining
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | MON |                                             HSE            3
> +-----+-----+-----+-----+-----+                                             MON            3
> |  2  | BCH | HSE | MON | BCH |                                             BCH            4
> +-----+-----+-----+-----+-----+                                             HWY            5
> |  3  | BCH | SHP | HSE | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | HWY | MON | HWY | MON |
> +-----+-----+-----+-----+-----+
> 
> MON: 2 + 2 + 1 + 1 = 6
> 
> MON at D1, D4: 2 pts each
> MON at C3, B4: 1 pts each
> ```
>
> ```
> When x >= 3 MON found at the corner of the city. IN this case 3 MON found ath the corner of the city.
> 
> +-----+-----+-----+-----+-----+                                             Building       Remaining      
> |     |  A  |  B  |  C  |  D  |                                             --------       ---------
> +-----+-----+-----+-----+-----+                                             SHP            4
> |  1  | SHP | SHP | HSE | MON |                                             HSE            3
> +-----+-----+-----+-----+-----+                                             MON            2
> |  2  | BCH | HSE | MON | BCH |                                             BCH            4
> +-----+-----+-----+-----+-----+                                             HWY            6
> |  3  | BCH | SHP | HSE | HSE |
> +-----+-----+-----+-----+-----+
> |  4  | MON | MON | HWY | MON |
> +-----+-----+-----+-----+-----+
> 
> MON: 4 + 4 + 4 + 4 + 4 = 20
> 
> MON at the 3 corner: D1, A4, D4
> MON not at the corner: C2, B4
> 
> Total count of MON = 5
> 
> Since there are atleast 3 MON located at the corner of the city, all Monument score 4 pts.
> ```
>
> 
