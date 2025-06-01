# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

PT Edutech merupakan perusahaan teknologi pendidikan yang terus berkembang dan sangat bergantung pada sumber daya manusia yang kompeten dan stabil. Namun, dalam beberapa tahun terakhir, HRD PT Edutech menghadapi tantangan dalam mempertahankan karyawan. Tingkat attrition atau pengunduran diri karyawan yang cukup tinggi menimbulkan kekhawatiran, karena berdampak langsung terhadap kelangsungan proyek, beban kerja tim, serta biaya rekrutmen dan pelatihan karyawan baru.

Selama ini, proses identifikasi penyebab attrition masih bersifat manual dan berdasarkan asumsi, sehingga tidak memberikan gambaran yang akurat tentang pola dan faktor-faktor yang berkontribusi terhadap keputusan karyawan untuk resign. Oleh karena itu, HRD ingin memanfaatkan pendekatan data science untuk menggali lebih dalam data karyawan dan mengidentifikasi variabel-variabel penting—seperti masa kerja, benefit, jabatan, lokasi kerja, beban kerja, performa, dan keterlibatan dalam pelatihan—yang dapat memengaruhi risiko pengunduran diri.

Oleh karena itu, HRD PT Edutech memerlukan pendekatan **data science** untuk:

- Mengidentifikasi faktor utama yang menyebabkan karyawan resign
- Membangun **model machine learning** untuk prediksi resign
- Menyediakan **business dashboard** untuk memantau kondisi karyawan secara real-time

## Permasalahan Bisnis

Beberapa permasalahan bisnis dapat dirumuskan menjadi beberapa pertanyaan sebagai berikut:

- Mengapa karyawan muda (usia 20–30 tahun) lebih rentan resign?
- Apakah gaji, benefit, dan stock option sudah kompetitif?
- Seberapa besar pengaruh kepuasan kerja dan lingkungan kerja?
- Apa dampak lembur dan perjalanan dinas terhadap burnout?
- Mengapa tingkat resign tertinggi terjadi di departemen R&D?

## Cakupan Proyek

A. Pengambilan & inspeksi data karyawan

B. Pembersihan data dari:

- Missing value
- Invalid data
- Duplicate data
- Inaccurate value
- Inconsistent value
- Outlier

C. Exploratory Data Analysis (EDA) mencakup:

- Distribusi numerik & kategorikal
- Korelasi antar fitur
- Visualisasi insight

D. Feature engineering / Data Preparation:

- Seleksi fitur
- Transformasi & scaling

E. Model training dengan algoritma machine learning

F. Evaluasi model menggunakan confusion matrix

## Persiapan

- **Dataset**: [Jaya Maju Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)
- **Python**: 3.11
- **Setup Environment**:
  ```bash
  python -m venv hr-problem-analysis-project
  hr-problem-analysis-project\Scripts\activate
  pip install -r requirements.txt
  pip install streamlit
  ```
- Gunakan data employees_sample.csv untuk melakukan prediksi model
- **Metabase acess:**

  **Email**: root@mail.com

  **Password**: root123

## Business Dashboard

Dashboard interaktif dibuat untuk membantu tim HR dalam memantau dan menganalisis faktor-faktor penyebab karyawan resign, seperti:

- Usia
- Benefit
- Tingkat Kepuasan Kerja
- Beban Kerja
- Frekuensi Perjalanan Dinas
- Departemen

Dashboard ini menyajikan **insight visual** berdasarkan hasil analisis dan model machine learning untuk mendukung pengambilan keputusan secara **data-driven**.

![Dashboard Analitik HR](mathiasy-dashboard.png)

## Conclusion

Dari hasil analisis data karyawan permasalahn yang terjadi dapat disimpulkan menjadi beberapa aspek yang menyebabkan karyawan resign:

**Aspek Demografi**

- Usia muda (20–30 tahun) → lebih rentan resign
- Belum menikah → lebih sering resign
- Lulusan S1 & Life Sciences → cenderung resign
- Jenis kelamin & jarak rumah tidak terlalu berpengaruh
- Pengalaman kerja rendah → lebih rentan resign

**Aspek Kepuasan**

- Kepuasan kerja tinggi → risiko resign menurun
- Lingkungan kerja buruk → memicu resign
- Hubungan sosial positif → retensi lebih tinggi
- Work-life balance rendah → lebih mudah resign

**Aspek Karier**

- Laboratory Technician & Research Scientist → paling banyak resign
- Jabatan rendah → lebih berisiko
- Lama bekerja pendek → lebih mudah resign

**Aspek Kompensasi**

- Income tinggi → lebih bertahan
- Stock option → meningkatkan loyalitas

**Aspek Beban Kerja**

- Lembur sering → memicu resign
- Perjalanan bisnis → berkorelasi dengan resign
- R&D department → tingkat resign tertinggi

## Rekomendasi Action Items

A. Mengurangi Resign pada Karyawan Muda

- Program onboarding & mentoring
- Job description yang jelas
- Jalur karier progresif
- Pelatihan & pengembangan rutin

B. Meningkatkan Gaji & Benefit

- Evaluasi dan kaji ulang terkait gaji / upah
- Berikan bonus upah berbasis performa
- Perluas skema kepemilikan saham yang merata

C. Meningkatkan Kepuasan & Lingkungan Kerja

- Survei rutin kepuasan kerja
- Implementasi perbaikan dari hasil survei
- Lingkungan kolaboratif & suportif

D. Mengurangi Stress Kerja karena Lembur/Perjalanan

- Batasi lembur sesuai regulasi
- Kompensasi lembur & istirahat
- Gunakan kerja jarak jauh bila memungkinkan

E. Menangani Tingginya Resign di R&D

- Evaluasi ekspektasi & beban kerja
- Sediakan tools & fasilitas yang memadai
- Libatkan tim R&D dalam proyek lintas fungsi
