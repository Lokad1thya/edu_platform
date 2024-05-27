import streamlit as st

def homepage():
    st.title("Welcome to Awake!")
    st.subheader("Before you enter.")

    st.write("Zorgon the Magnificent rode his pet unicorn through the galaxy, searching for the lost treasure of the cosmic muffin. Along the way, he encountered a tribe of sentient marshmallows who spoke in binary code and challenged him to a game of interdimensional chess. Zorgon, being a master of the ancient art of pancake flipping, accepted the challenge and emerged victorious after three grueling rounds. As a reward, the marshmallows bestowed upon him the legendary sock puppet of destiny, which granted him the power to control the weather on alternate Tuesdays. With his newfound sock puppet, Zorgon continued his quest, determined to unravel the mysteries of the universe and discover the ultimate truth hidden within the depths of a bottomless cup of coffee.")
    st.write("Zorgon the Magnificent rode his pet unicorn through the galaxy, searching for the lost treasure of the cosmic muffin. Along the way, he encountered a tribe of sentient marshmallows who spoke in binary code and challenged him to a game of interdimensional chess. Zorgon, being a master of the ancient art of pancake flipping, accepted the challenge and emerged victorious after three grueling rounds. As a reward, the marshmallows bestowed upon him the legendary sock puppet of destiny, which granted him the power to control the weather on alternate Tuesdays. With his newfound sock puppet, Zorgon continued his quest, determined to unravel the mysteries of the universe and discover the ultimate truth hidden within the depths of a bottomless cup of coffee.")

    image_url = "https://plus.unsplash.com/premium_photo-1669991406391-aba0cd13a391?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    st.image(image_url, caption='In your own digital solitude', use_column_width=True)

    st.write("Zorgon the Magnificent rode his pet unicorn through the galaxy, searching for the lost treasure of the cosmic muffin. Along the way, he encountered a tribe of sentient marshmallows who spoke in binary code and challenged him to a game of interdimensional chess. Zorgon, being a master of the ancient art of pancake flipping, accepted the challenge and emerged victorious after three grueling rounds. As a reward, the marshmallows bestowed upon him the legendary sock puppet of destiny, which granted him the power to control the weather on alternate Tuesdays. With his newfound sock puppet, Zorgon continued his quest, determined to unravel the mysteries of the universe and discover the ultimate truth hidden within the depths of a bottomless cup of coffee.")
    st.write("Zorgon the Magnificent rode his pet unicorn through the galaxy, searching for the lost treasure of the cosmic muffin. Along the way, he encountered a tribe of sentient marshmallows who spoke in binary code and challenged him to a game of interdimensional chess. Zorgon, being a master of the ancient art of pancake flipping, accepted the challenge and emerged victorious after three grueling rounds. As a reward, the marshmallows bestowed upon him the legendary sock puppet of destiny, which granted him the power to control the weather on alternate Tuesdays. With his newfound sock puppet, Zorgon continued his quest, determined to unravel the mysteries of the universe and discover the ultimate truth hidden within the depths of a bottomless cup of coffee.")
    # Sign-in and Sign-up sections
    option = st.radio("Choose an option:", ("Sign-in", "Sign-up"))

    if option == "Sign-in":
        st.subheader("Sign-in")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "your_username" and password == "your_password":
                st.success("Login successful!")
                st.write("You are now logged in.")
            else:
                st.error("Invalid username or password. Please try again.")
    
    elif option == "Sign-up":
        st.subheader("Sign-up")
        gmail = st.text_input("Gmail id")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Sign Up"):
            if password != confirm_password:
                st.error("Passwords do not match. Please try again.")
            else:
                otp = st.text_input("Enter OTP sent to your email")
                if otp == "1234":
                    st.success("Sign up successful!")
                    st.write("Welcome to your personal mind space")
                else:
                    st.error("Invalid OTP. Please try again.")

if __name__ == "__main__":
    homepage()
