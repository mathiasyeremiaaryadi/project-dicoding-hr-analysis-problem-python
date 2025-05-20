import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
import pickle

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

st.title("Prediksi Attrition")

uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data yang Diunggah")
    st.dataframe(df)

    apply_preprocessing = st.checkbox("Do you want pre-process the data?", value=True)

    if apply_preprocessing:
        with st.status("🔄 Pre-processing data...", expanded=True) as status:
            st.write("📊 Feature scaling...")
            df = feature_scaling(df)
            st.write("✅ Feature scaling completed.")

            st.write("🔤 Transforming data...")
            df = transform_feature(df)
            st.write("✅ Data transformation compelted.")

            status.update(label="✅ All Pre-Processing Completed.", state="complete", expanded=False)

    try:
        with open('model.sav', 'rb') as model_file:
            model = pickle.load(model_file)

        
    except FileNotFoundError:
        st.error("❌ File 'model.sav' is not found")