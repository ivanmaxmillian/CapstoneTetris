import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Dashboard setup
st.set_page_config(layout="centered")
# End of Dashboard setup

data_banjir = pd.read_excel('Data Bencana.xlsx')
data_banjir['Penyebab'].fillna(data_banjir['Kronologi & Dokumentasi'], inplace=True)

st.title('Kenapa Banjir Tidak Pernah Usai?')
st.markdown('#### Ivan Maxmillian Putra Pasaribu')
st.markdown('---')

image1 = Image.open('banjir.jpeg')
st.image(image1, caption='Gambar bencana Banjir diambil dari atas (Courtesy : Kompas.com)')

st.markdown('<div style= "text-align: justify;" >Banjir tidak pernah luput setiap tahunnya. \
    Banjir menjadi masalah yang selalu ada setiap tahunnya. Berita bencana banjir selalu muncul di media massa, \
    bahkan kita sering dengar ada daerah yang seakan sudah `menormalkan` banjir karena terlalu sering terjadi. \
    Berdasarkan data dari Badan Nasional Penanggulangan Bencana (BNPB), \
    Banjir di Indonesia meningkat dari adanya 1101 kejadian pada 2010\
    menjadi 1932 kasus pada 2021.\
    Lebih dari 6 juta rumah pernah terendam dan lebih dari 42 ribu orang tercatat \
    menjadi korban dari bencana banjir di seluruh Indonesia.\
    Banjir cenderung meningkat seperti grafik dibawah ini.</div>', unsafe_allow_html=True)

#BANJIR pertahun
banjir_perthn = pd.Series.to_frame(data_banjir['Kejadian'].groupby(data_banjir['Tanggal Kejadian'].dt.year).agg('count'))
banjir_perthn = banjir_perthn.iloc[0:12, :]
banjir_perthn = banjir_perthn.rename({'Kejadian': 'Jml Bencana Banjir'}, axis =1)
#BANJIR pertahun END

st.line_chart(banjir_perthn)

plotbjr1, plotbjr2 = st.columns(2)
with plotbjr1:
    image2 = Image.open('Penyebab Banjir.png')
    st.image(image2, width=350, caption='Keterangan Penyebab Banjir berdasarkan Data BNPB')
with plotbjr2:
    st.markdown('<div style= "text-align: justify;" >Berdasarkan data BNPB, penyebab dan/atau keterangan\
        bencana banjir sangat beragam dan dapat dilihat ada beberapa\
        kata yang sering muncul pada bubble word disamping, seperti hujan, intensitas tinggi, dll.\
        Secara visual dapat ditarik kesimpulan bahwa menurut data BNPB, \
        penyebab banjir di Indonesia adalah intensitas hujan yang tinggi.</div>', unsafe_allow_html=True)


st.markdown('<div style= "text-align: justify;" >Seberapa parah/tinggikah hujan Indonesia sehingga\
    dapat menyebabkan banjir secara terus menerus? Berdasarkan data dari Climate Change Knowledge Portal\
    (CCKP), terlihat bahwa sepanjang 10 tahun terakhir curhah hujan secara umum di Indonesia\
    tidak mengalami banyak perubahan dan cenderung menurun, tetapi banjir masih terus meningkat.</div>', unsafe_allow_html=True)

#Data Curah Hujan
data = pd.read_csv("pr_timeseries_monthly_cru_202208011058.csv")
av_col = data[data['annual']>2009]
av_col = pd.Series.to_frame(av_col.mean(axis=0))
av_col = av_col.reset_index()
bulanan = av_col.iloc[1:13, :]
# Data Curah Hujan End

#PLOT 10 tahun terakhir
data_annual = data[['annual', 'total']]
last10years = data_annual[data_annual['annual']>2009]
last10years = last10years.set_index('annual')
last10years = last10years.rename({'total': 'Intensitas Hujan dalam mm'}, axis =1)

