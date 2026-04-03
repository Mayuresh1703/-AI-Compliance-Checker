# -AI-Compliance-Checker
<img width="1906" height="902" alt="Screenshot 2026-04-03 230632" src="https://github.com/user-attachments/assets/f87635b1-b256-4953-b6d4-25005d94ff45" />
<img width="1891" height="794" alt="Screenshot 2026-04-03 230703" src="https://github.com/user-attachments/assets/fa90c3a8-c0f3-48fe-b83e-6e2708fb05ba" />
<img width="1804" height="865" alt="Screenshot 2026-04-03 230717" src="https://github.com/user-attachments/assets/d71f4836-1aa7-43af-b557-fd6d87f16b97" />
<img width="1822" height="870" alt="Screenshot 2026-04-03 230757" src="https://github.com/user-attachments/assets/59d118c7-a79a-4938-98dc-d72592cab811" />
<img width="1867" height="889" alt="Screenshot 2026-04-03 230838" src="https://github.com/user-attachments/assets/eed5a71f-2c29-44b5-bcfb-62efe8420195" />






# 💊 AI Regulatory Compliance Checker (Pharma + AI)

An advanced **AI-powered regulatory compliance system** for pharmaceutical documents that automatically analyzes uploaded PDFs and checks compliance based on regulatory rules inspired by **CDSCO (India), USFDA, and ICH guidelines**.

---

## 🚀 Features

* 🔐 Secure Login System
* 📄 PDF Upload & Text Extraction
* 🧠 Drug Type Detection (Tablet, Capsule, Syrup, Parenteral)
* ⚙️ Rule-Based Compliance Engine (Primary)
* 🤖 Machine Learning Support Model
* 🚨 Critical Error Detection
* ⚠️ Warning Classification
* 📊 Compliance Score Calculation
* 📋 Final Decision (Approved / Review / Rejected)
* 📑 Full Audit Report UI

---

## 🧠 How It Works

1. User logs in securely
2. Uploads a pharmaceutical PDF document
3. System extracts text using `pdfplumber`
4. Detects drug type automatically
5. Applies relevant regulatory rules
6. Identifies:

   * Missing requirements
   * Critical compliance failures
7. Calculates compliance score
8. Provides final decision and AI suggestion

---

## 🏗️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **PDF Processing:** pdfplumber
* **Machine Learning:** Scikit-learn (TF-IDF + Logistic Regression)
* **Security:** bcrypt
* **Data Handling:** pandas

---

## 📦 Installation

```bash
git clone https://github.com/your-username/pharma-ai-compliance.git
cd pharma-ai-compliance
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔐 Login Credentials

```
Username: mayuresh17
Password: Mayuresh@1234
```

---

## 📂 Project Structure

```
📁 pharma-ai-compliance/
│── app.py
│── requirements.txt
│── README.md
```

---

## 📊 Example Output

* Compliance Score: 92%
* Critical Errors: None
* Warnings: Minor
* Final Decision: ✅ APPROVED

---

## ⚠️ Important Note

This system is designed as an **AI-assisted compliance tool**.
It helps identify potential regulatory issues but should be used alongside professional validation.

---

## 🎯 Future Enhancements

* 📌 OCR support for scanned PDFs
* 🧠 BERT-based NLP model
* 📄 PDF error highlighting
* 📊 Dashboard analytics
* ☁️ Cloud deployment (AWS / Azure)
* 🔐 Multi-user authentication system

---

## 👨‍💻 Author

**Mayuresh Pathak**
B.Pharm + Data Science & AI

---

## ⭐ Contribute

Contributions, issues, and feature requests are welcome!

---

## 📜 License

This project is for educational and research purposes.
