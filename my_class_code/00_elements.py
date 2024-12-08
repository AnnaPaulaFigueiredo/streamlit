import streamlit as st
import pandas as pd
import time 
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt
import streamlit.components.v1 as stc
#from bokeh.plotting import figure
#from bokeh.models import ColumnDataSource

# Text Elements
st.text("This is a text")
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a super fnx")
st.markdown("# This is a **markdown**")
st.latex("\int latex")
st.json("{'data':'json file'}")
st.code("print('Python code')", language='python', line_numbers=True)
st.code('System.out.println("Java code");', language='java', line_numbers=True)


# Error Elements from bootstrap
st.success("This is success")
st.error("This is an error")
st.warning("This is a warning")
st.exception("TypeError")

# Input Widget
first_name = st.text_input("First Name")
password = st.text_input("Password", type="password")
message = st.text_area("Message")
date = st.date_input("Date")
appointment_time = st.time_input("Appointment Time")
age = st.number_input("Age", min_value=0, max_value=120)
gender = st.radio("Gender",["Male", "Female"])
enable = st.toggle("Enable Picker")
level_1 = st.checkbox("Level")
level_2 = st.checkbox("Level 2")

# Sliders
countries = st.selectbox("Countries", ['BR', 'PT', 'USA', 'MT', 'IT'])
programing_language = st.multiselect("Programming", ['Python', 'Rubi', 'Golang'])
rating = st.slider("Rating", 0,10)
ranking = st.select_slider("Ranking", ["Junior Dev", "Mid Dev", "Senior Dev"])

st.divider()
if enable:
    st.write(f"Details:{first_name}, {password}")

color = st.color_picker("Pick a color")
st.write(color)

# Data Elements
data = {
    "Fruta": ["Maçã", "Banana", "Laranja", "Uva", "Melancia"],
    "Preco": [3.50, 2.00, 4.00, 7.50, 10.00]
}

df = pd.DataFrame(data)

st.dataframe(df)
st.table(df)
edited_date = st.data_editor(df)
st.json(df.to_json())


# Conection to db
# st.connection()

# Media Elements
img = st.image("data/image_03.jpg")
audio_file = open("data/song.mp3", "rb")
st.audio(audio_file)
st.video("data/secret_of_success.mp4")

#if st.button("Take a picture"):
#    pic = st.camera_input("Take a photo")
#    with open(f"{pic.name}","wb") as f:
#        f.write(pic.getbuffer())

# Download and uploads
#file_upload = st.file_uploader("Uploader", type=['CSV'])
#if file_upload:
#    st.write(pd.read_csv(file_upload))

#st.download_button("Download", file_upload)

# Status Elements
if st.button("Compute"):
    with st.spinner("Thinking..."):
        time.sleep(1)
        st.write("Hello")
    st.toast("This is a toast.")

# Inicializando a barra de progresso
progress_bar = st.progress(0)
status_text = st.empty()
for i in range(101):
    status_text.text(f"Progresso: {i}%")
    progress_bar.progress(i / 100)
    time.sleep(0.05) 
st.success("Processamento concluído!")

# Chat Elements (LLM UI)
# Type writer efect
def stream_data (data, delay:float=0.02):
    for word in data.split():
        yield word + " "
        time.sleep(delay)

prompt = st.chat_input("Ask Something")

#if prompt:

#    with st.chat_message("user"):
#        st.write(f"You typed {prompt}")

#    with st.spinner("Thinking ... "):
#        time.sleep(0.2)
#        response = f"Há, na mente de Deus, um plano que abraça cada criatura de todos os seus imensos domínios; e esse plano é um propósito eterno de oportunidades sem fronteiras, de progresso ilimitado e vida eterna... A meta da eternidade está adiante!... e uma vitória certa irá coroar os esforços de qualquer ser humano, nessa corrida de fé e confiança”."
#        st.write(stream_data(response))
#        st.chat_message("assistant")

response = """Há, na mente de Deus, um plano que abraça cada criatura de todos os seus  
 imensos domínios; e esse plano é um propósito eterno de oportunidades sem fronteiras, de  
 progresso ilimitado e vida eterna... A meta da eternidade está adiante!...
 e uma vitória certa irá coroar os esforços de qualquer ser humano, 
 nessa corrida de fé e confiança”."""    

if st.button("Stream"):
    st.write_stream(stream_data(response))



st.divider()
# Layouts
home_tab, about_tab = st.tabs(["Home", "About"])

with home_tab:
    st.subheader("This is a home tab")

with about_tab:
    st.subheader("This is about tab")

col1, col2, col3 = st.columns(3)

with col1:
    st.title("Columns")

col1.dataframe(df)
col2.image("data/image_03.jpg", use_container_width=True)
col3.write("Col 3")

# Containers
container = st.container(border=True)
container.write("Some container")

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    title = col.container(height=120)
    title.title(":balloon:")

#Expander and PopOver
with st.expander("Expander"):
    st.dataframe(df)

with st.popover("PopOver"):
    st.image("data/image_03.jpg")


# Plots
st.area_chart(df, x='Fruta', y='Preco')
st.line_chart(df, x='Fruta', y='Preco')
st.bar_chart(df, x='Fruta', y='Preco')
st.scatter_chart(df, x='Fruta', y='Preco')


data = {
    "Produto": ["A", "B", "C", "D", "E"],
    "Vendas": [50, 80, 30, 70, 90],
    "Cidades": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"],
    "Latitude": [-23.55052, -22.90685, -19.91668, -25.4284, -30.03306],
    "Longitude": [-46.63331, -43.1729, -43.93449, -49.2733, -51.2300]
}

df = pd.DataFrame(data)

fig = px.bar(df, x="Produto", y="Vendas", color="Produto", title="Vendas por Produto")
st.plotly_chart(fig)


plt.figure(figsize=(8, 4))
plt.bar(df["Produto"], df["Vendas"], color="skyblue")
plt.title("Vendas por Produto", fontsize=16)
plt.xlabel("Produto", fontsize=12)
plt.ylabel("Vendas", fontsize=12)
st.pyplot(plt)

chart = alt.Chart(df).mark_bar(color="orange").encode(
    x="Produto",
    y="Vendas",
    tooltip=["Produto", "Vendas"]
).properties(title="Vendas por Produto")
st.altair_chart(chart)

map_data = df[["Latitude", "Longitude"]]
#st.map(map_data)

#source = ColumnDataSource(df)
#p = figure(title="Vendas por Produto", x_range=df["Produto"], width=600, height=400)
#p.vbar(x="Produto", top="Vendas", width=0.5, color="green", source=source)
#st.bokeh_chart(p)

# Forms
with st.form("MyForm"):
    first_name = st.text_input("First Name")
    password = st.text_input("Password", type='password')  # Corrigi 'Passowrd' para 'Password'
    message = st.text_area("Your message")
    
    # O botão deve estar dentro do 'with'
    submit_button = st.form_submit_button("Send")


stc.html("<p> hello </p>")
import streamlit.components.v1 as components
components.iframe("https://jcharistech.com", width=800, height=600)

if st.button("Visit"):
    st.write("Redirecting...")
    st.markdown("[Visit site](https://jcharistech.com)")
