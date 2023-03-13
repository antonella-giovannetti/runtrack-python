def distance_in_m(walking_number, step_height):
    cm_per_day = (walking_number * step_height) * 5 * 2
    cm_per_week = cm_per_day * 7
    result = cm_per_week / 10
    print("Pour " + str(walking_number) + " marche de " + str(step_height) + "cm, le gardien parcours " + str(result) + "m par semaine")


distance_in_m(10, 8)
