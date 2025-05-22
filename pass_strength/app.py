import streamlit as st

def check_password(password):
    score = 0
    tips = []
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Password should be at least 8 characters long")
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Password should have at least one uppercase letter")
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Password should have at least one lowercase letter")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Password should have at least one digit")
    if any(c in "!@#$%^&*()_+-=" for c in password):
        score += 1
    else:
        tips.append("Password should have at least one special character i.e.!@#$%^&*()_+-=")
    return score, tips

def main():
    st.title("Password Strength Checker")
    st.write("This tool checks the strength of a password based on the following criteria:")
    st.write("- At least 8 characters long")
    st.write("- At least one uppercase letter")
    st.write("- At least one lowercase letter")
    st.write("- At least one digit")
    st.write("- At least one special character")
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Password"):
        score, tips = check_password(password)
        st.write(f"Password strength: {score}/5")
        if score == 5:
            st.write("Password is strong!")
        elif score == 4 or score == 3:
            st.write("Password is Moderate!")
        else:
            st.write("Password is weak!")
        for tip in tips:
            st.write(tip)
main()            