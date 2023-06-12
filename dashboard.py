import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

labor_area, labor_gender = st.tabs(["Berdasarkan Area", "Berdasarkan Jenis Kelamin"])

with labor_area:
    anak_buta = pd.read_csv("data/buta_labor_cleaned/anak_buta.csv")
anak_buta["tahun"] = pd.to_datetime(anak_buta["tahun"].astype(str))
anak_buta.set_index("tahun", inplace=True)
area = st.selectbox(
"Pilih Area",
anak_buta.columns.unique(),
index=len(anak_buta.columns.unique()) - 1,
    )
fig, ax = plt.subplots(figsize=(10, 5))
anak_buta[area].plot(marker="o", ax=ax)
# create a seperator before and after 2016
plt.axvline(
    x="2015",
    color="red",
    linestyle="--")
fill_thresholds_min, fill_thresholds_max = (
np.min(ax.get_yticks()) - 0.2,
np.max(ax.get_yticks()) + 0.2,
    )
ax.fill_between(
anak_buta.index[:3],
fill_thresholds_min,
fill_thresholds_max,
color="green",
alpha=0.2,
    )
ax.fill_between(
anak_buta.index[:2],
fill_thresholds_min,
fill_thresholds_max,
color="red",
alpha=0.2,
    )

ax.text("2016", fill_thresholds_max - 0.15, "sesusah", style="italic")
ax.text("2014", fill_thresholds_max - 0.15, "Sebelum ", style="italic")
for i, value in enumerate(anak_buta[area]):
    ax.text(
   anak_buta.index[i],
    value+0.05,
    value,style="italic")
plt.ylabel("%")
plt.annotate(
"Sumber: Badan Pusat Statistik (BPS)",
(0, 0),
(0, -35),
fontsize=10,
xycoords="axes fraction",
textcoords="offset points",
va="top",
    )
st.pyplot(fig)
with labor_gender:
    anak_buta_gender= pd.read_csv("data/buta_labor_cleaned/pers_anak_buta_gender.csv")
anak_buta_gender["tahun"] = pd.to_datetime(anak_buta_gender["tahun"].astype(str))
anak_buta_gender.set_index("tahun", inplace=True)
fig, ax = plt.subplots(figsize=(10, 5))
anak_buta_gender["Laki-laki"].plot(marker="o", color="b", ax=ax)
anak_buta_gender["Perempuan"].plot(marker="o", color="r", ax=ax)
# create a seperator before and after 2016
plt.axvline(x="2015", color="red", linestyle="--")
fill_thresholds_min, fill_thresholds_max = (
np.min(ax.get_yticks()) - 0.2,
np.max(ax.get_yticks()) + 0.2,
    )
ax.fill_between(
anak_buta.index[:3],
        fill_thresholds_min,
        fill_thresholds_max,
        color="green",
        alpha=0.2,)



ax.legend(["Laki-laki", "Perempuan"])
# create text top left
ax.text("2017", 3.6, "sesudah", style="italic")
ax.text("2015", 3.6, "Sebelum ", style="italic")
for i, value in enumerate(anak_buta_gender["Laki-laki"]):ax.text(anak_buta.index[i], value + 0.05, value, style="italic", color="blue"
        )
for i, value in enumerate(anak_buta_gender["Perempuan"]):ax.text(anak_buta.index[i], value - 0.15, value, style="italic", color="red"
        )
plt.ylabel("%")
plt.annotate(
"Sumber: Badan Pusat Statistik (BPS)",
(0, 0),
(0, -35),
fontsize=10,
xycoords="axes fraction",
textcoords="offset points",
va="top",
    )
st.pyplot(fig)


st.markdown("<h5>Persentase Anak Usia 10 yang buta huruf</h5>", unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 3))
buta_huruf_rank = pd.read_csv("data/buta_labor_cleaned/pers_buta_huruf_provinsi_rank.csv")
sns.barplot(x="provinsi", y="persentase", data=buta_huruf_rank, palette="Blues_d")
plt.xticks(rotation=90)
plt.title("Peringkat Provinsi Anak Usia 10 yang Buta Huruf Terbanyak")
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

st.markdown("<h3>Sisi Gelap buta huruf Anak...</h3>", unsafe_allow_html=True)
st.write(
    """
       Keterbatasan pendidikan: Anak-anak yang buta huruf menghadapi keterbatasan dalam mengakses pendidikan. Mereka tidak dapat membaca, menulis, 
       atau menghitung dengan baik, yang membatasi kesempatan mereka untuk belajar dan berkembang secara penuh. Keterbatasan ini dapat menghambat kemajuan 
       akademik mereka 
       dan membatasi pilihan pendidikan di masa depan.
    """
)


