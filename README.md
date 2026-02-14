# Intelligent Migration Control System (IMCS)

Description
-----------
Intelligent Migration Control System (IMCS) is a small project for exploring migration data and building a risk model. It includes Jupyter notebooks for analysis, a minimal app (`app.py`), and the raw dataset.

Quick overview
--------------
- `donnees_migratoires_mbujimayi.csv` — primary dataset.
- `modele_risque.ipynb`, `modele_risque-Copy1.ipynb` — analysis & modeling notebooks.
- `app.py` — simple entry point (demo/API).

Requirements
------------
Install project dependencies from `requirements.txt`.

Quick start (PowerShell)
------------------------
Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run notebooks:

```powershell
jupyter notebook
```

Run the app (local demo):

```powershell
python app.py
```

Notes
-----
- Check `app.py` before exposing it to production (secrets, input validation, logging).
- Do not commit sensitive or large data. Add datasets to `.gitignore` if needed.

Contributing
------------
- Fork, create a branch, implement changes, and open a pull request.

License
-------
MIT

Contact
-------
For questions or contributions, contact me : [Alphonse Kazadi](mailto:alphonsekazadi01@gmail.com).