st.line_chart(last10years)

st.markdown('<div style= "text-align: justify;" >Dengan adanya data diatas,\
    apakah data BNPB yang menyebutkan bahwa hujan merupakan penyabab banjir terbanyak itu benar?\
    Rasanya tidak. </div>', unsafe_allow_html=True)

st.markdown('### Lantas mengapa banjir masih kerap terjadi?')
st.markdown('---')

st.markdown('<div style= "text-align: justify;" >Apakah ada alasan lain? Mari kita ambil tiga sampel daerah yang paling sering mengalami\
    bencana banjir berdasarkan data BNPB sepanjang 2010-2022, yaitu Bandung (288 kejadian), Bogor (220 kejadian), dan \
    Cilacap (171 kejadian) untuk melihat kecenderungan terjadinya bencana banjir berdasarkan faktor\
    KEPADATAN PENDUDUK dan LOKASI BANJIR.\
    Apakah peningkatan jumlah penduduk berpengaruh kepada kejadian banjir, dan apakah ada ciri khusus\
    dari lokasi terjadinya banjir di Indonesia.</div>', unsafe_allow_html=True)

#BANDUNG BANDUNG BANDUNG BANDUNG BANDUNG BANDUNG
st.markdown('#### Bandung')

banjir_bandung = data_banjir[data_banjir['Kabupaten'] == 'BANDUNG']
banjir_bdg_pertahun = banjir_bandung.pivot_table(values='Kejadian', index='Tanggal Kejadian', aggfunc='count')
banjir_bdg_pertahun = banjir_bdg_pertahun.reset_index()
banjir_bdg_pertahun = banjir_bdg_pertahun.groupby(banjir_bdg_pertahun['Tanggal Kejadian'].dt.year)['Kejadian'].sum()

jbr = pd.read_csv('disdukcapil-2-od_17020_kepadatan_penduduk_berdasarkan_kabupatenkota_data.csv')
bandung = jbr[jbr['nama_kabupaten_kota'] == 'KABUPATEN BANDUNG']
bandung = bandung[['tahun', 'kepadatan_penduduk']]
bandung = bandung.iloc[1:, :]

banjirbandung, teksbanjirbdg = st.columns([3,1])
with banjirbandung:
    fig1 = plt.figure(figsize=(10,6))
    plt.xlabel("Tahun", size=16)
    plt.ylabel("Jumlah Kasus Banjir Bandung", size=16)
    plt.title("Banjir Bandung 2010-2021", size=20)
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.plot(banjir_bdg_pertahun)
    st.pyplot(fig1)
with teksbanjirbdg:
    st.markdown('<div style= "text-align: justify;" >Banjir di Kab.Bandung terlihat naik dan turun\
    setiap tahunnya. Tahun-tahun dengan kejadian tertinggi terjadi pada 2010 (lebih dari 60 bencana)\
    dan 2013 (lebih darir 50 bencana)<. Namun, secara keseluruhan banjir di Bandung masih fluktuatif.</div>', unsafe_allow_html=True)

pendudukbdg, tekspendudukbdg = st.columns([3,1])
with pendudukbdg:
    fig2 = plt.figure(figsize=(10,6))
    plt.xlabel("Tahun", size=16)
    plt.ylabel("Kepadatan Penduduk Bandung per km2", size=16)
    plt.title("Kepadatan Penduduk Bandung 2014-2021", size=20)
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.plot(bandung['tahun'], bandung['kepadatan_penduduk'])
    st.pyplot(fig2)
with tekspendudukbdg:
    st.markdown('<div style= "text-align: justify;" >Penduduk di Kab.Bandung terlihat semakin padat\
        setiap tahunnya, mulai dari sekitar 1975 penduduk per km2 tahun 2013\
        hingga 2055 penduduk per km2 pada 2021</div>', unsafe_allow_html=True)

