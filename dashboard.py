from collections import namedtuple
import altair as alt
import math
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

plt.style.use("seaborn")
st.set_page_config(
    page_title="Penduduk Berumur 10 Tahun ke Atas yang Buta Huruf",
    # layout="wide"
)

pp, name = st.columns([1, 10])
pp.image("data/profile/pp.png", width=60)
name.markdown(
    """
        <style>
            .name {
                margin-top: -15px;
            }
            .sub {
                margin-top: -20px;
            }
            .date {
                margin-top: -20px;
                font-size: 12px;
            }
        </style>
    """,
    unsafe_allow_html=True,
)
name.markdown("<h6 class='name'>Muhammad Devid</h6>", unsafe_allow_html=True)
name.markdown("<p class='sub'>TETRIS III: Data Analytics</p>", unsafe_allow_html=True)
name.markdown("<p class='date'>10 juni 2023</p>", unsafe_allow_html=True)

"---"

st.title("Penduduk Berumur 10 Tahun ke Atas yang Buta Huruf!")

st.write(
    """
        Setiap individu memiliki hak yang sama untuk mendapatkan pendidikan dan mengembangkan kemampuan literasi. Buta huruf dapat menghambat seseorang dalam m
        engakses informasi, memperoleh pekerjaan yang layak, dan berpartisipasi secara aktif dalam masyarakat. Oleh karena itu, adalah tanggung jawab kita untuk 
        memastikan bahwa penduduk berumur 10 tahun ke atas yang masih buta huruf mendapatkan kesempatan yang setara untuk belajar.
    """
)
st.info(
    "***Undang-Undang Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional, mengatur sistem pendidikan di Indonesia. Salah satu tujuan undang-undang ini adalah memberikan pendidikan yang berkualitas dan merata kepada seluruh warga negara, termasuk mereka yang buta huruf.***"
)
st.write(
    """
   Mengacu pada hasil Survey Sosial Ekonomi Nasional (Susenas) tahun 2021, angka buta aksara di Indonesia tinggal 1,56 persen atau 2,7 juta orang**.
    """
)

st.markdown(
    "<h3>Persentase anak usia 10 tahun ke atas buta huruf</h3>", unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 3))
pers_buta_huruf_provinsi = pd.read_csv("data/child_labor_cleaned/pers_buta_huruf_provinsi_rank.csv")
sns.barplot(x="provinsi", y="persentase", data=pers_buta_huruf_provinsi_rank, palette="Blues_d")
plt.xticks(rotation=90)
plt.title("Peringkat Provinsi Anak Usia 10 yang buta huruf")
plt.ylabel("%")
for i in ax.containers:
    ax.bar_label(i, fontsize=8)
plt.annotate(
    "Sumber: Badan Pusat Statistik (BPS)",
    (0, 0),
    (0, -150),
    fontsize=10,
    xycoords="axes fraction",
    textcoords="offset points",
    va="top",
)
st.pyplot(fig)

col1, col2 = st.columns([3, 2])
fig, ax = plt.subplots(figsize=(7, 4))
angka_buta_anak_2016 = pd.read_csv(
    "data/child_labor_cleaned/pers_buta_huruf_provinsi_rank.csv"
)
angka_buta_anak_2016.set_index("tahun", inplace=True)
angka_buta_anak_2016.plot(kind="bar", ax=ax)
plt.ylabel("%")
for i in ax.containers:
    ax.bar_label(
        i,
    )
plt.annotate(
    "Sumber: Badan Pusat Statistik (BPS)",
    (0, 0),
    (0, -50),
    fontsize=10,
    xycoords="axes fraction",
    textcoords="offset points",
    va="top",
)
col1.pyplot(fig)

col2.markdown(
    "<h5>Persentase Pekerja Anak Usia 10 yang buta huruf</h5>",
    unsafe_allow_html=True,
)
col2.write(
    """
        
    """
)

st.markdown("<h3>Sisi Gelap buta huruf Anak...</h3>", unsafe_allow_html=True)
st.write(
    """
       Keterbatasan pendidikan: Anak-anak yang buta huruf menghadapi keterbatasan dalam mengakses pendidikan. Mereka tidak dapat membaca, menulis, 
       atau menghitung dengan baik, yang membatasi kesempatan mereka untuk belajar dan berkembang secara penuh. Keterbatasan ini dapat menghambat kemajuan 
       akademik mereka 
       dan membatasi pilihan pendidikan di masa depan.
    """
)


