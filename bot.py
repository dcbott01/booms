import argparse
import random
import json
import requests
from requests.structures import CaseInsensitiveDict
import time
import datetime
from colorama import init, Fore, Style
from requests.exceptions import RequestException, Timeout, ConnectionError

init(autoreset=True)

# Define a function for retrying HTTP requests
def retry_request(url, headers):
    retries = 3  # Set the maximum number of retries
    delay = 1  # Set the initial delay between retries
    backoff = 2  # Set the backoff factor for exponential backoff

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
        except (RequestException, Timeout, ConnectionError):
            # Handle different types of exceptions (e.g., timeout, connection error)
            if attempt < retries - 1:
                # Retry with exponential backoff
                delay *= backoff
                time.sleep(delay)
            else:
                # If all retries fail, raise the exception
                raise

def join_squad(token):
    url = 'https://game-domain.blum.codes/api/v1/tribe/d6a340fe-a1e5-450e-9971-d2c216e82be7/join'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = requests.post(url, headers=headers)
    except RequestException as e:
        print(f"{Fore.RED+Style.BRIGHT}Request failed: {e}")

start_time = datetime.datetime.now()  

def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Blum BOT')

    args = parser.parse_args()
    args.task = 'n'  

    return args

def check_tasks(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
   
    try:
        response = requests.get('https://game-domain.blum.codes/api/v1/tasks', headers=headers)
        if response.status_code == 200:
            tasks = response.json()
            for task in tasks:
                titlenya = task['title']
                if task['status'] == 'CLAIMED':
                    print(f"{Fore.CYAN+Style.BRIGHT}Task {titlenya} claimed  | Status: {task['status']} | Reward: {task['reward']}")
                elif task['status'] == 'NOT_STARTED':
                    print(f"{Fore.YELLOW+Style.BRIGHT}Starting Task: {task['title']}")
                    start_task(token, task['id'],titlenya)
                    claim_task(token, task['id'],titlenya)
                else:
                    print(f"{Fore.CYAN+Style.BRIGHT}Task already started: {task['title']} | Status: {task['status']} | Reward: {task['reward']}")
        else:
            print(f"{Fore.RED+Style.BRIGHT}\nFailed to get tasks")
    except:
        print(f"{Fore.RED+Style.BRIGHT}\nFailed to get tasks {response.status_code} ")

def start_task(token, task_id,titlenya):
    url = f'https://game-domain.blum.codes/api/v1/tasks/{task_id}/start'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(f"{Fore.GREEN+Style.BRIGHT}\nTask {titlenya} started")
        else:
            print(f"{Fore.RED+Style.BRIGHT}\nFailed to start task {titlenya}")
        return 
    except:
        print(f"{Fore.RED+Style.BRIGHT}\nFailed to start task {titlenya} {response.status_code} ")

def claim_task(token, task_id,titlenya):
    print(f"{Fore.YELLOW+Style.BRIGHT}\nClaiming task {titlenya}")
    url = f'https://game-domain.blum.codes/api/v1/tasks/{task_id}/claim'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(f"{Fore.CYAN+Style.BRIGHT}\nTask {titlenya} claimed")
        else:
            print(f"{Fore.RED+Style.BRIGHT}\nFailed to claim task {titlenya}")
    except:
        print(f"{Fore.RED+Style.BRIGHT}\nFailed to claim task {titlenya} {response.status_code} ")

        
def get_new_token(query_id):
    import json
 
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://telegram.blum.codes",
        "priority": "u=1, i",
        "referer": "https://telegram.blum.codes/"
    }

  
    data = json.dumps({"query": query_id})

  
    url = "https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"

   
    for attempt in range(3):
        print(f"\r{Fore.YELLOW+Style.BRIGHT}Mendapatkan token...", end="", flush=True)
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print(f"\r{Fore.GREEN+Style.BRIGHT}Token berhasil dibuat", end="", flush=True)
            response_json = response.json()
            return response_json['token']['refresh']
        else:
            print(response.json())
            print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan token, percobaan {attempt + 1}", flush=True)
  

    print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan token setelah 3 percobaan.", flush=True)
    return None


