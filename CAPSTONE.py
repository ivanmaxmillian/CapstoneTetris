import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from PIL import Image

# Dashboard setup
st.set_page_config(layout="centered")
# End of Dashboard setup

data_banjir = pd.read_excel('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Data Bencana.xlsx')
data_banjir['Penyebab'].fillna(data_banjir['Kronologi & Dokumentasi'], inplace=True)

st.title('Melihat Lebih Luas Banjir Indonesia')
st.markdown('### Ivan Maxmillian Putra Pasaribu')
st.markdown('---')

image1 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/banjir.jpeg')
st.image(image1, caption='Gambar bencana Banjir diambil dari atas (Courtesy : Kompas.com)')

st.markdown('##### <div style= "text-align: justify;" > Intensitas hujan yang tinggi hanya faktor pendukung penyebab banjir Indonesia. Faktor utama ialah \
sungai besar yang melintasi suatu daerah sehingga hujan mendukung meluapnya air ke permukaan.</div>', unsafe_allow_html=True)

st.markdown('<div style= "text-align: justify;" >Banjir tidak pernah luput setiap tahunnya. \
    Berdasarkan data dari Badan Nasional Penanggulangan Bencana (BNPB), \
    Banjir di Indonesia meningkat dari adanya 1101 kejadian pada 2010\
    menjadi 1932 kasus pada 2021.\
    Lebih dari 6 juta rumah pernah terendam dan lebih dari 42 ribu orang tercatat \
    menjadi korban dari bencana banjir di seluruh Indonesia.\
    Data BNPB menyebutkan penyebab banjir di Indonesia didominasi oleh \'intensitas hujan yang tinggi\'.</div>', unsafe_allow_html=True)

#BANJIR pertahun
banjir_perthn = pd.Series.to_frame(data_banjir['Kejadian'].groupby(data_banjir['Tanggal Kejadian'].dt.year).agg('count'))
banjir_perthn = banjir_perthn.reset_index()
banjir_perthn = banjir_perthn.iloc[0:12, :]
#BANJIR pertahun END

plotbjr1, plotbjr2 = st.columns(2)
with plotbjr1:
    fig1 = plt.figure(figsize = (18, 18))
    plt.bar(banjir_perthn['Tanggal Kejadian'], banjir_perthn['Kejadian'], color ='maroon',
            width = 0.4)
    plt.xlabel("Tahun", size=20)
    plt.ylabel("Jumlah Kasus Banjir", size=20)
    plt.title("Banjir Tahunan Indonesia 2010-2021", size=25)
    plt.xticks(size=16)
    plt.yticks(size=16)
    st.pyplot(fig1)
with plotbjr2:
    image2 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Penyebab Banjir.png')
    st.image(image2, width=350, caption='Keterangan Penyebab Banjir berdasarkan Data BNPB')

st.markdown('<div style= "text-align: justify;" >Seberapa parahkah hujan Indonesia sehingga\
    dapat menyebabkan banjir secara terus menerus? Berdasarkan data dari Climate Change Knowledge Portal\
    (CCKP), secara rata-rata, curah hujan Indonesia cukup tinggi mulai bulan November\
    hingga bulan Maret dengan nilai precipitation lebih dari 250mm tetapi masih dalam kategori normal. \
    Namun, secara kasar selama 10 tahun terakhir, curah hujan di Indonesia terlihat menurun \
    seperti grafik dibawah ini.</div>', unsafe_allow_html=True)

#Data Curah Hujan
data = pd.read_csv("C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/SQL/datasets/pr_timeseries_monthly_cru_202208011058.csv")
av_col = data[data['annual']>2009]
av_col = pd.Series.to_frame(av_col.mean(axis=0))
av_col = av_col.reset_index()
x = av_col.iloc[1:13, :]
# Data Curah Hujan End

plothujan1, plothujan2 = st.columns(2)
with plothujan1:
    #PLOT 10 tahun terakhir
    data_annual = data[['annual', 'total']]
    last10years = data_annual[data_annual['annual']>2009]
    fig3=plt.figure(figsize=(10,6))
    plt.plot(last10years['annual'], last10years['total'])
    plt.title('Intensitas Hujan Tahunan Indonesia 2010-2020', size=16)
    plt.ylabel('Precipitation (mm)', size=14)
    plt.xlabel('Tahun')
    st.pyplot(fig3)
    #PLOT 10 tahun terakhir END
with plothujan2:
    # Plot BULANAN
    fig2 = plt.figure(figsize=(10,6))
    plt.bar(x['index'], x[0])
    plt.title('Rata-rata Intensitas Hujan Indonesia Setiap Bulan 2010-2020', size=16)
    plt.ylabel('Precipitation (mm)', size=14)
    plt.xlabel('Bulan')
    st.pyplot(fig2)
    # Plot BULANAN END

st.markdown('<div style= "text-align: justify;" >Apabila dilihat dari kasus banjir setiap tahun\
    dan rata-rata tingkat intensitas hujan, maka dapat dilihat bahwa secara umum banjir meningkat, namun\
    intensitas hujan menurun.</div>', unsafe_allow_html=True)
st.markdown('### Lantas mengapa banjir masih kerap terjadi?')
st.markdown('---')