st.markdown('<div style= "text-align: justify;" >Dari data diatas, kepadatan penduduk tidak searah\
    dengan kasus banjir yang terjadi di Bandung. Bagaimana dengan lokasi bencana? Dari 288 kejadian bencana banjir di Bandung,\
    ada 86 kejadian yang tercatat secara lengkap lokasi/daerahnya oleh BNPB. Dari 86 kasus tersebut,\
    61 diantaranya (atau 71%) terjadi di 3 daerahh, Kec. Baleendah, Kec. Bojongsoang , dan Kec. Dayeuhkolot.</div>', unsafe_allow_html=True)

bdg1, bdg2, bdg3 = st.columns(3)
with bdg1:
    image3 = Image.open('Baleendah.png')
    st.image(image3, caption='Baleendah, Bandung')
with bdg2:
    image4 = Image.open('Bojongsoang.png')
    st.image(image4, caption='Bojongsoang, Bandung')
with bdg3:
    image5 = Image.open('DayeuhKolot.png')
    st.image(image5, caption='DayeuhKolot, Bandung')

st.write('<div style= "text-align: justify;" >Ketiga daerah tersebut memiliki kesamaan yang terlihat \
    pada gambar, dilewati oleh Sungai Citarum.</div>', unsafe_allow_html=True)

url1= "https://www.detik.com/jabar/berita/d-6048748/luapan-citarum-rendam-3-kecamatan-di-kabupaten-bandung"
st.write("[Berita terbaru](%s) juga mendukung hal tersebut. Lalu, Bagimana dengan daerah lainnya?" % url1)

#BOGOR BOGOR BOGOR BOGOR BOGOR BOGOR
st.markdown('#### Bogor')

url2 = "https://banten.tribunnews.com/2022/03/01/luapan-sungai-di-ciomas-merendam-rumah-warga-jembatan-banjir-akses-jalan-terputus"

banjir_bogor = data_banjir[data_banjir['Kabupaten'] == 'BOGOR']
banjir_bgr_pertahun = banjir_bogor.pivot_table(values='Kejadian', index='Tanggal Kejadian', aggfunc='count')
banjir_bgr_pertahun = banjir_bgr_pertahun.reset_index()
banjir_bgr_pertahun = banjir_bgr_pertahun.groupby(banjir_bgr_pertahun['Tanggal Kejadian'].dt.year)['Kejadian'].sum()

bogor = jbr[jbr['nama_kabupaten_kota'] == 'KABUPATEN BOGOR']
bogor = bogor[['tahun', 'kepadatan_penduduk']]

banjirbogor, teksbanjirbgr = st.columns([3,1])
with banjirbogor:
    fig3 = plt.figure(figsize=(10,6))
    plt.xlabel("Tahun", size=16)
    plt.ylabel("Jumlah Kasus Banjir Bogor", size=16)
    plt.title("Banjir Bogor 2010-2021", size=20)
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.plot(banjir_bgr_pertahun)
    st.pyplot(fig3)
with teksbanjirbgr:
    st.markdown('<div style= "text-align: justify;" >Berbeda dengan Bandung, bencana\
        banjir di Kab.Bogor cenderung terus meningkat meskipun tidak terlalu drastis,\
        tetapi terjadi lonjakan hingga 70 bencana pada 2021. Meskipun demikian, hingga Juli 2022 (separuh tahun 2022),\
        bencana banjir di Bogor baru terjadi 18 kali sehingga ada kemungkinan kembali menurun.\</div>', unsafe_allow_html=True)

pendudukbogor, tekspendudukbgr = st.columns([3,1])
with pendudukbogor:
    fig4 = plt.figure(figsize=(10,6))
    plt.xlabel("Tahun", size=16)
    plt.ylabel("Kepadatan Penduduk Bogor per km2", size=16)
    plt.title("Kepadatan Penduduk Bogor 2013-2021", size=20)
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.plot(bogor['tahun'], bogor['kepadatan_penduduk'])
    st.pyplot(fig4)
