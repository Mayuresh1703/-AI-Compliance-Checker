# =========================================================
# 💊 FIXED PHARMA AI COMPLIANCE SYSTEM
# =========================================================

import streamlit as st
import pdfplumber
import bcrypt
import pandas as pd

# =========================================================
# 🔐 LOGIN SYSTEM (FIXED WITH SESSION)
# =========================================================

USERNAME = "mayuresh17"
PASSWORD_HASH = bcrypt.hashpw("Mayuresh@1234".encode(), bcrypt.gensalt())

def login(user, pwd):
    if user == USERNAME:
        return bcrypt.checkpw(pwd.encode(), PASSWORD_HASH)
    return False

# SESSION FIX
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =========================================================
# 📄 PDF TEXT EXTRACTION
# =========================================================

def extract_text(pdf):
    text = ""
    try:
        with pdfplumber.open(pdf) as pdf_file:
            for page in pdf_file.pages:
                text += page.extract_text() or ""
    except:
        text = ""
    return text.lower()


# =========================================================
# 💊 DRUG TYPE DETECTION
# =========================================================

def detect_drug_type(text):
    if "tablet" in text:
        return "tablet"
    elif "capsule" in text:
        return "capsule"
    elif "injection" in text or "parenteral" in text:
        return "parenteral"
    elif "syrup" in text:
        return "syrup"
    return "general"


# =========================================================
# 📚 RULES
# =========================================================

RULES = {
    "tablet": ["dissolution", "uniformity"],
    "parenteral": ["sterility", "endotoxin"],
    "general": ["batch record", "stability", "label"]
}


# =========================================================
# ⚙️ RULE CHECK
# =========================================================

def evaluate(text):
    drug_type = detect_drug_type(text)

    rules = RULES.get(drug_type, []) + RULES["general"]

    results = []
    score = 0
    critical_fail = False

    for r in rules:
        if r in text:
            results.append((r, "✅ PASS"))
            score += 1
        else:
            results.append((r, "❌ FAIL"))
            critical_fail = True

    accuracy = (score / len(rules)) * 100
    return results, accuracy, critical_fail, drug_type


# =========================================================
# 🌐 STREAMLIT UI
# =========================================================

st.title("💊 AI Compliance Checker")

# LOGIN UI
user = st.sidebar.text_input("Username")
pwd = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    if login(user, pwd):
        st.session_state.logged_in = True
    else:
        st.sidebar.error("Invalid Credentials")

# AFTER LOGIN
if st.session_state.logged_in:

    st.sidebar.success("Login Successful ✅")

    st.subheader("📂 Upload PDF")
    file = st.file_uploader("Upload PDF", type=["pdf"])

    if file:
        text = extract_text(file)

        # DEBUG
        st.write("🔍 Extracted Text Length:", len(text))

        if len(text) == 0:
            st.error("❌ No text found in PDF (maybe scanned image)")
        else:
            st.text_area("📄 Extracted Text", text[:2000])

            results, score, critical, drug_type = evaluate(text)

            st.subheader("💊 Drug Type")
            st.info(drug_type)

            st.subheader("📊 Score")
            st.success(f"{score:.2f}%")

            st.subheader("📋 Results")
            df = pd.DataFrame(results, columns=["Rule", "Status"])
            st.dataframe(df)

            st.subheader("📌 Final Decision")
            if critical:
                st.error("❌ NON-COMPLIANT")
            else:
                st.success("✅ COMPLIANT")

else:
    st.info("🔐 Please login to continue")