st.markdown('<div style= "text-align: justify;" >Agar lebih jelas, mari kita ambil tiga sampel daerah yang paling sering mengalami\
    bencana banjir berdasarkan data BNPB sepanjang 2010-2022, yaitu Bandung (288 kejadian), Bogor (220 kejadian), dan \
    Cilacap (171 kejadian).</div>', unsafe_allow_html=True)

#BANDUNG BANDUNG BANDUNG BANDUNG BANDUNG BANDUNG
st.markdown('#### Bandung')

st.markdown('<div style= "text-align: justify;" >Dari 288 kejadian bencana banjir di Bandung,\
    ada 86 kejadian yang tercatat secara lengkap lokasi/daerahnya oleh BNPB. Dari 86 kasus tersebut,\
    61 diantaranya (atau 71%) terjadi di 3 daerahh, Kec. Baleendah, Kec. Bojongsoang , dan Kec. Dayeuhkolot.</div>', unsafe_allow_html=True)

bdg1, bdg2, bdg3 = st.columns(3)
with bdg1:
    image3 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Baleendah.png')
    st.image(image3, caption='Baleendah, Bandung')
with bdg2:
    image4 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Bojongsoang.png')
    st.image(image4, caption='Bojongsoang, Bandung')
with bdg3:
    image5 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/DayeuhKolot.png')
    st.image(image5, caption='DayeuhKolot, Bandung')

st.write('<div style= "text-align: justify;" >Ketiga daerah tersebut memiliki kesamaan yang terlihat \
    pada gambar, dilewati oleh Sungai Citarum.</div>', unsafe_allow_html=True)

url1= "https://www.detik.com/jabar/berita/d-6048748/luapan-citarum-rendam-3-kecamatan-di-kabupaten-bandung"
st.write("[Berita terbaru](%s) juga mendukung hal tersebut. Lalu, Bagimana dengan daerah lainnya?" % url1)

#BOGOR BOGOR BOGOR BOGOR BOGOR BOGOR
st.markdown('#### Bogor')

url2 = "https://banten.tribunnews.com/2022/03/01/luapan-sungai-di-ciomas-merendam-rumah-warga-jembatan-banjir-akses-jalan-terputus"

st.markdown('<div style= "text-align: justify;" >146 dari total 220 bencana banjir berhasil tercatat\
    lokasinya oleh BNPB, dengan 40 (27%) diantaranya terjadi di Kec. Cibinong, Kec.Bojonggede, dan Kec. Ciomas yang\
    dilewati oleh Sungai Ciliwung.</div>', unsafe_allow_html=True)
st.write('Daerah lainnya, misalkan [Kec. Ciomas](%s) (9 kejadian banjir tercatat), \
    juga dilewati banyak anak sungai.' % url2)

bgr1, bgr2, bgr3 = st.columns(3)
with bgr1:
    image6 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Cibinong.png')
    st.image(image6, caption='Cibinong, Bogor')
with bgr2:
    image7 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Bojonggede.png')
    st.image(image7, caption='Bojonggede, Bogor')
with bgr3:
    image8 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Cisarua.png')
    st.image(image8, caption='Cisarua, Bogor')

st.markdown('<div style= "text-align: justify;" >Mirip seperti Bandung,\
    beberapa daerah yang paling sering terkena Banjir di Bogor ini dilewati oleh Sungai\
    Ciliwung. Mari kita lihat kabupaten terakhir, Cilacap.</div>', unsafe_allow_html=True)

#Cilacap Cilacap Cilacap Cilacap Cilacap Cilacap
st.markdown('#### Cilacap')

st.markdown('<div style= "text-align: justify;" >Meskipun ada 171 data bencana banjir di Cilacap,\
    hanya 61 kejadian yang tercatat lokasinya, dan dari 61 kejadian tersebut, 31 (51%) diantaranya terjadi di\
    3 kecamatan, Kec. Wanareja, Kec. Sidareja, dan Kec. Majenang </div>', unsafe_allow_html=True)

clp1, clp2, clp3 = st.columns(3)
with clp1:
    image6 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Wanareja.png')
    st.image(image6, caption='Wanareja, Cilacap')
with clp2:
    image7 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Sidareja.png')
    st.image(image7, caption='Bojonggede, Cilacap')
with clp3:
    image8 = Image.open('C:/Users/ivanm/Documents/DOCUMENTS/BELAJAR/TETRIS/Project/Majenang.png')
    st.image(image8, caption='Majenang, Cilacap')

st.markdown('<div style= "text-align: justify;" >Beberapa sungai kecil pun dapat menyebabkan banjir\
    seperti yang terjadi di Cilacap ini. </div>', unsafe_allow_html=True)

url3= "https://jateng.tribunnews.com/2022/02/14/banjir-rutinan-di-dusun-cikalong-sidareja-baru-surut-subuh-tadi"
st.write('Beberapa kejadian bahkan disebut sebagai [banjir rutin](%s)'% url3)

st.markdown('---')
st.markdown('<div style= "text-align: justify;" >Dari beberapa sampel daerah diatas,\
    membuktikan bahwa faktor utama penyebab banjir adalah wilayah sekitar sungai yang\
    didorong meluap oleh hujan deras, oleh karena itu kita tidak dapat menyalahkan hujan sepenuhnya.</div>', unsafe_allow_html=True)
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
