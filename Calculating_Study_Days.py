#!/usr/bin/python3

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import random

sub1 =str()
sub2=str()
st.set_page_config(
     page_title='Calculate Research Days',
     layout="wide",
     initial_sidebar_state="expanded")

one, two, three = st.beta_columns(3)

image = three.image('https://images.unsplash.com/photo-1584967918940-a7d51b064268?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80', width =250)

one.title("Calculate Research Days")

st.header("Instructions:")
st.write("From the selection field in the sidebar, select the type of research being performed. Enter information about the pilot study and then the parameters for the study. Then press Calculate below.")
st.subheader("Predicted Time to Complete Study")

work = st.sidebar.selectbox("Research Type", ["Select","Field Work","Lab Work"])

#labwork = st.sidebar.checkbox("Lab Work")
 
if work == "Select":
	st.sidebar.write("")
	

if work == "Field Work":
	st.sidebar.subheader("Pilot Study Information")
	pilothours =st.sidebar.number_input("Total hours:", value = 3)
	pilotobs = st.sidebar.number_input("Total observtions:", value = 14)
	pilotpeople = st.sidebar.number_input("Number of people collecting data:", value = 4)
		
	st.sidebar.subheader("Study Information")
	type = st.sidebar.number_input("Number of location types:", value = 3)
	site = st.sidebar.number_input("Number of sites per location type:", value = 3)
	obs = st.sidebar.number_input("Number of observations per location:", value = 60)
	people = st.sidebar.number_input ("Number of people collecting data (or number of groups):", value = 4)
	hours = st.sidebar.number_input ("Number of hours per day for data collection:", value= 8)
	
	def calc1(pilothours,pilotpeople,obs,type,site,pilotobs):  
		totalobs= (obs * type * site)
		pilotmhrs= pilothours * pilotpeople
		total1 = ((pilotmhrs*totalobs)/pilotobs)
		return total1
	
	subtotal1 = calc1(pilothours,pilotpeople,obs,type,site,pilotobs)
	manhours  = people*hours
	subtotal2 = subtotal1/manhours
	sub1 = str(round(subtotal1,2))
	sub2 = str(round(subtotal2))
	


if work == "Lab Work":
	st.sidebar.subheader("Pilot Study Information")
	pilothours =st.sidebar.number_input("Total hours:", value = 3)
	pilotobs = st.sidebar.number_input("Total observtions:", value = 14)
	pilotpeople = st.sidebar.number_input("Number of people collecting data:", value = 4)
				
	st.sidebar.subheader("Study Information")
	obs = st.sidebar.number_input("Number of observations needed:", value = 60)
	people = st.sidebar.number_input ("Number of people collecting data (or number of groups):", value = 4)
	hours = st.sidebar.number_input ("Number of hours per day for data collection:", value= 8)
	
	def calc3(pilothours,pilotpeople,obs,pilotobs):  
		totalobs= obs
		pilotmhrs= (pilothours * pilotpeople)
		total2 = ((pilotmhrs*obs)/pilotobs)
		return total2
	
	
	subtotal1 = calc3(pilothours,pilotpeople,obs,pilotobs)
	manhours  = (people*hours)
	subtotal2 = manhours/(people*hours)
	sub1 = str(round(subtotal1,2))
	sub2 = str(round(subtotal2))
write1= str("Total Man Hours Needed = " + sub1)
write2 = str("Total Days Needed = " + sub2)	

if st.button ("Calculate"):
	st.write(write1)
	st.write(write2)