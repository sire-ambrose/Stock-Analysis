import plotly.graph_objects as go
import streamlit as st
import yfinance as yf
st.write("# Stock Analysis")
'\n'

name_dict={'APPLE':'AAPL', 'Facebook':'FB'}

def display(name):
    st.write("### "+name)
    get_info=yf.Ticker(name_dict[name])
    '\n'

    interval = st.selectbox('Period',['1 day', '5 days', '1 month', '3 months', '6 months', '1 year', '2 years'],key=name+'period')

    'You selected: ', interval
    interval_dict={'1 day':'1d', '5 days':'5d', '1 month':'1mo', '3 months':'3mo', '6 months':'6mo', '1 year':'1y', '2 years':'2y'}
    '\n'
    
    data=get_info.history(period=interval_dict[interval])
    st.write(data)

    fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
    

    fig.show()
    st.plotly_chart(fig)

    extra_info = st.selectbox('Information',['Yes', 'No'],key=name+'info')

    'You selected: ', extra_info

    if extra_info == 'Yes':
        for i in get_info.info.keys():
            i,' :',get_info.info[i]
            ''
for i in name_dict:
    display(i)
    ''

st.write('\n\n\n\n\n\n')
st.write('### Contact Developer : ')
st.write('[Facebook](https://www.facebook.com/profile.php?id=100005064735483)')
st.write('[Github ](https://github.com/sire-ambrose)')
st.write('[Linkedin](https://www.linkedin.com/in/ambrose-ikpele-61643419a)')
