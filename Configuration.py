def configurator(var):

    if var[0] == 1: # mernok1
        var[1] = var[1]

    if var[0] == 2:  # ebedlo
        var[1] = var[1]

    if var[0] == 3:  # mernok2
        var[1] = var[1]

    if var[0] == 4:  # kistargyalo
        var[1] = var[1] + 20

    if var[0] == 5:  # nagytarghyalo
        var[1] = var[1] + 10

    if var[0] == 6:  # iroda
        var[1] = var[1] + 10

    return var