with tekspendudukbgr:
    st.markdown('<div style= "text-align: justify;" >Dibandingkan dengan Bandung (sebelumnya), \
    peningkatan kepadatan penduduk Kab.Bogor jauh lebih drastis. Pada 2013 sebanyak 1263 per km2, \
    dan pada 2020 mencapai 1965 per km2 (meningkat sekitar 55%).</div>', unsafe_allow_html=True)

st.markdown('<div style= "text-align: justify;" >Dari data diatas, peningkatan\
    penduduk yang drastis tidak terlalu berpengaruh terhadap bencana banjir.\
    Berdasarkan daerahnya, 146 dari total 220 bencana banjir berhasil tercatat\
    lokasinya oleh BNPB, dengan 40 (27%) diantaranya terjadi di Kec. Cibinong, Kec.Bojonggede, dan Kec. Ciomas yang\
    dilewati oleh Sungai Ciliwung.</div>', unsafe_allow_html=True)
st.write('Daerah lainnya, misalkan [Kec. Ciomas](%s) (9 kejadian banjir tercatat), \
    juga dilewati banyak anak sungai.' % url2)

bgr1, bgr2, bgr3 = st.columns(3)
with bgr1:
    image6 = Image.open('Cibinong.png')
    st.image(image6, caption='Cibinong, Bogor')
with bgr2:
    image7 = Image.open('Bojonggede.png')
    st.image(image7, caption='Bojonggede, Bogor')
with bgr3:
    image8 = Image.open('Cisarua.png')
    st.image(image8, caption='Cisarua, Bogor')

st.markdown('<div style= "text-align: justify;" >Mirip seperti Bandung,\
    beberapa daerah yang paling sering terkena Banjir di Bogor ini dilewati oleh Sungai\
    Ciliwung. Mari kita lihat kabupaten terakhir, Cilacap.</div>', unsafe_allow_html=True)

#Cilacap Cilacap Cilacap Cilacap Cilacap Cilacap
st.markdown('#### Cilacap')

banjir_cilacap = data_banjir[data_banjir['Kabupaten'] == 'CILACAP']
banjir_clp_pertahun = banjir_cilacap.pivot_table(values='Kejadian', index='Tanggal Kejadian', aggfunc='count')
banjir_clp_pertahun = banjir_clp_pertahun.reset_index()
banjir_clp_pertahun = banjir_clp_pertahun.groupby(banjir_clp_pertahun['Tanggal Kejadian'].dt.year)['Kejadian'].sum()
clp = pd.read_excel("kepadatanCilacap.xlsx")

banjirclp, teksbanjirclp = st.columns([3,1])
with banjirclp:
    fig3 = plt.figure(figsize=(10,6))
    plt.xlabel("Tahun", size=16)
    plt.ylabel("Jumlah Kasus Banjir Cilacap", size=16)
    plt.title("Banjir Cilacap 2010-2021", size=20)
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.plot(banjir_clp_pertahun)
    st.pyplot(fig3)
with teksbanjirclp:
    st.markdown('<div style= "text-align: justify;" >Banjir di Cilacap dari tahun ke tahun\
        cenderung fluktuatif di kisaran 5 hingga 25 kejadian per tahun. </div>', unsafe_allow_html=True)

pendudukclp, tekspendudukclp = st.columns([3,1])
with pendudukclp:
    fig5 = plt.figure(figsize=(10,6))
    plt.xlabel("Tahun", size=16)
    plt.ylabel("Kepadatan Penduduk Cilacap per km2", size=16)
    plt.title("Kepadatan Penduduk Cilacap 2010-2021", size=20)
    plt.xticks(size=12)
    plt.yticks(size=12)
    plt.plot(clp['Tahun'], clp['Kepadatan Penduduk/km2'])
    st.pyplot(fig5)
