**This was fixed in uv 0.5.30**

---

```bash
git clone https://github.com/RazerM/uv-cannot-install-this.git
cd uv-cannot-install-this
uv build --sdist
uv build --wheel dist/uv_cannot_install_this-1.0.tar.gz
uvx --from=dist/uv_cannot_install_this-1.0-py3-none-any.whl --python 3.12 --refresh uv-cannot-install-this
```

```
Missing: data/PmwTDwPvyfFkMzuJjMYZGwVcaFXUvXXwGcRIgaLroLunLYwqTHqwsDyuxyrMwlClMPzIYvVWEqCDQlCLrGeVrmiNgsQzVsMohMbx
Found:   data/PmwTDwPvyfFkMzuJjMYZGwVcaFXUvXXwGcRIgaLro

Missing: data/BqMlnKrLJFRUBYGNkhkzSwTbVJCIUoiHEnzKiKLADIHROEqVxEWYAsCusUAJKcXYLBZmxYhKncZsXLEjjhctJVXbcvBuSYjkiEnu
Found:   data/BqMlnKrLJFRUBYGNkhkzSwTbVJCIUoiHEnzKiKLAD

Missing: data/WRDWdZSTLeOixzwhUBDuWyktTYmXLkDuJpJvPxxWxjiHuwqxovuwRwgQwxpxVBTgvUkvwnBDEuRTXJpaJsEWwLwlYTGaqRBbFbZN
Found:   data/WRDWdZSTLeOixzwhUBDuWyktTYmXLkDuJpJvPxxWx

Missing: data/cvpYHXtnEbfJmnflwYwRUneJnWoAswvXjJfxxnoQsRoWLbmjhGUDDxlXnPGTRLgXxXXlehxbDHmPzOoqKQxQAshPTTFtstwVaDOz
Found:   data/cvpYHXtnEbfJmnflwYwRUneJnWoAswvXjJfxxnoQs

Missing: data/jhDgXQPnsxYXugmltiBRzrwPualmsjTEjyCQPIXNoEYEOKBaCGtobkgisEyGkFXAovuciJOegxGjwKScJuVujEWntxTdPUeFWKiC
Found:   data/jhDgXQPnsxYXugmltiBRzrwPualmsjTEjyCQPIXNo

Missing: data/IpjXpmbssCRJYzwCMUFAXrQJKFGUZjlBxYDlOnxclVVOBfxOfDDeTcVlpHQocAMejwdRourDpgcxEDROcgYtpRcGNxwjJpKfMQIg
Found:   data/IpjXpmbssCRJYzwCMUFAXrQJKFGUZjlBxYDlOnxcl

Missing: data/tEjeOXVVZtJYcOdIjItoRTYnCFDcjAdoMJbholfRiRkesWDLYxGbQHRwyzIJFaDxdfleUsDPKftreQLyArliSyTmPqMJJKygqivC
Found:   data/tEjeOXVVZtJYcOdIjItoRTYnCFDcjAdoMJbholfRi

9993 files ok, 7 missing
```
