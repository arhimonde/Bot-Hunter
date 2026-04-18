import os
import json
import time
import schedule
from dotenv import load_dotenv
from scraper import get_universal_deals
from notifier import send_telegram_alert

base_path = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(base_path, '.env')
trackers_path = os.path.join(base_path, 'trackers.json')

load_dotenv(dotenv_path)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

MIN_DISCOUNT = 70

def global_hunt():
    try:
        with open(trackers_path, 'r') as f:
            sources = json.load(f)
    except: return

    print(f"\n🌍 [{time.strftime('%H:%M:%S')}] Escaneo Global de Chollos (Filtro: {MIN_DISCOUNT}%+)")
    
    for source in sources:
        print(f"📡 Escaneando {source['name']}...")
        deals = get_universal_deals(source['url'])
        
        found_any = False
        for deal in deals:
            # Calcul reducere
            current = deal["price"]
            old = deal["old_price"]
            
            discount = int(((old - current) / old) * 100)
            
            if discount >= MIN_DISCOUNT:
                found_any = True
                msg = (
                    f"💎 ¡SUPEROFERTA DETECTADA ({discount}%)! 💎\n"
                    f"📦 {deal['title']}\n"
                    f"💰 Ahora: {current}€ (Antes: {old}€)\n"
                    f"🔗 Link: {deal['link']}"
                )
                send_telegram_alert(BOT_TOKEN, CHAT_ID, msg)
                print(f"   ✨ Encontrado: {deal['title']} (-{discount}%)")
        
        if not found_any:
            print(f"   (No se encontraron superofertas de {MIN_DISCOUNT}% en esta pasada)")
        
        time.sleep(5) # Pauză mai lungă între feed-uri

def main():
    print("🚀 Bot de Caza Global - Versión 2.0")
    
    # Mesaj de bun venit pe Telegram pentru confirmare
    welcome_msg = "🌟 ¡Bot Hunter Activado! 🎯\nSunt gata! Voi monitoriza feed-ul principal și te voi anunța imediat ce găsesc oferte de peste 70%."
    send_telegram_alert(BOT_TOKEN, CHAT_ID, welcome_msg)
    
    global_hunt()
    
    # Verificăm la fiecare oră (ofertele pe feed-ul principal se schimbă repede)
    schedule.every(1).hours.do(global_hunt)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
