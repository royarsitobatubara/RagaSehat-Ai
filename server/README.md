# 🌐 **SERVER RagaSehat**

### 🚀 **How to Start**

### 🏃‍♀️‍➡️ **How to Running**

### 📂 **Directory Structure**
 ```text
   server/
   ├── .venv/               # Virtual environment Python (terisolasi)
   ├── data/                # Dataset kesehatan (misal: heart.csv)
   ├── model/               # Artifact model ML hasil training (.pkl / .onnx)
   ├── src/                 # Source code utama aplikasi
   │   ├── api/             # Endpoint & Router FastAPI
   │   ├── ML/              # Modul preprocessing & inference Machine Learning
   │   ├── notebooks/       # Eksperimen EDA & training model (.ipynb)
   │   ├── __init__.py      # Penanda package Python
   │   └── main.py          # Entry point utama FastAPI
   ├── .gitignore           # Daftar berkas/folder yang diabaikan oleh Git
   ├── Makefile             # Shortcut perintah eksekusi (run server, install, dll)
   ├── README.md            # Dokumentasi proyek
   └── requirements.txt     # Daftar dependensi & library Python
 ```

### 📊 Dataset References

| Kategori Penyakit | Deskripsi Data | Sumber Dataset |
| :--- | :--- | :--- |
| **Heart Disease** | Data indikator medis & risiko serangan jantung | [Kaggle - Heart](https://www.kaggle.com/datasets/jumainzulkaidah/data-penyakit-jantung) |
| **Cholesterol Level** | Data profil lipid (LDL, HDL, Trigliserida) | [Kaggle - Lipid & Cholesterol Dataset](https://www.kaggle.com/datasets) |
| **Diabetes / Gula Darah** | Indikator glukosa puasa & riwayat diabetes | [Kaggle - Pima Indians Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) |

> **Catatan:** Seluruh file `.csv` mentah disimpan di dalam folder `data/` dan diolah terlebih dahulu di `src/notebooks/` sebelum model diekspor ke `model/`.

---