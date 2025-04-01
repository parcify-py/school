
# Použité funkce ve skriptu :
## Ve svém skriptu jsem použil několik základních funkcí Pythonu, aby seznam aut získal požadovaný tvar. Tady je popis jednotlivých kroků:

### Nejprve jsem použil len(), abych zjistil, kolik prvků je v mém seznamu aut. Tento krok mi pomohl získat přehled o délce seznamu a nastavit cyklus.
### S využitím for cyklu jsem prošel celý seznam car a vytiskl názvy všech aut jedno po druhém.
###  Nové auto jsem do seznamu přidal pomocí funkce append(). Uživatel zadal jeho název prostřednictvím input().
### Staré auto, konkrétně 'Skoda', jsem odstranil z mého seznamu pomocí remove(), protože už tam nemělo co dělat.
### Aby byl seznam seřazený podle abecedy, použil jsem funkci sort(). Ale pak jsem si řekl, že obrácené pořadí bude zajímavější, a proto jsem použil reverse().
### Během celého procesu jsem používal print(), abych si zobrazil délku seznamu, názvy aut a konečný stav seznamu.
Muj code
```python
car = ['Skoda','Mercedes','Lada','Reno','Hyundai','Tesla']
print(len(car))
for i in range(len(car)):
    print(car[i])
car.append(input("Enter next car "))
car.remove('Skoda')
car.sort()
car.reverse()
print(car)
```
![OGC](https://github.com/user-attachments/assets/7db372c0-134d-40ca-86a0-439cf2a75757)
