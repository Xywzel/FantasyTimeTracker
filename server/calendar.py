
def main ():
    months = ["1. Petial","2. Rilava","3. Dahine","4. Necil","5. Delel","6. Zalaph","7. Gielel","8. Hyrico","9. Toros","10. Senaeb"]
    month_lens = [31, 30, 31, 30, 31, 30, 31, 30, 31, 32]
    weekdays = ["Amula","Libetu","Eheina","Syrik","Niram","Doriav"]

    day = 1
    weekday = 0
    month = 0

    kosomo_len = 13
    yalamo_len = 31
    kosomo = 0
    yalamo = 0

    current_year = 0
    while current_year < year:
        weekday += 1
        if weekday == len(weekdays):
            weekday = 0
        day += 1
        if day > month_lens[month]:
            day = 1
            month += 1
        if month == len(months):
            month = 0
            current_year += 1
        kosomo += 1
        if kosomo == kosomo_len:
            kosomo = 0
        yalamo += 1
        if yalamo == yalamo_len:
            yalamo = 0

    print("Year\tMonth\tDay\tWeekday\tKosomo\tYalamo\t")
    while year == current_year:
        k_phase = "(+)" if kosomo == 0 else "   "
        y_phase = "(+)" if yalamo == 0 else "   "
        print("", current_year, "\t", months[month], "\t", day, "\t", weekdays[weekday], "\t", k_phase, "\t", y_phase)
        weekday += 1
        if weekday == len(weekdays):
            weekday = 0
            print("--------------------------")
        day += 1
        if day > month_lens[month]:
            day = 1
            month += 1
            print("+++++++++++++++++++++++++++")
        if month == len(months):
            month = 0
            current_year += 1
            print("===========================")
        kosomo += 1
        if kosomo == kosomo_len:
            kosomo = 0
        yalamo += 1
        if yalamo == yalamo_len:
            yalamo = 0

main()