with tekspendudukclp:
    st.markdown('<div style= "text-align: justify;" >Berbeda dengan jumlah kasus bencana banjir, \
    kepadatan penduduk Cilacap cenderung terus meningkat dari 818 penduduk per km2 hingga 873 per km2 dan pernah\
    menyentuh 900 penduduk per km2 sepanjang perjalanannya.</div>', unsafe_allow_html=True)


st.markdown('<div style= "text-align: justify;" >Kejadian banjir di Cilacap tidak sesering\
    di Bandung dan Bogor, begitu juga dengan kepadatan penduduk Cilacap tidak sepadat di\
    Bandung dan Bogor. Tetapi bagaimana dengan lokasi banjir di Cilacap?\
    Dari 171 data bencana banjir di Cilacap,\
    hanya 61 kejadian yang tercatat lokasinya, dan dari 61 kejadian tersebut, 31 (51%) diantaranya terjadi di\
    3 kecamatan, Kec. Wanareja, Kec. Sidareja, dan Kec. Majenang </div>', unsafe_allow_html=True)

clp1, clp2, clp3 = st.columns(3)
with clp1:
    image6 = Image.open('Wanareja.png')
    st.image(image6, caption='Wanareja, Cilacap')
with clp2:
    image7 = Image.open('Sidareja.png')
    st.image(image7, caption='Bojonggede, Cilacap')
with clp3:
    image8 = Image.open('Majenang.png')
    st.image(image8, caption='Majenang, Cilacap')

st.markdown('<div style= "text-align: justify;" >Beberapa sungai kecil pun dapat menyebabkan banjir\
    seperti yang terjadi di Cilacap ini. </div>', unsafe_allow_html=True)

url3= "https://jateng.tribunnews.com/2022/02/14/banjir-rutinan-di-dusun-cikalong-sidareja-baru-surut-subuh-tadi"
st.write('Beberapa kejadian bahkan disebut sebagai [banjir rutin](%s)'% url3)

st.markdown('---')
st.markdown('<div style= "text-align: justify;" >Dari seluruh data diatas,\
    kejadian banjir di 3 sampel daerah di Indonesia cenderung fluktuatif dan tidak mutlak\
    berbanding lurus dengan peningkatan kepadatan penduduk. Namun, ada hal yang identik dari ketiga\
    daerah tersebut yaitu daerah yang paling sering terdampak banjir adalah daerah yang dilewati,\
    dikelilingi, atau dilintasi oleh aliran sungai besar.\
    Hal ini menunjukkan bahwa faktor hujan dan kepadatan penduduk bukanlah yang utama dari penyebab banjir, melainkan\
    lokasi daerah dekat dengan sungai yang paling sering terkena banjir sehingga\
    asumsi yang dapat diambil adalah adanya tata kelola yang salah dengan daerah sekitar sungai. </div>', unsafe_allow_html=True)
st.markdown('')
st.markdown('<div style= "text-align: justify;" >BAGI PEMERINTAH, terutama pemerintah daerah masing-masing,\
    diperlukan adanya upaya yang konkrit untuk mengatas permasalah sungai-sungai penyebab banjir.\
    Banyak faktor pendukung, seperti sampah yang dibuang disungai, sungai yang mendangkal akibat lumpur, \
    dan lain sebagainya. Hal-hal tersebut harus menjadi fokus untuk mengatasi banjir.</div>', unsafe_allow_html=True)
st.markdown('')
st.markdown('<div style= "text-align: justify;" >    BAGI MASYARAKAT, kedepannya perlu diperhatikan lingkungan pemukiman yang akan ditempati apakah\
    memiliki dekat dengan sungai yang memiliki peluang banjir yang berulang.\
    Kesadaran masyarakat untuk membantu menjaga aliran sungai tetap baik juga dapat membantu\
    mengatasi banjir. </div>', unsafe_allow_html=True)
