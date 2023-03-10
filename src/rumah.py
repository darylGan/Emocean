import streamlit as st
from track_utils import add_prediction_details
from datetime import datetime
import pandas as pd
import numpy as np
import neattext as nt
from neattext.functions import clean_text
from imblearn.pipeline import Pipeline, make_pipeline
import joblib
from sklearn.feature_extraction import text 

def space(num_lines=1):
    for _ in range(num_lines):
        st.write("")

st.set_option('deprecation.showPyplotGlobalUse', False)

#Stop Words
malay_stop_words = ["abdul","abdullah","acara","ada","adalah","ahmad","air","akan","akhbar","akhir","aktiviti","alam","amat", "amerika","anak","anggota","antara","antarabangsa","apa","apabila","april","as","asas","asean","asia","asing","atas","atau","australia","awal","awam","bagaimanapun","bagi","bahagian","bahan","baharu","bahawa","baik","bandar","bank","banyak","barangan","baru","baru-baru","bawah","beberapa","bekas","beliau","belum","berada","berakhir","berbanding","berdasarkan","berharap","berikutan","berjaya","berjumlah","berkaitan","berkata","berkenaan","berlaku","bermula","bernama","bernilai","bersama","berubah","besar","bhd","bidang","bilion","bn","boleh","bukan","bulan","bursa","cadangan","china","dagangan","dalam","dan","dana","dapat","dari","daripada","dasar","datang","datuk","demikian","dengan","depan","derivatives","dewan","di","diadakan","dibuka","dicatatkan","dijangka","diniagakan","dis","disember","ditutup","dolar","dr","dua","dunia","ekonomi","eksekutif","eksport","empat","enam","faedah","feb","global","hadapan","hanya","harga","hari","hasil","hingga","hubungan","ia","iaitu","ialah","indeks","india","indonesia","industri","ini","islam","isnin","isu","itu","jabatan","jalan","jan","jawatan","jawatankuasa","jepun","jika","jualan","juga","julai","jumaat","jumlah","jun","juta","kadar","kalangan","kali","kami","kata","katanya","kaunter","kawasan","ke","keadaan","kecil","kedua","kedua-dua","kedudukan","kekal","kementerian","kemudahan","kenaikan","kenyataan","kepada","kepentingan","keputusan","kerajaan","kerana","kereta","kerja","kerjasama","kes","keselamatan","keseluruhan","kesihatan","ketika","ketua","keuntungan","kewangan","khamis","kini","kira-kira","kita","klci","klibor","komposit","kontrak","kos","kuala","kuasa","kukuh","kumpulan","lagi","lain","langkah","laporan","lebih","lepas","lima","lot","luar","lumpur","mac","mahkamah","mahu","majlis","makanan","maklumat","malam","malaysia","mana","manakala","masa","masalah","masih","masing-masing","masyarakat","mata","media","mei","melalui","melihat","memandangkan","memastikan","membantu","membawa","memberi","memberikan","membolehkan","membuat","mempunyai","menambah","menarik","menawarkan","mencapai","mencatatkan","mendapat","mendapatkan","menerima","menerusi","mengadakan","mengambil","mengenai","menggalakkan","menggunakan","mengikut","mengumumkan","mengurangkan","meningkat","meningkatkan","menjadi","menjelang","menokok","menteri","menunjukkan","menurut","menyaksikan","menyediakan","mereka","merosot","merupakan","mesyuarat","minat","minggu","minyak","modal","mohd","mudah","mungkin","naik","najib","nasional","negara","negara-negara","negeri","niaga","nilai","nov","ogos","okt","oleh","operasi","orang","pada","pagi","paling","pameran","papan","para","paras","parlimen","parti","pasaran","pasukan","pegawai","pejabat","pekerja","pelabur","pelaburan","pelancongan","pelanggan","pelbagai","peluang","pembangunan","pemberita","pembinaan","pemimpin","pendapatan","pendidikan","penduduk","penerbangan","pengarah","pengeluaran","pengerusi","pengguna","pengurusan","peniaga","peningkatan","penting","peratus","perdagangan","perdana","peringkat","perjanjian","perkara","perkhidmatan","perladangan","perlu","permintaan","perniagaan","persekutuan","persidangan","pertama","pertubuhan","pertumbuhan","perusahaan","peserta","petang","pihak","pilihan","pinjaman","polis","politik","presiden","prestasi","produk","program","projek","proses","proton","pukul","pula","pusat","rabu","rakan","rakyat","ramai","rantau","raya","rendah","ringgit","rumah","sabah","sahaja","saham","sama","sarawak","satu","sawit","saya","sdn","sebagai","sebahagian","sebanyak","sebarang","sebelum","sebelumnya","sebuah","secara","sedang","segi","sehingga","sejak","sekarang","sektor","sekuriti","selain","selama","selasa","selatan","selepas","seluruh","semakin","semalam","semasa","sementara","semua","semula","sen","sendiri","seorang","sepanjang","seperti","sept","september","serantau","seri","serta","sesi","setiap","setiausaha","sidang","singapura","sini","sistem","sokongan","sri","sudah","sukan","suku","sumber","supaya","susut","syarikat","syed","tahap","tahun","tan","tanah","tanpa","tawaran","teknologi","telah","tempat","tempatan","tempoh","tenaga","tengah","tentang","terbaik","terbang","terbesar","terbuka","terdapat","terhadap","termasuk","tersebut","terus","tetapi","thailand","tiada","tidak","tiga","timbalan","timur","tindakan","tinggi","tun","tunai","turun","turut","umno","unit","untuk","untung","urus","usaha","utama","walaupun","wang","wanita","wilayah","yang","i","so","to","this","for","nya","x","geng","selangor","pahang","a","you","of","my","shah","pon","but","sbb","mcm","time","korang","tp","aja","nang","area","eh","kl","or","kg","gak","kalo","in","pas","sih","gue","udah","jakarta","lg","jd","sih","gw","ku","hulu","langat",'banjir', 'mangsa', 'bantu', 'allah', 'selamat', 'and', 'moga', 'hujan', 'hati', 'tengok', 'ga', 'muda', 'taman', 'please', 'baca', 'raja', 'help', 'stay', 'bencana', 'the', 'org', 'sedih', 'doa']
#Stop Words

