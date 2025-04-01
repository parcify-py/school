# Python
[Priklad codu](#popis-kódu)
## Python je vysokoúrovňový, interpretovaný programovací jazyk, který v roce 1991 navrhl Guido van Rossum. Nabízí dynamickou kontrolu datových typů a podporuje různá programovací paradigmata, včetně objektově orientovaného, imperativního nebo funkcionálního. 

![159-1595848_python-logo-png-transparent-background-python-logo-png](https://github.com/user-attachments/assets/a711f677-d676-4817-980f-e4e6c4eb4584)
# Priklad python code
## Popis kódu:
  Funkce factorial přijímá jeden argument n, což je číslo, jehož faktoriál se počítá.
  Pokud je n rovno 0 nebo 1 (základní případ), funkce vrací 1.
  Pokud je n větší než 1, funkce volá sama sebe (rekurze) s argumentem n-1 a násobí výsledek číslem n.
  V hlavní části programu je funkce factorial zavolána pro číslo 5 a výsledek je vypsán na obrazovku.
  Tento kód tedy vypočítává faktoriál čísla pomocí rekurzivního přístupu. Například faktoriál čísla 5 (5!) je 5 × 4 × 3 × 2 × 1 = 120.

```python
def factorial(n):
    # Základní případ: faktoriál čísla 0 nebo 1 je 1
    if n == 0 or n == 1:
        return 1
    # Rekurzivní případ: n se násobí faktoriálem z (n-1)
    else:
        return n * factorial(n - 1)

# Příklad použití funkce
cislo = 5
vysledek = factorial(cislo)
print(f"Faktoriál čísla {cislo} je {vysledek}")
```
![nyan-cat-icegif-22](https://github.com/user-attachments/assets/a4de726f-635a-4cae-bd28-c4d4745565d2)
