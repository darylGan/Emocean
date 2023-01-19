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

add_stop_words = ['you know','i mean','yo','dude','couldnt','cant','dont','doesnt','youve','im','ive','wasnt','mightnt','hadnt','hvnt','youre','wouldnt','shouldnt','arent','isnt','werent','youll','its','thats','know','people','amp','time','need','like','year','term','risk','work','gonna','gon na','u','na','sri','dm','tl','bc','cause','ya','w','taman','muda','shah','alam','hulu','langat']
english_stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)
custom_stop_word_list = ['flood', 'help', 'come', 'day', 'feel', 'let', 'love', 'stay', 'water', 'victim', 'make', 'think', 'god', 'want', 'guy', 'bad', 'pls', 'malaysia', 'today', 'tweet', 'open', 'life', 'really', 'say', 'safe', 'pray', 'rain']
english_stop_words = english_stop_words.union(custom_stop_word_list)

malay_stop_words = ["abdul","abdullah","acara","ada","adalah","ahmad","air","akan","akhbar","akhir","aktiviti","alam","amat", "amerika","anak","anggota","antara","antarabangsa","apa","apabila","april","as","asas","asean","asia","asing","atas","atau","australia","awal","awam","bagaimanapun","bagi","bahagian","bahan","baharu","bahawa","baik","bandar","bank","banyak","barangan","baru","baru-baru","bawah","beberapa","bekas","beliau","belum","berada","berakhir","berbanding","berdasarkan","berharap","berikutan","berjaya","berjumlah","berkaitan","berkata","berkenaan","berlaku","bermula","bernama","bernilai","bersama","berubah","besar","bhd","bidang","bilion","bn","boleh","bukan","bulan","bursa","cadangan","china","dagangan","dalam","dan","dana","dapat","dari","daripada","dasar","datang","datuk","demikian","dengan","depan","derivatives","dewan","di","diadakan","dibuka","dicatatkan","dijangka","diniagakan","dis","disember","ditutup","dolar","dr","dua","dunia","ekonomi","eksekutif","eksport","empat","enam","faedah","feb","global","hadapan","hanya","harga","hari","hasil","hingga","hubungan","ia","iaitu","ialah","indeks","india","indonesia","industri","ini","islam","isnin","isu","itu","jabatan","jalan","jan","jawatan","jawatankuasa","jepun","jika","jualan","juga","julai","jumaat","jumlah","jun","juta","kadar","kalangan","kali","kami","kata","katanya","kaunter","kawasan","ke","keadaan","kecil","kedua","kedua-dua","kedudukan","kekal","kementerian","kemudahan","kenaikan","kenyataan","kepada","kepentingan","keputusan","kerajaan","kerana","kereta","kerja","kerjasama","kes","keselamatan","keseluruhan","kesihatan","ketika","ketua","keuntungan","kewangan","khamis","kini","kira-kira","kita","klci","klibor","komposit","kontrak","kos","kuala","kuasa","kukuh","kumpulan","lagi","lain","langkah","laporan","lebih","lepas","lima","lot","luar","lumpur","mac","mahkamah","mahu","majlis","makanan","maklumat","malam","malaysia","mana","manakala","masa","masalah","masih","masing-masing","masyarakat","mata","media","mei","melalui","melihat","memandangkan","memastikan","membantu","membawa","memberi","memberikan","membolehkan","membuat","mempunyai","menambah","menarik","menawarkan","mencapai","mencatatkan","mendapat","mendapatkan","menerima","menerusi","mengadakan","mengambil","mengenai","menggalakkan","menggunakan","mengikut","mengumumkan","mengurangkan","meningkat","meningkatkan","menjadi","menjelang","menokok","menteri","menunjukkan","menurut","menyaksikan","menyediakan","mereka","merosot","merupakan","mesyuarat","minat","minggu","minyak","modal","mohd","mudah","mungkin","naik","najib","nasional","negara","negara-negara","negeri","niaga","nilai","nov","ogos","okt","oleh","operasi","orang","pada","pagi","paling","pameran","papan","para","paras","parlimen","parti","pasaran","pasukan","pegawai","pejabat","pekerja","pelabur","pelaburan","pelancongan","pelanggan","pelbagai","peluang","pembangunan","pemberita","pembinaan","pemimpin","pendapatan","pendidikan","penduduk","penerbangan","pengarah","pengeluaran","pengerusi","pengguna","pengurusan","peniaga","peningkatan","penting","peratus","perdagangan","perdana","peringkat","perjanjian","perkara","perkhidmatan","perladangan","perlu","permintaan","perniagaan","persekutuan","persidangan","pertama","pertubuhan","pertumbuhan","perusahaan","peserta","petang","pihak","pilihan","pinjaman","polis","politik","presiden","prestasi","produk","program","projek","proses","proton","pukul","pula","pusat","rabu","rakan","rakyat","ramai","rantau","raya","rendah","ringgit","rumah","sabah","sahaja","saham","sama","sarawak","satu","sawit","saya","sdn","sebagai","sebahagian","sebanyak","sebarang","sebelum","sebelumnya","sebuah","secara","sedang","segi","sehingga","sejak","sekarang","sektor","sekuriti","selain","selama","selasa","selatan","selepas","seluruh","semakin","semalam","semasa","sementara","semua","semula","sen","sendiri","seorang","sepanjang","seperti","sept","september","serantau","seri","serta","sesi","setiap","setiausaha","sidang","singapura","sini","sistem","sokongan","sri","sudah","sukan","suku","sumber","supaya","susut","syarikat","syed","tahap","tahun","tan","tanah","tanpa","tawaran","teknologi","telah","tempat","tempatan","tempoh","tenaga","tengah","tentang","terbaik","terbang","terbesar","terbuka","terdapat","terhadap","termasuk","tersebut","terus","tetapi","thailand","tiada","tidak","tiga","timbalan","timur","tindakan","tinggi","tun","tunai","turun","turut","umno","unit","untuk","untung","urus","usaha","utama","walaupun","wang","wanita","wilayah","yang","i","so","to","this","for","nya","x","geng","selangor","pahang","a","you","of","my","shah","pon","but","sbb","mcm","time","korang","tp","aja","nang","area","eh","kl","or","kg","gak","kalo","in","pas","sih","gue","udah","jakarta","lg","jd","sih","gw","ku","hulu","langat",'banjir', 'mangsa', 'bantu', 'allah', 'selamat', 'and', 'moga', 'hujan', 'hati', 'tengok', 'ga', 'muda', 'taman', 'please', 'baca', 'raja', 'help', 'stay', 'bencana', 'the', 'org', 'sedih', 'doa']

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
    cleanDocx = ' '.join(term for term in cleanDocx.split() if term not in english_stop_words)
    return cleanDocx

