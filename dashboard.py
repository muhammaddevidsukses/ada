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
    "<h3>Persentase anak usia 10 tahun ke atas buta huruf</h3>", unsafe_allow_html=True
)
labor_area, labor_gender = st.tabs(["Berdasarkan Area", "Berdasarkan Jenis Kelamin"])


def plot_labor_area(area, ax):
    pers_buta_huruf_tmp = pers_buta_huruf[pers_buta_huruf["provinsi"] == area]
    sns.lineplot(x="tahun", y="persentase", data=pers_buta_huruf_tmp, marker="o", ax=ax)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_ticklabels(
        [""] + sorted(pers_buta_huruf_tmp.tahun.dt.strftime("%Y-%b"))
    )
    # create a seperator before and after 2020
    plt.axvline(x=pd.to_datetime("2020-03-02"), color="red", linestyle="--")
    fill_thresholds_min, fill_thresholds_max = (
        np.min(ax.get_yticks()) - 0.2,
        np.max(ax.get_yticks()) + 0.2,
    )
    ax.fill_between(
        ["2018-12-31", "2020-03-02"],
        fill_thresholds_min,
        fill_thresholds_max,
        color="green",
        alpha=0.2,
    )
    ax.fill_between(
        ["2020-03-02", "2021-12-31"],
        fill_thresholds_min,
        fill_thresholds_max,
        color="red",
        alpha=0.2,
    )
    ax.text(
        pd.to_datetime("2020-04"), fill_thresholds_max - 0.2, "Pandemi", style="italic"
    )
    ax.text(
        pd.to_datetime("2019"),
        fill_thresholds_max - 0.2,
        "Sebelum Pandemi",
        style="italic",
    )
    plt.ylim(fill_thresholds_min, fill_thresholds_max)
    for i, row in pers_buta_huruf_tmp.iterrows():
        ax.text(
            row["tahun"], row["persentase"] + 0.05, row["persentase"], style="italic"
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


with labor_area:
    pers_buta_huruf = pd.read_csv("data/buta_labor_cleaned/buta_huruf_gender.csv")
    pers_buta_huruf["tahun"] = pd.to_datetime(pers_buta_huruf["tahun"])
    area = st.selectbox(
        "Pilih Area",
        pers_buta_huruf.provinsi.unique(),
        index=len(pers_buta_huruf.provinsi.unique()) - 1,
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    plot_labor_area(area, ax)
    st.pyplot(fig)

    labor_area_1, labor_area_2 = st.columns(2)
    with labor_area_1:
        fig, ax = plt.subplots(figsize=(10, 5))
        plot_labor_area("SULAWESI TENGGARA", ax)
        plt.title("SULAWESI TENGGARA", fontsize=20)
        st.pyplot(fig)
        fig, ax = plt.subplots(figsize=(10, 5))
        plot_labor_area("SULAWESI BARAT", ax)
        plt.title("SULAWESI BARAT", fontsize=20)
        st.pyplot(fig)
    with labor_area_2:
        fig, ax = plt.subplots(figsize=(10, 5))
        plot_labor_area("KALIMANTAN UTARA", ax)
        plt.title("KALIMANTAN UTARA", fontsize=20)
        st.pyplot(fig)
        fig, ax = plt.subplots(figsize=(10, 5))
        plot_labor_area("SULAWESI UTARA", ax)
        plt.title("SULAWESI UTARA", fontsize=20)
        st.pyplot(fig)

with labor_gender:
    pers_buta_huruf_gender = pd.read_csv(
        "data/buta_labor_cleaned/buta_huruf_gender.csv"
    )
    pers_buta_huruf_gender["tahun"] = pd.to_datetime(
        pers_buta_huruf_gender["tahun"].astype(str)
    )
    pers_buta_huruf_laki = pers_buta_huruf_gender[
        pers_buta_huruf_gender["gender"] == "Laki-laki"
    ]
    pers_buta_huruf_perempuan = pers_buta_huruf_gender[
        pers_buta_huruf_gender["gender"] == "Perempuan"
    ]
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        x="tahun",
        y="persentase",
        data=pers_buta_huruf_laki,
        marker="o",
        color="b",
        ax=ax,
    )
    sns.lineplot(
        x="tahun",
        y="persentase",
        data=pers_buta_huruf_perempuan,
        marker="o",
        color="r",
        ax=ax,
    )
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_ticklabels(
        [""] + sorted(pers_buta_huruf_laki.tahun.dt.strftime("%Y-%b"))
    )
    # create a seperator before and after 2020
    plt.axvline(x=pd.to_datetime("2020-03-02"), color="red", linestyle="--")
    fill_thresholds_min, fill_thresholds_max = (
        np.min(ax.get_yticks()) - 0.5,
        np.max(ax.get_yticks()) + 0.2,
    )
    ax.fill_between(
        ["2018-12-31", "2020-03-02"],
        fill_thresholds_min,
        fill_thresholds_max,
        color="green",
        alpha=0.2,
    )
    ax.fill_between(
        ["2020-03-02", "2021-12-31"],
        fill_thresholds_min,
        fill_thresholds_max,
        color="red",
        alpha=0.2,
    )
    ax.text(
        pd.to_datetime("2020-04"), fill_thresholds_max - 0.2, "Pandemi", style="italic"
    )
    ax.text(
        pd.to_datetime("2019"),
        fill_thresholds_max - 0.2,
        "Sebelum Pandemi",
        style="italic",
    )
    plt.ylim(fill_thresholds_min, fill_thresholds_max)
    plt.legend(["Laki-laki", "Perempuan"])
    for i, row in pers_buta_huruf_laki.iterrows():
        ax.text(
            row["tahun"],
            row["persentase"] + 0.05,
            row["persentase"],
            style="italic",
            color="b",
        )
    for i, row in pers_buta_huruf_perempuan.iterrows():
        ax.text(
            row["tahun"],
            row["persentase"] + 0.05,
            row["persentase"],
            style="italic",
            color="r",
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

st.write(
    """
        Kurangnya akses pendidikan: Beberapa penduduk mungkin tidak memiliki akses ke fasilitas pendidikan yang memadai karena keterbatasan geografis, ekonomi, atau sosial.
        Mereka mungkin tinggal di daerah terpencil, daerah miskin, atau terkena konflik yang menghambat akses mereka ke pendidikan formal.**.
    """
)

fig, ax = plt.subplots(figsize=(10, 3))
pers_buta_huruf_rank = pd.read_csv("data/child_labor_cleaned/pers_buta_huruf_rank.csv")
sns.barplot(x="provinsi", y="persentase", data=pers_buta_huruf_rank, palette="Blues_d")
plt.xticks(rotation=90)
plt.title("Peringkat Daerah Anak Usia 10-17 Tahun Yang Bekerja 2021")
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

st.write(
    """
            Berdasarkan data peringkat diatas, daerah **Papua** memiliki persentase buta huruf tertinggi di Indonesia.
            Hal ini menunjukkan **Papua** memerlukan perhatian khusus dari pemerintah untuk menurunkan angka buta huruf.
         """
)

col1, col2 = st.columns([3, 2])
fig, ax = plt.subplots(figsize=(7, 4))
angka_pekerja_anak_2020 = pd.read_csv(
    "data/child_labor_cleaned/angka_pekerja_anak_2020.csv"
)
sns.barplot(data=angka_pekerja_anak_2020, x="kelompok", y="persentase", hue="tahun", palette="Reds_d", ax=ax)
plt.ylabel("%")
for i in ax.containers:
    ax.bar_label(
        i,
    )
plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=3)
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
    "<h5>Persentase Pekerja Anak Usia 10-17 Tahun Yang Bekerja Berdasarkan Kelompok Umur</h5>",
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


