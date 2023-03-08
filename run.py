import subprocess

from datetime import date, datetime

today = date.today()

output = subprocess.run(["bash", "ssl_checker.sh"], stdout=subprocess.PIPE, text=True)

expiration_date = datetime.strptime(output.stdout.strip(), "%Y-%m-%d").date()

print(abs((today - expiration_date).days))
