import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "1923471")

API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5424505458:AAGIwqM1MMKB5TToJjaj9ecf25_YSA3ZVNQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "jasuranserials") 

DB_NAME = os.environ.get("DB_NAME","asuranj")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://video:video@cluster0.gp0rn.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
