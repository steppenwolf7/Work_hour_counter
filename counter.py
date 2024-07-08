def count_hours():
    try:
        eight_hour_days = int(input("Podaj liczbę dni w miesiącu w których pracujesz po 8,5 godziny:"))
        twelve_hour_days = int(input("Podaj liczbę dni w miesiącu w których pracujesz po 12 godzin:"))
        day_overtime_hours = int(input("Podaj liczbę nadgodzin dziennych:"))
        night_overtime_hours = int(input("Podaj liczbę nadgodzin nocnych:"))
    except ValueError:
        print("Podane wartości muszą być liczbami!")
        return

    sum_of_eight_hour = eight_hour_days * 8.5
    sum_of_twelve_hour = twelve_hour_days * 12
    
    sum_of_all_hours = day_overtime_hours + night_overtime_hours + sum_of_eight_hour + sum_of_twelve_hour

    night_hours = (twelve_hour_days * 8) + (eight_hour_days * 4.5) + night_overtime_hours

    print(f"Całkowita liczba godzin to {sum_of_all_hours}\nCałkowita liczba godzin nocnych to: {night_hours}")

if __name__ == "__main__":
    count_hours()