from datetime import datetime

current_year = datetime.now().year
birth_year = current_year - int(age)
print("Vous êtes né(e) en", birth_year)
