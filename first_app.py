import streamlit as st

#### Sidebar Column
st.sidebar.title('Sidebar Widgets')

#### Radio button 
rating = st.sidebar.radio('Are You Happy with the Example',('Yes','No','Not Sure'))
if rating == 'Yes':
    st.sidebar.success('Thank You for Selecting Yes')
elif rating =='No':
    st.sidebar.info('Thank You for Selecting No')
elif rating =='Not Sure':
    st.sidebar.info('Thank You for Selecting Not sure')
    
#### Selectbox
rating = st.sidebar.selectbox("How much would you rate this App? ",
                     ['5 Stars', '4 Stars', '3 Stars','2 Stars','1 Star'])
st.sidebar.success(rating)
st.sidebar.write('Find Square of a Number')

#### Slider
get_number = st.sidebar.slider("Select a Number", 1, 10)
st.sidebar.write('Square of Number',get_number, 'is', get_number*get_number)


##########################################################################

st.title("A primality test app with Streamlit")
## Your name and title

st.header("*Testing Purpose* :boom:")


#### Height selectbox

height = st.number_input('Enter the height')
#number = int(number)

if not height:
    st.warning('Please enter the height above.')
    #st.stop()
    
if height:
    st.write('You entered ->', height, ':smile:')


#### Width Selectbox

width = st.number_input('Enter the width')
#number = int(number)

if not width:
    st.warning('Please enter the width above.')
    
elif width:
    st.write('You entered ->', width, ':smile:')


#### Room Slider
    
room = st.slider('Select the number of room(max)', 0, 10)

if not room:
    st.warning('Please choose no. of room.')
    st.stop()

elif room:
    st.write('You choose ->', room, ':smile:')


st.success('Thank you for entering the information.')

st.text('Calculating the price...')
