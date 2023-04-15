import streamlit as st
def calculate_emi(p,n,r):
	emi = p*(r/100)*((1+(r/100)**n)/(1+(r/100)**n)-1)
	return emi
st.title('EMI calculator')
p = st.slider('Enter Principal Amount', 1,1000000)
n = st.slider('Enter number of years', 1,20)
r = st.slider('Enter rate of interest', 1,25)
if st.button('Calculate'):
	emi = calculate_emi(p,n,r)
	st.write('EMI =',emi)
