import requests
import time
import urllib3
import os
from datetime import datetime

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def choose_city():
    print("Choose City:")

    user_city_input_num = input(
        "1. Wrocław       2. Legnica      3. Wałbrzych        4. Jelenia Góra\n"
    )
    if user_city_input_num == "1":
        chosen_city = "Wrocław"
        return chosen_city
    elif user_city_input_num == "2":
        chosen_city = "Legnica"
        return chosen_city
    elif user_city_input_num == "3":
        chosen_city = "Wałbrzych"
        return chosen_city
    elif user_city_input_num == "4":
        chosen_city = "Jelenia Góra"
        return chosen_city
    else:
        print("Invalid city selection.")
        exit(1)


def main():
    url = "https://rezerwacje.duw.pl/status_kolejek/query.php?status"

    chosen_city = choose_city()

    user_ticket_value = input("What is your Ticket Value(ex: C085): ").upper()
    letter_user_ticket_value = user_ticket_value[0]
    number_user_ticket_value = int(user_ticket_value[1:])

    reminder = input("How many line before do you want to be reminded(ex: 5): ")
    number_reminder_ticket_value = number_user_ticket_value - int(reminder)

    while True:
        try:
            response = requests.get(url, verify=False)

            data = response.json()["result"]
        except Exception as e:
            print(f"Network/API error {e}")
            time.sleep(3)
            continue

        office_info = data[chosen_city]
        for id in office_info:
            ticket_value = id["ticket_value"].upper()
            if ticket_value.startswith(letter_user_ticket_value):
                # print(ticket_value)
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] Current ticket: {ticket_value}"
                )

                if ticket_value == letter_user_ticket_value + str(
                    number_reminder_ticket_value
                ):
                    print("Get ready your time has come")
                    pygame.mixer.init()
                    pygame.mixer.music.load("alert.wav")  # Use a .wav file here
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(0.1)
        time.sleep(5)


if __name__ == "__main__":
    main()
