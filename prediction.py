import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
import pickle
import time
import matplotlib.pyplot as plt


def remove_feature(df):
    irrelevant_feature = ['EmployeeId', 'EmployeeCount', 'StandardHours', 'PerformanceRating', 'Over18']
    df = df.drop(columns=irrelevant_feature, axis=1, errors='ignore')
    return df

def feature_scaling(df):
    df_temp = df.copy()
    df_temp = df_temp.select_dtypes(include=['int64', 'float64'])
    df_temp = df_temp.drop(columns=[
        'Attrition',
        'Education',
        'EnvironmentSatisfaction',
        'JobInvolvement',
        'RelationshipSatisfaction',
        'JobSatisfaction',
        'JobLevel',
        'StockOptionLevel',
        'WorkLifeBalance'
    ])

    numerical_columns = df_temp.columns

    scaler = StandardScaler()
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    return df

def transform_feature(df):
    categorical_columns = list(df.select_dtypes(include='object').columns)
    encoder = OrdinalEncoder()

    for column in categorical_columns:
        df[column] = encoder.fit_transform(df[[column]])

    extra_categorical = [
        'Education',
        'EnvironmentSatisfaction',
        'JobInvolvement',
        'RelationshipSatisfaction',
        'JobSatisfaction',
        'JobLevel',
        'StockOptionLevel',
        'WorkLifeBalance',
    ]

    all_categorical_columns = categorical_columns + extra_categorical

    df = pd.get_dummies(df, columns=all_categorical_columns, drop_first=True, dtype=int)

    return df

def risk_label(p):
    if p >= 0.8:
        return "Tinggi"
    elif p >= 0.5:
        return "Sedang"
    else:
        return "Rendah"

if 'show_confirm' not in st.session_state:
    st.session_state.show_confirm = False
if 'preprocess_ok' not in st.session_state:
    st.session_state.preprocess_ok = False
if 'df_processed' not in st.session_state:
    st.session_state.df_processed = None

st.subheader("Upload Data")

## FIEL UPLOAD
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

st.divider()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data")
    st.dataframe(df)

    ## PRE-PROCESSING DATA
    if st.button("🔧 Apakah ingin melakukan pre-processing data?"):
        st.session_state.show_confirm = True
        st.session_state.preprocess_ok = False

    if st.session_state.show_confirm and not st.session_state.preprocess_ok:    
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Ya, lakukan"):
                st.session_state.show_confirm = False
                st.session_state.preprocess_ok = True
        with col2:
            if st.button("❌ Tidak"):
                st.session_state.show_confirm = True
                st.session_state.df_processed = df

        if st.session_state.preprocess_ok:
            with st.status("🔄 Pre-processing data...", expanded=True) as status:
                st.write("📊 Membersihkan fitur yang tidak relevan . . .")
                df_cleaned = remove_feature(df)
                st.write("✅ Pembersihan fitur tidak relevan selesai.")

                st.write("📊 Melakukan feature scaling . . .")
                df_cleaned = feature_scaling(df_cleaned)
                st.write("✅ Feature scaling selesai.")

                st.write("🔤 Melakukan transformasi data...")
                df_cleaned = transform_feature(df_cleaned)
                st.write("✅ Data transformasi selesai.")
                
                st.session_state.df_processed = df_cleaned
                status.update(label="✅ Semua Pre-Processing Data Telah Selesai.", state="complete", expanded=True)

            st.divider()
            st.subheader("📊 Data Setelah Pre-Processing")
            st.dataframe(df_cleaned)

    st.divider()

    ## MODEL PREDICTION
    selected_features = None
    if st.session_state.df_processed is not None:
        try:
            with open('model.sav', 'rb') as model_file:
                model = pickle.load(model_file)   
                st.write("✅ Model ditemukan") 
                selected_features = model.get_booster().feature_names
        except FileNotFoundError:
            st.error("❌ File 'model.sav' tidak ditemukan")
            st.stop()

        try:
            if st.button("🔮 Prediksi Sekarang"):
                with st.status("⏳ Melakukan Prediksi...", expanded=True) as status:
                    progress = st.progress(0)
                    for i in range(1, 101, 10):
                        time.sleep(0.05)
                        progress.progress(i)

                    df_pred = st.session_state.df_processed.copy()
                    df_pred = df_pred[selected_features]
                    predictions = model.predict(df_pred)
                    prediction_proba = model.predict_proba(df_pred)
                    prob_attrition = prediction_proba[:, 1]

                    df['Prediksi'] = ['Keluar' if p == 1 else 'Bertahan' for p in predictions]
                    df['Tingkat Risiko'] = [risk_label(p) for p in prob_attrition] 

                status.update(label="✅ Prediksi Selesai", state="complete", expanded=False)

                ## PREDICTION RESULT
                st.divider()
                st.subheader("📈 Hasil Prediksi Pegawai")
                st.dataframe(df[['Prediksi', 'Tingkat Risiko'] + [col for col in df.columns if col not in ['Prediksi', 'Tingkat Risiko']]])


                # PREDICTION SUMMARY
                st.divider()
                st.subheader("📊 Ringkasan Prediksi")
                chart_data = df['Prediksi'].value_counts().reset_index()
                chart_data.columns = ['Status', 'Jumlah']
                st.bar_chart(chart_data.set_index('Status'))

                keluar = chart_data.loc[chart_data['Status'] == 'Keluar', 'Jumlah'].values[0] if 'Keluar' in chart_data['Status'].values else 0
                bertahan = chart_data.loc[chart_data['Status'] == 'Bertahan', 'Jumlah'].values[0] if 'Bertahan' in chart_data['Status'].values else 0
                total = keluar + bertahan

                st.write(f"📌 Dari total **{total} pegawai**, sebanyak **{keluar} diprediksi akan keluar**, dan **{bertahan} diprediksi akan tetap bertahan**.")

                fig, ax = plt.subplots()
                ax.pie([keluar, bertahan], labels=['Keluar', 'Bertahan'], autopct='%1.1f%%', startangle=90, colors=['#FF6B6B', '#4ECDC4'])
                ax.axis('equal')
                st.pyplot(fig)

                df.to_csv('employee_result.csv', index=False)
        except Exception as e:
            st.error("❌ Terdapat data yang invalid, harap melakukan pre-processing terlebih dahulu")
            st.stop()
else:
    st.error("❌ Belum ada file data")
    st.stop()