#Flood Analyzer
eng_flood_model = joblib.load("models/english_flood_related_mnb.pkl","r")

def predictFlood(docx):
    results = eng_flood_model.predict([docx])
    return results
#Flood Analyzer


#Emotion Analyzer
emotions_emoji_dict = {"anger":"😡","anticipation":"🤔","disgust":"🤢","fear":"😨","joy":"😂","sadness":"😔","surprise":"😲","trust":"🤗"}

dfEng = pd.read_pickle("datasets/DSPEnglishTweetsCleanedV2.pkl")

from sklearn.model_selection import train_test_split
dfEng_subset = dfEng[dfEng['neutral'] != 1]
train, test = train_test_split(dfEng_subset, shuffle=True, test_size=0.2, random_state=42)
X_emotion_train = train['Tweets']
y_emotion_train = train[['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']]
X_emotion_test = test['Tweets']
y_emotion_test = test[['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']]

eng_emotion_model = joblib.load("models/english_emotion_rf.pkl","r")

def get_prediction_proba(docx):
    emotion = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
    results = pd.DataFrame(columns=['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust'])
    for label in emotion:
        eng_emotion_model.fit(X_emotion_train, train[label])

        test_y_prob = eng_emotion_model.predict_proba([docx])[:,1]
        results[label] = test_y_prob
    return results
#Emotion Analyzer

def app():
    st.markdown(f'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
        <style>
        blockquote.twitter-tweet {
            display: inline-block;
            font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
            font-size: 12px;
            font-weight: bold;
            line-height: 16px;
            border-color: #eee #ddd #bbb;
            border-radius: 5px;
            border-style: solid;
            border-width: 1px;
            box-shadow: 0 1px 3px rgb(0 0 0 / 20%);
            margin: 10px 15%;
            padding: 8px 16px 16px 16px;
            max-width: 468px;
            transition: transform 500ms ease;
        }
        .twitter-tweet:hover,
        .twitter-tweet:focus-within {
            transform: scale(1.025);
        }
        </style>""",unsafe_allow_html=True)

    col_1, col_2, col_3 = st.columns([1,8,1])

    with col_1:
        st.write()
    
    with col_2:
        st.image("images/name.png")
        st.markdown('<h1 style="font-weight:10;font-size: 50px;font-family:Source Sans Pro, sans-serif;text-align:center;">Sentiment & Emotion-based Flood Detection through Twitter</h1>',unsafe_allow_html=True)
        space(2)
        st.subheader("Text Sentiment & Emotion Analyzer")
        space(1)
        st.markdown("**Instructions:** Enter Text")

        with st.form(key='emotion_form'):
            raw_text = st.text_area('Type Here: -',"")
            cleanDocx = cleantext(raw_text)
            submit_text = st.form_submit_button(label='Analyze')

    if submit_text:
        col1, col2, col3, col4 = st.columns([1,2,4,1])

        # Prediction Funtions
        testing = predictFlood(cleanDocx)
        probability = get_prediction_proba(cleanDocx)
        prediction = pd.DataFrame(probability.idxmax(axis=1))

        with col2:
            st.write(testing)
            st.success("Prediction")
            value = prediction.loc[0][0]
            emoji_icon = emotions_emoji_dict[value]
            st.write("{}:{}".format(value,emoji_icon))
            st.write("Emotion Score:{:.0%}".format(np.max(probability.to_numpy())))
            add_prediction_details(raw_text,value,np.max(probability.to_numpy()),datetime.now())
            
        with col3:
            st.success("Emotion Score")
            proba_df = probability
            porba_df_clean = proba_df.T.reset_index()
            porba_df_clean.columns = ["emotions","probability"]

            import plotly.express as px 
            bar_CC = px.bar(porba_df_clean, x='emotions', y='probability', color='emotions',color_discrete_sequence=px.colors.qualitative.T10)

            bar_CC.update_xaxes()
            bar_CC.update_layout()
            st.plotly_chart(bar_CC,use_container_width=True)
            
    else:
        with col_2: 
            st.write("*Click 'Analyze' Button*")
