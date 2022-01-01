def add_time(start_time, duration, day_of_the_week=None):

    timeOfDay = start_time.split()[1]
    start_time = start_time.split()[0].split(":")
    start_hours = int(start_time[0])
    start_minutes = int(start_time[1])

    duration = duration.split(":")
    duration_hours = int(duration[0])
    duration_minutes = int(duration[1])

    day_of_the_week_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                            7: 'Sunday'}

    def get_day_of_the_week(day_of_the_week):
        for key, value in day_of_the_week_dict.items():
            if day_of_the_week == value:
                return key

    if day_of_the_week:
        day_of_the_week = day_of_the_week.lower().title()
        number_of_the_day = get_day_of_the_week(day_of_the_week)


    if "PM" in timeOfDay:
        start_hours = start_hours + 12


    combineMinutes = start_minutes + duration_minutes
    combineHours = start_hours + duration_hours


    if combineMinutes > 59:
        combineMinutes = start_minutes + duration_minutes - 60
        combineHours = combineHours + 1

    if combineMinutes < 10:
        combineMinutes = "0" + str(combineMinutes)

    if duration_hours + duration_minutes == 0:
        time = str(combineHours) + ":" + str(combineMinutes) + " " + timeOfDay
        return time

    if combineHours < 24:
        if combineHours == 12:
            combineHours = combineHours + 12

        time = str(combineHours - 12) + ":" + str(combineMinutes) + " PM"
        if day_of_the_week:
            time = time + ", " + day_of_the_week



    if combineHours > 24:
        restHours = combineHours - 24
        days = int(combineHours / 24)

        if start_minutes + duration_minutes > 59:
            start_hours += 1

        if restHours < 24:
            time = str(restHours) + ":" + str(combineMinutes) + " AM" + " (next day)"
            if day_of_the_week:
                day = number_of_the_day + days
                time = str(restHours) + ":" + str(combineMinutes) + " AM" + ", " + str(day_of_the_week_dict.get(day)) + " (next day)"


        if restHours >= 24:
            restHours = start_hours + (duration_hours % 24)
            restHours = restHours - 24
            if restHours == 0:
                restHours += 12
            time = str(restHours) + ":" + str(combineMinutes) + " AM" + " (" + str(days) + " days later)"
            if day_of_the_week:
                day = number_of_the_day + days
                if day > 7:
                    day = day % 7
                time = str(restHours) + ":" + str(combineMinutes) + " AM" + ", " + str(day_of_the_week_dict.get(day)) + " (" + str(days) + " days later)"






    return print(time)


add_time("5:01 AM", "0:00")
add_time("8:16 PM", "466:02", "tuesday")
add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30", "monday")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")