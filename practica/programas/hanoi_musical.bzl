Hanoi |:
    HanoiMusical 5 1 2 3
:|

HanoiMusical n ori dst aux |:
    if n > 0 |:
        HanoiMusical (n - 1) ori aux dst
        (:) C + (n % 5)
        HanoiMusical (n - 1) aux dst ori
    :|
:|