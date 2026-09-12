import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vision22 Market Intelligence", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.main {background:#ffffff;}
.card {background:white;border:1px solid #e6e6e6;border-radius:18px;padding:20px;box-shadow:0 4px 15px #00000010;}
.metric-title{font-size:14px;color:#666;}
.metric-value{font-size:28px;font-weight:700;color:#111;}
h1,h2,h3{color:#111;}
</style>
""",unsafe_allow_html=True)

@st.cache_data
def data():
    packages=pd.DataFrame([
    ["B2B Growth Foundation",6000,9000,85],
    ["B2B Lead Generation Engine",8000,12000,90],
    ["Digital Authority & Brand Growth",12000,20000,75],
    ["Performance Growth System",10000,15000,85],
    ["Complete B2B Growth Department",20000,35000,65]],columns=["Package","Setup","Monthly","Success"])
    sectors=pd.DataFrame([
    ["Manufacturing",95,90,85], ["B2B SaaS",92,95,88],
    ["Healthcare",85,90,80], ["Construction",80,82,78],
    ["Professional Services",78,85,75]],columns=["Sector","Attractiveness","Buying Power","Entry"])
    return packages,sectors

packages,sectors=data()

st.sidebar.title("Vision22 Intelligence")
page=st.sidebar.radio("Navigation",[
"Executive Overview","Market Analysis","Packages","Pricing Intelligence","SWOT","Risk Analysis","GTM Roadmap","Email Simulator","Revenue Forecast"])

st.title("Vision22 USA & Canada Growth Intelligence")
st.caption("Premium B2B Strategy Dashboard | Consulting Style")

if page=="Executive Overview":
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Market","USA + Canada")
    c2.metric("Best Entry","B2B Lead Generation")
    c3.metric("Opportunity Score","90%")
    c4.metric("Positioning","Premium Affordable")
    st.info("Vision22 enters North America as a specialized B2B Growth Partner focused on pipeline generation and measurable business growth.")

elif page=="Market Analysis":
    st.header("Target Market Opportunity")
    st.dataframe(sectors,use_container_width=True)
    st.plotly_chart(px.scatter(sectors,x="Buying Power",y="Attractiveness",size="Entry",text="Sector"),use_container_width=True)

elif page=="Packages":
    st.header("Package Intelligence")
    st.dataframe(packages,use_container_width=True)
    st.plotly_chart(px.bar(packages,x="Package",y="Success",text="Success"),use_container_width=True)

elif page=="Pricing Intelligence":
    st.header("Pricing Scenario Analysis")
    pricing=pd.DataFrame([["Current",7000,90],["30% Lower",4900,94],["50% Lower",3500,97]],columns=["Scenario","Price","Opportunity"])
    st.dataframe(pricing,use_container_width=True)
    st.plotly_chart(px.bar(pricing,x="Scenario",y="Opportunity"),use_container_width=True)

elif page=="SWOT":
    a,b,c,d=st.columns(4)
    a.success("Strengths\n\nB2B Strategy\nCreative Production\nCompetitive Delivery")
    b.warning("Weaknesses\n\nNorth America Awareness\nNeed More Proof")
    c.info("Opportunities\n\nManufacturing\nSaaS\nHealthcare")
    d.error("Threats\n\nCompetition\nPrice Pressure")

elif page=="Risk Analysis":
    st.table(pd.DataFrame([["Trust Gap","High","Build Case Studies"],["Wrong Positioning","High","Sell Outcomes"],["Low Outreach","Medium","ABM System"]],columns=["Risk","Impact","Solution"]))

elif page=="GTM Roadmap":
    st.header("90 Day Growth Roadmap")
    st.markdown("""### Phase 1 — Foundation
Authority + Positioning

### Phase 2 — Market Entry
ABM + Email Outreach

### Phase 3 — Acquisition
Meetings + Sales Conversion

### Phase 4 — Scaling
Partnerships + Expansion""")

elif page=="Email Simulator":
    accounts=st.slider("Target Accounts",100,10000,1000)
    reply=st.slider("Reply Rate %",1,20,3)
    meeting=st.slider("Meeting Rate %",5,80,30)
    close=st.slider("Close Rate %",5,80,20)
    clients=int(accounts*reply/100*meeting/100*close/100)
    st.metric("Expected Clients",clients)
    st.metric("Expected MRR",f"${clients*7000:,}")

elif page=="Revenue Forecast":
    rev=pd.DataFrame([["Conservative",3,21000],["Realistic",5,35000],["Aggressive",10,70000]],columns=["Scenario","Clients","Revenue"])
    st.dataframe(rev)
    st.plotly_chart(px.bar(rev,x="Scenario",y="Revenue"),use_container_width=True)

st.success("Vision22 Market Intelligence Dashboard")