def cleantext(docx):
    docxFrame = nt.TextFrame(text=docx)
    docxFrame.remove_hashtags()
    docxFrame.remove_userhandles()
    docxFrame.remove_multiple_spaces()
    docxFrame.remove_urls()
    docxFrame.remove_emails()
    docxFrame.remove_numbers()
    docxFrame.remove_emojis()
    docxFrame.remove_puncts()
    docxFrame.remove_special_characters()
    docxFrame.remove_non_ascii()
    docxFrame.remove_stopwords()
    
    cleanDocx = docxFrame.text
    cleanDocx = clean_text(cleanDocx, contractions=True, stopwords=True)
    cleanDocx = ' '.join(term for term in cleanDocx.split() if term not in malay_stop_words)
    return cleanDocx

#Malay Flood Analyzer
mly_flood_model = joblib.load("models/malay_flood_related_lr.pkl","r")

def predictFloodMly(docx):
    results = mly_flood_model.predict([docx])
    return results[0]
#Malay Flood Analyzer

#Malay Sentiment Analyzer
mly_sentiment_model = joblib.load("models/malay_sentiment_rf.pkl","r")

def predictSentimentMly(docx):
    results = mly_sentiment_model.predict([docx])
    return results[0]
#Malay Sentiment Analyzer

emotions_emoji_dict = {"anger":"????","anticipation":"????","disgust":"????","fear":"????","joy":"????","sadness":"????","surprise":"????","trust":"????"}

#Malay Emotion Analyzer
dfMly = pd.read_pickle("datasets/DSPMalayTweetsCleanedV2.pkl")
from sklearn.model_selection import train_test_split
dfMly_subset = dfMly[dfMly['neutral'] != 1]
dfMly_train, dfMly_test = train_test_split(dfMly_subset, shuffle=True, test_size=0.2, random_state=42)
Mly_X_emotion_train = dfMly_train['Tweets']
Mly_y_emotion_train = dfMly_train[['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']]
Mly_X_emotion_test = dfMly_test['Tweets']
Mly_y_emotion_test = dfMly_test[['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']]

mly_emotion_model = joblib.load("models/malay_emotion_rf.pkl","r")

def get_prediction_probaMly(docx):
    emotion = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
    results = pd.DataFrame(columns=['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust'])
    for label in emotion:
        mly_emotion_model.fit(Mly_X_emotion_train, dfMly_train[label])

        test_y_prob = mly_emotion_model.predict_proba([docx])[:,1]
        results[label] = test_y_prob
    return results
#Malay Emotion Analyzer

def app():
    col_1, col_2, col_3 = st.columns([1,8,1])

    with col_1:
        st.write()
    
    with col_2:
        st.image("images/name.png")
        st.markdown('<h1 style="font-weight:10;font-size: 50px;font-family:Source Sans Pro, sans-serif;text-align:center;">Pengesanan Banjir berasaskan Sentimen & Emosi melalui Twitter</h1>',unsafe_allow_html=True)
        
        #Malay
        space(5)
        st.subheader("Penganalisis Teks Banjir & Sentimen & Emosi")
        space(1)
        st.markdown("**Arahan:** Masukkan Teks")

        with st.form(key='form_emosi'):
            raw_textMly = st.text_area('Taip Sini: -',"")
            cleanDocxMly = cleantext(raw_textMly)
            submit_malay_text = st.form_submit_button(label='Analisis')
        #Malay

    if submit_malay_text:
        col__1, col__2, col__3, col__4 = st.columns([1,2,4,1])

        testingMly = predictFloodMly(cleanDocxMly)
        testingSentimentMly = predictSentimentMly(cleanDocxMly)
        probabilityMly = get_prediction_probaMly(cleanDocxMly)
        predictionMly = pd.DataFrame(probabilityMly.idxmax(axis=1))

        with col__2:
            st.success("Ramalan")
            if testingMly == 0:
                st.write("Tidak Berkaitan Banjir")
            else:
                st.write("Berkaitan Banjir")         
            
            st.write("Sentimen: {}".format(testingSentimentMly))
         
            valueMly = predictionMly.loc[0][0]
            emoji_icon = emotions_emoji_dict[valueMly]
            st.write("Emosi: {} {}".format(valueMly,emoji_icon))
            st.write("Skor Emosi: {:.0%}".format(np.max(probabilityMly.to_numpy())))
            
            add_prediction_details(raw_textMly,valueMly,np.max(probabilityMly.to_numpy()),datetime.now())
            
        with col__3:
            st.success("Skor Emosi")
            proba_df = probabilityMly
            porba_df_clean = proba_df.T.reset_index()
            porba_df_clean.columns = ["emosi","kebarangkalian"]

            import plotly.express as px 
            bar_CC = px.bar(porba_df_clean, x='emosi', y='kebarangkalian', color='emosi',color_discrete_sequence=px.colors.qualitative.T10)

            bar_CC.update_xaxes()
            bar_CC.update_layout()
            st.plotly_chart(bar_CC,use_container_width=True)
            
    else:
        with col_2: 
            st.write("*Klik Butang 'Analisis'*")
