import streamlit as st
import time
st.title("Stremlit Pomodoro Timer")
worktime= st.slider("Work Time (minutes)",5,98,25)
breaktime= st.slider("Break Time (minutes)",1,30,5)

def PomodoroTimer(worktime,breaktime):
    workseconds= worktime*60
    breakseconds= breaktime*60
    
    workplaceholder= st.empty()
    breakplaceholder= st.empty()
    
    workplaceholder.write("Work!")
    for i in range(workseconds):
        time.sleep(1)
        workplaceholder.write(f"{workseconds -i} seconds left")
        
    breakplaceholder.write("Work!")
    for i in range(breakseconds):
        time.sleep(1)
        workplaceholder.write(f"{breakseconds -i} seconds left")
if st.button("Start Timer"):
    PomodoroTimer(worktime,breaktime)