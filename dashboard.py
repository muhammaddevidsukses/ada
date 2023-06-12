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
pers_buta_huruf_jenis = pd.read_csv("data/buta_labor_cleaned/pers_buta_huruf_jenis.csv")
pers_buta_huruf_jenis.head()
pers_anak_laki = pers_buta_huruf_jenis_melted[pers_buta_huruf_jenis_melted["gender"] == "Laki-laki"]
pers_anak_perempuan = pers_buta_huruf_jenis_melted[pers_buta_huruf_jenis_melted["gender"] == "Perempuan"]
ax = sns.lineplot(
    x="tahun",
    y="persentase",
    data=pers_anak_laki,
    marker="o",
    color="b",
    
)
sns.lineplot(
    x="tahun",
    y="persentase",
    data=pers_anak_perempuan,
    marker="o",
    color="r",
    ax=ax,
)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_ticklabels(
    [""]
    + sorted(
        pers_anak_laki.tahun.dt.strftime("%y-%b")
    )
    + sorted(
        pers_anak_perempuan.tahun.dt.strftime("%y-%b")
    )
)
# create a seperator before and after 2017
plt.axvline(x=pd.to_datetime("2016-03-02"), color="red", linestyle="--")
fill_thresholds_min, fill_thresholds_max = (
    np.min(ax.get_yticks()) - 0.2,
    np.max(ax.get_yticks()) + 0.2,
)
ax.fill_between(
    ["2014-12-31", "2016-03-02"],
    fill_thresholds_min,
    fill_thresholds_max,
    color="green",
    alpha=0.2,
)
ax.fill_between(
    ["2016-03-02", "2017-12-31"],
    fill_thresholds_min,
    fill_thresholds_max,
    color="red",
    alpha=0.2,
)
ax.text(pd.to_datetime("2014-12"), fill_thresholds_max - 0.2, "sesudah", style="italic")
ax.text(
    pd.to_datetime("2016"), fill_thresholds_max - 0.2, "Sebelum ", style="italic"
)
plt.ylim(fill_thresholds_min, fill_thresholds_max)
plt.ylabel("%")
plt.show()

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