def get_user_info(token):

    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get('https://gateway.blum.codes/v1/user/me', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        hasil = response.json()
        if hasil['message'] == 'Token is invalid':
            print(f"{Fore.RED+Style.BRIGHT}Token salah, mendapatkan token baru...")
            # Mendapatkan token baru
            new_token = get_new_token()
            if new_token:
                print(f"{Fore.GREEN+Style.BRIGHT}Token baru diperoleh, mencoba lagi...")
                return get_user_info(new_token)  # Rekursif memanggil fungsi dengan token baru
            else:
                print(f"{Fore.RED+Style.BRIGHT}Gagal mendapatkan token baru.")
                return None
        else:
            print(f"{Fore.RED+Style.BRIGHT}Gagal mendapatkan informasi user")
            return None

def check_daily_reward(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
    
    current_offset = int(time.timezone / 60)
    
    try:
        response = requests.post(f'https://game-domain.blum.codes/api/v1/daily-reward?offset={current_offset}', headers=headers, timeout=10)
        if response.status_code == 200:
            try:
                return response.json()  # This ensures that the response is always parsed as JSON
            except json.JSONDecodeError:
                if response.text == "OK":
                    return {"message": "OK"}  # Return a dictionary with the appropriate message
                print(f"{Fore.RED+Style.BRIGHT}Json Error: {response.text}")
                return {"message": "error"}  # Return a dictionary with an error message
        else:
            print(f"{Fore.RED+Style.BRIGHT}Udah di Claim")  # Print the HTTP error code for debugging
            return {"message": "error"}  # Return a dictionary with an error message
    except requests.exceptions.Timeout:
        print(f"\r{Fore.RED+Style.BRIGHT}Gagal claim daily: Timeout")
        return {"message": "error"}  # Return a dictionary with an error message
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED+Style.BRIGHT}Request Exception: {e}")  # Print the exception for debugging
        return {"message": "error"}  # Return a dictionary with an error message
      
    return {"message": "error"}  # Return a dictionary with an error message if none of the above conditions are met

# Fungsi untuk mendapatkan saldo
def get_balance(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    for attempt in range(3):
        try:
            response = requests.get('https://game-domain.blum.codes/api/v1/user/balance', headers=headers)
            # print(response.json())
            if response.status_code == 200:
                # print(f"{Fore.GREEN+Style.BRIGHT}Berhasil mendapatkan saldo")
                return response.json()
            else:
                print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan saldo, percobaan {attempt + 1}", flush=True)
        except:
            print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan saldo, mencoba lagi {attempt + 1}", flush=True)
    print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan saldo setelah 3 percobaan.", flush=True)
    return None


def play_game(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/game/play', headers=headers)
    return response.json()



def claim_game(token, game_id, points):
    url = "https://game-domain.blum.codes/api/v1/game/claim"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["authorization"] = "Bearer "+token
    headers["content-type"] = "application/json"
    headers["origin"] = "https://telegram.blum.codes"

    headers["priority"] = "u=1, i"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    data = '{"gameId":"'+game_id+'","points":'+str(points)+'}'

    resp = requests.post(url, headers=headers, data=data)
    return resp 



def claim_balance(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/farming/claim', headers=headers)
    return response.json()


def start_farming(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/farming/start', headers=headers)
    return response.json()

def refresh_token(old_refresh_token):
    url = 'https://gateway.blum.codes/v1/auth/refresh'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'origin': 'https://telegram.blum.codes',
        'referer': 'https://telegram.blum.codes/'
    }
    data = {
        'refresh': old_refresh_token
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{Fore.RED+Style.BRIGHT}Gagal refresh token untuk: {old_refresh_token}")
        return None  


def check_balance_friend(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get('https://gateway.blum.codes/v1/friends/balance', headers=headers)
    balance_info = response.json()
    return balance_info



def claim_balance_friend(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://gateway.blum.codes/v1/friends/claim', headers=headers)
    return response.json()

def print_welcome_message():
    print(r"""
 
  _  _   _    ____  _   ___    _   
 | \| | /_\  |_  / /_\ | _ \  /_\  
 | .` |/ _ \  / / / _ \|   / / _ \ 
 |_|\_/_/ \_\/___/_/ \_\_|_\/_/ \_\
                                   

    """)
    print(Fore.GREEN + Style.BRIGHT + "BLUM BOT")
    print(Fore.CYAN + Style.BRIGHT + "Jajanin dong orang baik :)")
    print(Fore.YELLOW + Style.BRIGHT + "0x5bc0d1f74f371bee6dc18d52ff912b79703dbb54")
    print(Fore.RED + Style.BRIGHT + "Update Link: https://github.com/dcbott01/blum")
    print(Fore.BLUE + Style.BRIGHT + "Tukang Rename MATI AJA")
    print(Fore.GREEN + "=====================================")

    
checked_tasks = {}
with open('tokens.txt', 'r') as file:
    query_ids = file.read().splitlines()
while True:
    args = parse_arguments()
    cek_task_enable = args.task
    print_welcome_message()

    for query_id in query_ids:
        token = get_new_token(query_id) 
        user_info = get_user_info(token)
        if user_info is None:
            continue
        print(f"{Fore.BLUE+Style.BRIGHT}\r\n==================[{Fore.WHITE+Style.BRIGHT}{user_info['username']}{Fore.BLUE+Style.BRIGHT}]==================")  
        print(f"\r{Fore.CYAN+Style.BRIGHT}[ Daily Reward ] : Checking daily reward...", end="", flush=True)
        daily_reward_response = check_daily_reward(token)
        if daily_reward_response is None:
            print(f"\r{Fore.RED+Style.BRIGHT}[ Daily Reward ] : Gagal cek hadiah harian", flush=True)
            continue
        else:
            if daily_reward_response.get('message') == 'same day':
                print(f"\r{Fore.CYAN+Style.BRIGHT}[ Daily Reward ] : Hadiah harian sudah diklaim hari ini", flush=True)
            elif daily_reward_response.get('message') == 'OK':
                print(f"\r{Fore.CYAN+Style.BRIGHT}[ Daily Reward ] : Hadiah harian berhasil diklaim!", flush=True)
        
        join_squad_response = join_squad(token)
        # Pengecekan saldo
        print(f"\r{Fore.YELLOW+Style.BRIGHT}Getting Info....", end="", flush=True)
        balance_info = get_balance(token)
        if balance_info is None:
            print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan informasi balance", flush=True)
            continue
        else:
            available_balance_before = balance_info['availableBalance'] 
            balance_before = f"{float(available_balance_before):,.0f}".replace(",", ".")
            print(f"\r{Fore.YELLOW+Style.BRIGHT}[Balance]: {balance_before}", flush=True)
            print(f"{Fore.MAGENTA+Style.BRIGHT}[Tiket Game]: {balance_info['playPasses']}")
            
            farming_info = balance_info.get('farming')
            if farming_info:
                
                end_time_ms = farming_info['endTime']
                end_time_s = end_time_ms / 1000.0
                end_utc_date_time = datetime.datetime.fromtimestamp(end_time_s, datetime.timezone.utc)
                current_utc_time = datetime.datetime.now(datetime.timezone.utc)
                time_difference = end_utc_date_time - current_utc_time
                hours_remaining = int(time_difference.total_seconds() // 3600)
                minutes_remaining = int((time_difference.total_seconds() % 3600) // 60)
                farming_balance = farming_info['balance']
                farming_balance_formated = f"{float(farming_balance):,.0f}".replace(",", ".")
                print(f"{Fore.RED+Style.BRIGHT}[ Claim Balance ] : {hours_remaining} jam {minutes_remaining} menit | Balance: {farming_balance_formated}")
                if hours_remaining < 0:
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claiming balance...", end="", flush=True)
                    claim_response = claim_balance(token)
                    if claim_response:
                        print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claimed: {claim_response['availableBalance']}", flush=True)
                        print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Starting farming...", end="", flush=True)
                        start_response = start_farming(token)
                        if start_response:
                            print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Farming started.", flush=True)
                        else:
                            print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal start farming", start_response.status_code, flush=True)
                    else:
                        print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal claim", claim_response.status_code, flush=True)
            else:
                print(f"\n{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal mendapatkan informasi farming", flush=True)
                print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claiming balance...", end="", flush=True)
                claim_response = claim_balance(token)
                if claim_response:
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claimed               ", flush=True)
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Starting farming...", end="", flush=True)
                    start_response = start_farming(token)
                    if start_response:
                        print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Farming started.", flush=True)
                    else:
                        print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal start farming", start_response.status_code, flush=True)
                else:
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal claim", claim_response.status_code, flush=True)
        # cek task 
        if cek_task_enable == 'y':
            if query_id not in checked_tasks or not checked_tasks[query_id]:
                print(f"\r{Fore.YELLOW+Style.BRIGHT}Checking tasks...\n", end="", flush=True)
                check_tasks(token)
                checked_tasks[query_id] = True

        
        print(f"\r{Fore.YELLOW+Style.BRIGHT}[ Reff Balance ] : Checking reff balance...", end="", flush=True)
        friend_balance = check_balance_friend(token)
        if friend_balance:
            if friend_balance['canClaim']:
                print(f"\r{Fore.GREEN+Style.BRIGHT}Reff Balance: {friend_balance['amountForClaim']}", flush=True)
                print(f"\n\r{Fore.GREEN+Style.BRIGHT}Claiming Ref balance.....", flush=True)
                claim_friend_balance = claim_balance_friend(token)
                if claim_friend_balance:
                    claimed_amount = claim_friend_balance['claimBalance']
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Reff Balance ] : Sukses claim total: {claimed_amount}", flush=True)
                else:
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Reff Balance ] : Gagal mengklaim saldo ref", flush=True)
            else:
                
                can_claim_at = friend_balance.get('canClaimAt')
                if can_claim_at:
                    claim_time = datetime.datetime.fromtimestamp(int(can_claim_at) / 1000)
                    current_time = datetime.datetime.now()
                    time_diff = claim_time - current_time
                    hours, remainder = divmod(int(time_diff.total_seconds()), 3600)
                    minutes, seconds = divmod(remainder, 60)
                    print(f"{Fore.RED+Style.BRIGHT}\r[ Reff Balance ] : Klaim pada {hours} jam {minutes} menit lagi", flush=True)
                else:
                    print(f"{Fore.RED+Style.BRIGHT}\r[ Reff Balance ] : False                                 ", flush=True)
        else:
            print(f"{Fore.RED+Style.BRIGHT}\r[ Reff Balance ] : Gagal cek reff balance", flush=True)
        available_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

        while balance_info['playPasses'] > 0:
            print(f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] : Playing game...")
            game_response = play_game(token)
            print(f"\r{Fore.CYAN+Style.BRIGHT}[ Play Game ] : Checking game...", end="", flush=True)
            time.sleep(1)
            claim_response = claim_game(token, game_response['gameId'], random.randint(1500, 2000))
            if claim_response is None:
                print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal mengklaim game, mencoba lagi...", flush=True)
            while True:
                if claim_response.text == '{"message":"game session not finished"}':
                    time.sleep(1)  
                    random_color = random.choice(available_colors)
                    print(f"\r{random_color+Style.BRIGHT}[ Play Game ] : Game belum selesai.. mencoba lagi", flush=True)
                    claim_response = claim_game(token, game_response['gameId'], random.randint(1500, 2000))
                    if claim_response is None:
                        print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal mengklaim game, mencoba lagi...", flush=True)
                elif claim_response.text == '{"message":"game session not found"}':
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Game sudah berakhir", flush=True)
                    break
                elif 'message' in claim_response and claim_response['message'] == 'Token is invalid':
                    print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Token tidak valid, mendapatkan token baru...")
                    token = get_new_token(query_id) 
                    continue  
                else:
                    print(f"\r{Fore.YELLOW+Style.BRIGHT}[ Play Game ] : Game selesai: {claim_response.text}", flush=True)
                    break
            
            balance_info = get_balance(token) 
            if balance_info is None: 
                print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] Gagal mendapatkan informasi tiket", flush=True)
            else:
                available_balance_after = balance_info['availableBalance']  
                before = float(available_balance_before) 
                after =  float(available_balance_after)
                # balance_after = f"{float(available_balance):,.0f}".replace(",", ".")
                total_balance = after - before  
                print(f"\r{Fore.YELLOW+Style.BRIGHT}[ Play Game ]: You Got Total {total_balance} From Playing Game", flush=True)
                if balance_info['playPasses'] > 0:
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Play Game ] : Tiket masih tersedia, memainkan game lagi...", flush=True)
                    continue  
                else:
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Tidak ada tiket tersisa.", flush=True)
                    break

        
    print(f"\n{Fore.GREEN+Style.BRIGHT}========={Fore.WHITE+Style.BRIGHT}Semua akun berhasil di proses{Fore.GREEN+Style.BRIGHT}=========", end="", flush=True)
    print(f"\r\n\n{Fore.GREEN+Style.BRIGHT}Refreshing token...", end="", flush=True)
    import sys
    waktu_tunggu = 3600  # 60 menit dalam detik
    for detik in range(waktu_tunggu, 0, -1):
        sys.stdout.write(f"\r{Fore.CYAN}Menunggu waktu claim berikutnya dalam {Fore.CYAN}{Fore.WHITE}{detik // 60} menit {Fore.WHITE}{detik % 60} detik")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rWaktu claim berikutnya telah tiba!                                                          \n")
