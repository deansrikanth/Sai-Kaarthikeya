import streamlit as st

st.set_page_config(page_title='My Website', page_icon=":bar_chart:", layout="wide")

custom_css = """
<style>

    h1,h2,h3,h4 {
      text-align: center;
      color: #32CD32;
    }

    .centered-image img {
      display: block;
      margin-left: auto;
      margin-right: auto;
      margin-top:-40px;
      border-radius: 50%;
      width: 200px;
      height: 200px;
      object-fit: cover;
    }

</style>
"""

#Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)


# Main content of the page
with st.container():
    st.markdown(
    """
    <div class="centered-image">
    <img src = "https://images4.alphacoders.com/135/1352902.jpeg" width="200"/>
    </div>

    """,
    unsafe_allow_html=True
    )

#Introduction
with st.container():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2 style="color: #1E90FF;">Hello!</h2>
            <h3>I am Sai Kaarthikeya.</h3>
            <h5 style="color: white;">I have completed my MBA from Aurora's P.G College, which comes under Osmania University.</h5>      
        </div>
        """,
        unsafe_allow_html=True
    )

#Objective
with st.container():
    st.write("----")
    st.markdown(
      """
      <div style="text-align: left;">
          <h4 style="text-align: left;">Objective :</h4>
          <p style="font-size:20px;color: white;">To Secure a Challenging Position in an Organization that Fosters Professional Growth, where I can Contribute My skills to the Company's Success while Advancing My Own Development.</p>
      </div>

      """,
      unsafe_allow_html=True
      )
    
#Qualification   
with st.container():
    st.write('----')
    st.markdown(
      """
      <div style='text-align: left:'>
        <h4 style='text-align: left;'>Qualification :</h4>
        <ul style="list-style-type: disc; padding: 0;">
              <li>Masters in Business Administration(MBA) - Completed</li>
              <li>Bachelor of Science(Chemistry) - 8.04 CGPA</li>
              <li>Intermediate - 73.3 </li>
              <li>Secondary School Certificate (SSC) - 7.7 CGPA</li>
        </ul>
      </div>
          
      """,
      unsafe_allow_html=True
    )

#Certificates
with st.container():
    st.write('----')
    left_side, right_side = st.columns(2)

    with left_side:
        st.markdown(
        """
        <div style="text-align: left;">
          <h4 style='text-align: left;'>Certificates :</h4>
          <ul style='list-style: disc; padding: 0;'>
                <li>Preparing Data for Analysis with Microsoft Excel</li>
                <li>Data Modeling in Power BI</li>
                <li>Data Analysis and Visualization with Power BI</li>   
                <li>Extract, Transform and Load Data in Power BI</li>
                <li>Creative Designing in Power BI</li>
                <li>Harnessing the Power of Data with Power BI</li>
                <li>Microsoft Power BI Data Analyst</li>
          </ul>
        </div>

       """, 
       unsafe_allow_html=True
       
     )
        
    with right_side:
        st.markdown(
        """
        <div style='text-align: right;'>
          <h4 style='text-align: right;'>Links</h4>
          <ul style='list-style: none; padding: 0;'>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/GHZ3NP3JZ8F4" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/RP4V24X7XMMD" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/2NJ5NQVCTFTW" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/9V9N6LR22X2X" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/Z8L6BYS2BYLH" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/verify/MKCAGXXP3NSQ" target='_blank'>View Certificate</a></li>
                 <li><a href = "https://www.coursera.org/account/accomplishments/professional-cert/ULF9YVXJ2XTA" target='_blank'>View Certificate</a></li>
          </ul>
        </div>

        """,
        unsafe_allow_html=True
      )

#Skills and Hobbies
with st.container():
    st.write('----')
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown(
        """
        <div style="text-align :left;">
          <h4 style="text-align: left;">Skills :</h4>
          <ul style="list-style-type: disc; padding: 0;">
                <li>Power BI</li>
                <li>Microsoft Office (PowerPoint, Excel, Word)</li>
                <li>Basics In Python</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
       )
        

    with right_column:
        st.markdown("""
        <div style="text-align :left;">
          <h4 style="text-align: left;">Hobbies and Interest:</h4>
          <ul style="list-style-type: disc; padding: 0;">
                <li>Playing Video Games</li>
                <li>Listening to Music</li>
                <li>Watching Movies</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True
       )
# Contact info
with st.container():
  st.write("----")
  st.markdown(
     """

  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> 

  <div style="text-align: center; margin: 20px;">
    <h2><b>Contact on :</b></h2>

    <p style="margin: 10px 0;">
      <span class="material-icons" style="vertical-align: middle;">email</span>
      <b>Email</b>: <a href="mailto:karthikeya18032001@gmail.com">karthikeya18032001@gmail.com</a>
    </p>

    <p style="margin: 10px 0;">
      <span class="material-icons" style="vertical-align: middle;">business_center</span>
      <b>LinkedIn</b>: <a href="https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit">Profile</a>
    </p>

    <p style="margin: 10px 0;">
      <span class="material-icons" style="vertical-align: middle;">phone</span>
      <b>Phone</b>: +91-8309383175
    </p>

  </div>

     """,
    unsafe_allow_html = True
 
 )




 


