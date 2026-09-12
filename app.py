import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Vision22 Growth Strategy Intelligence', layout='wide')

st.markdown('''<style>
body{background:#ffffff}
.stMetric{border:1px solid #e8e8e8;padding:15px;border-radius:12px}
h1,h2,h3{color:#111111}
</style>''', unsafe_allow_html=True)

@st.cache_data
def packages_data():
    return pd.DataFrame([
        ['B2B Growth Foundation',6000,9000,85],
        ['B2B Lead Generation Engine',8000,12000,90],
        ['Digital Authority & Brand Growth',12000,20000,75],
        ['Performance Growth System',10000,15000,85],
        ['Complete B2B Growth Department',20000,35000,65]
    ],columns=['Package','Setup Price','Monthly Retainer','Success %'])

st.title('Vision22 USA & Canada Growth Strategy Case Study')
st.caption('Premium B2B Marketing Intelligence Dashboard')

c1,c2,c3,c4=st.columns(4)
c1.metric('Market','USA + Canada')
c2.metric('Primary Entry','B2B Lead Generation')
c3.metric('Best Success Rate','90%')
c4.metric('Positioning','Premium Affordable')

st.header('Executive Overview')
st.write('Vision22 should enter North America as a specialized B2B Growth Partner focused on measurable pipeline generation, authority building and strategic digital growth systems.')

st.header('Market Analysis')
segments=pd.DataFrame([['Manufacturing',95,90,85],['B2B SaaS',92,95,88],['Healthcare',85,90,80],['Construction',80,82,78],['Professional Services',78,85,75]],columns=['Sector','Attractiveness','Buying Power','Entry Score'])
st.dataframe(segments,use_container_width=True)
st.plotly_chart(px.scatter(segments,x='Buying Power',y='Attractiveness',size='Entry Score',text='Sector'),use_container_width=True)

st.header('Package Intelligence')
p=packages_data()
st.dataframe(p,use_container_width=True)
st.plotly_chart(px.bar(p,x='Package',y='Success %',text='Success %'),use_container_width=True)

st.header('Pricing Intelligence')
pricing=pd.DataFrame([['Current Pricing',7000,90],['30% Discount',4900,94],['50% Discount',3500,97]],columns=['Scenario','Average Price','Opportunity Score'])
st.dataframe(pricing,use_container_width=True)
st.plotly_chart(px.bar(pricing,x='Scenario',y='Opportunity Score'),use_container_width=True)

st.header('SWOT Analysis')
a,b,c,d=st.columns(4)
a.success('Strengths\n\nCreative capability\nB2B strategy\nCompetitive delivery')
b.warning('Weaknesses\n\nLow North America awareness\nNeed more proof')
c.info('Opportunities\n\nManufacturing\nSaaS\nHealthcare')
d.error('Threats\n\nCompetition\nPrice pressure')

st.header('Risk Analysis')
st.table(pd.DataFrame([['Positioning','High','Sell outcomes not services'],['Trust Gap','High','Build case studies'],['Low Outreach','Medium','ABM campaigns']],columns=['Risk','Impact','Solution']))

st.header('Go To Market Roadmap')
st.markdown('''Phase 1: Foundation and authority building\n\nPhase 2: ABM outreach and market entry\n\nPhase 3: Sales conversion\n\nPhase 4: Scaling partnerships''')

st.header('Email Campaign Calculator')
accounts=st.number_input('Target Accounts',100,50000,1000)
reply=st.slider('Reply Rate %',1,20,3)
meeting=st.slider('Meeting Rate %',5,80,30)
close=st.slider('Close Rate %',5,80,20)
clients=int(accounts*reply/100*meeting/100*close/100)
st.metric('Expected Clients',clients)
st.metric('Expected MRR',f'${clients*7000:,}')

st.header('Revenue Forecast')
revenue=pd.DataFrame([['Conservative',3,21000],['Realistic',5,35000],['Aggressive',10,70000]],columns=['Scenario','Clients','Revenue'])
st.dataframe(revenue)
st.plotly_chart(px.bar(revenue,x='Scenario',y='Revenue'),use_container_width=True)

st.success('Vision22 Growth Intelligence Dashboard Ready')
