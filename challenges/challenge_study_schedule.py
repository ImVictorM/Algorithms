def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    people_present_in_target_time = 0

    for entry_time, exit_time in permanence_period:
        if isinstance(entry_time, int) and isinstance(exit_time, int):
            if entry_time <= target_time <= exit_time:
                people_present_in_target_time += 1
        else:
            return None

    return people_present_in_target_time
