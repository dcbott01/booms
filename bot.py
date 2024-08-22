import requests
from datetime import datetime, timezone
from colorama import Fore, Style, init
import time

# Initialize Colorama
init()

def print_welcome_message():
    print(r"""
 
  _  _   _    ____  _   ___    _   
 | \| | /_\  |_  / /_\ | _ \  /_\  
 | .` |/ _ \  / / / _ \|   / / _ \ 
 |_|\_/_/ \_\/___/_/ \_\_|_\/_/ \_\
                                   

    """)
    print(Fore.GREEN + Style.BRIGHT + "BOOMS BOT")
    print(Fore.CYAN + Style.BRIGHT + "Jajanin dong orang baik :)")
    print(Fore.YELLOW + Style.BRIGHT + "0x5bc0d1f74f371bee6dc18d52ff912b79703dbb54")
    print(Fore.RED + Style.BRIGHT + "Update Link: https://github.com/dcbott01/booms")
    print(Fore.BLUE + Style.BRIGHT + "Tukang Rename MATI AJA")

# Function to read the queries from the file
def read_queries(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Ask the user if they want to submit tasks
def ask_to_submit_tasks():
    while True:
        response = input("Do you want to submit tasks for all accounts? (yes/no): ").strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Print the welcome message
print_welcome_message()

# Read queries from the file
queries = read_queries('query.txt')

# Get the user's choice to submit tasks
submit_tasks = ask_to_submit_tasks()

# The URL for the session creation request
create_session_url = "https://api.booms.io/v1/auth/create-session"

# Headers for the session creation request
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, ",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://booms.io",
    "referer": "https://booms.io/",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127", "Microsoft Edge WebView2";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

# Currency ID to name mapping
currency_names = {
    1: "coin",
    2: "usdt",
    3: "booms",
    4: "ton"
}

def process_queries():
    for query in queries:
        payload = {"telegram_init_data": query}
        response = requests.post(create_session_url, headers=headers, json=payload)

        if response.status_code == 200:
            token = response.json().get('token')

            if token:
                profile_url = "https://api.booms.io/v1/profiles/self"
                get_headers = headers.copy()
                get_headers["authorization"] = f"Bearer {token}"

                profile_response = requests.get(profile_url, headers=get_headers)
                time.sleep(2)
                print(Fore.GREEN + '=' * 60 + Style.RESET_ALL)

                if profile_response.status_code == 200:
                    profile_data = profile_response.json()
                    name = profile_data.get('name')
                    coins_balance = profile_data.get('coins_balance')
                    level = profile_data.get('level')
                    coins_multiplier = profile_data.get('coins_multiplier')
                    energy_current_value = profile_data.get('energy_current_value')

                    print(Fore.CYAN + f"[Name] :" + Style.RESET_ALL + Fore.MAGENTA + f" {name}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"[Level] :" + Style.RESET_ALL + Fore.MAGENTA + f" {level}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"[Multiplier] :" + Style.RESET_ALL + Fore.MAGENTA + f" {coins_multiplier}" + Style.RESET_ALL)
                    print(Fore.CYAN + f"[Energy Current] :" + Style.RESET_ALL + Fore.MAGENTA + f" {energy_current_value}" + Style.RESET_ALL)

                    tap_url = "https://api.booms.io/v1/profiles/tap"
                    current_time = datetime.now(timezone.utc).isoformat()
                    tap_payload = {
                        "taps_count": energy_current_value,
                        "tapped_from": current_time
                    }
                    tap_response = requests.post(tap_url, headers=get_headers, json=tap_payload)

                    if tap_response.status_code == 200:
                        print(Fore.GREEN + "Tapping successful!" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Failed to send tap!" + Style.RESET_ALL)

                    daily_reward_url = "https://api.booms.io/v1/tasks/daily-reward"
                    daily_reward_response = requests.get(daily_reward_url, headers=get_headers)

                    if daily_reward_response.status_code == 200:
                        daily_reward_data = daily_reward_response.json()
                        collectable = daily_reward_data.get('collectable')
                        current_day = daily_reward_data.get('current_day')
                        last_reward_value = daily_reward_data.get('value', 'No reward value')

                        print(Fore.CYAN + f"Current Day : {current_day} - {last_reward_value} Coins" + Style.RESET_ALL)

                        # Always attempt to collect the daily reward
                        collect_reward_url = "https://api.booms.io/v1/tasks/daily-reward"
                        collect_reward_response = requests.post(collect_reward_url, headers=get_headers)

                        if collect_reward_response.status_code == 200:
                            print(Fore.GREEN + "Daily reward collected successfully!" + Style.RESET_ALL)
                        else:
                            print(Fore.GREEN + "Daily already collect!" + Style.RESET_ALL)

                    else:
                        print(Fore.RED + "Failed to retrieve daily reward information!" + Style.RESET_ALL)

                    balance_url = "https://api.booms.io/v1/balances"
                    balance_response = requests.get(balance_url, headers=get_headers)

                    if balance_response.status_code == 200:
                        balance_data = balance_response.json()
                        print(Fore.MAGENTA + "----------- Balance ----------" + Style.RESET_ALL)
                        for item in balance_data.get('items', []):
                            amount = item.get('amount')
                            currency_id = item.get('currency_id')

                            currency_name = currency_names.get(currency_id, "unknown")
                            print(Fore.BLUE + f"[{currency_name.capitalize()}] : {amount}" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Failed to retrieve balance information!" + Style.RESET_ALL)

                    tasks_url = "https://api.booms.io/v1/tasks"
                    tasks_response = requests.get(tasks_url, headers=get_headers)

                    if tasks_response.status_code == 200:
                        tasks_data = tasks_response.json()
                        if submit_tasks:
                            print(Fore.GREEN + "Tasks Data:" + Style.RESET_ALL)
                        for task in tasks_data.get('items', []):
                            task_id = task.get('id')
                            task_title = task.get('rewards', [{}])[0].get('title', 'No Title')

                            if task_id:
                                if submit_tasks:
                                    submit_task_url = f"https://api.booms.io/v1/tasks/{task_id}/submit"
                                    submit_task_response = requests.post(submit_task_url, headers=get_headers)

                                    if submit_task_response.status_code == 200:
                                        print(Fore.GREEN + f"Task {task_title} successfully!" + Style.RESET_ALL)
                                    else:
                                        print(Fore.RED + f"Failed to submit Task {task_title}!" + Style.RESET_ALL)
    
                    else:
                        print(Fore.RED + "Failed to retrieve tasks information!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Failed to retrieve profile information!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No token found in the response!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Session creation failed!" + Style.RESET_ALL)


# Loop to process queries every 15 minutes
while True:
    process_queries()
    print(Fore.CYAN + "================ Waiting 15 Minutes Before Loop ================" + Style.RESET_ALL)
    time.sleep(15 * 60)  # Sleep for 15 minutes
