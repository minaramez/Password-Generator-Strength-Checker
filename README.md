# 🔐 **Password Generator & Strength Checker**

## **Overview**
This Python script serves as a **secure password generator** and **strength analyzer**. It ensures that generated passwords meet strong security standards while also evaluating the robustness of user-provided passwords using entropy calculations.

## **Features**
✅ **Generate secure passwords** (16-character randomized mix of uppercase, lowercase, digits, and special characters).  
🔍 **Analyze password strength** based on:
   - Length
   - Character variety (uppercase, lowercase, digits, special characters)
   - **Entropy calculation** to measure randomness.  
📊 **Entropy-based validation** ensures secure password generation.  
🛡️ **User-friendly menu** for easy interaction.  

---

## **Requirements**
- Python 3 installed on your system.

---

## **Installation**
Clone this repository:
```bash
git clone https://github.com/yourusername/password-security-tool.git
cd password-security-tool
```

Ensure the script has execute permissions:
```bash
chmod +x password_generator.py
```

---

## **Usage**
Run the script:
```bash
python3 password_generator.py
```

### **Menu Options**
| Option | Description |
|--------|-------------|
| 1 | Generate a secure password |
| 2 | Test the strength of an existing password |
| quit | Exit the script |

---

## **Example Output**
### **Generating a Password**
```
Choose an option:
1. Generate a secure password
2. Test the strength of a password
Enter your choice (1, 2, or 'quit' to exit): 1

Generated secure password: 8@XrT3z!pB5uF^yW
```

### **Checking Password Strength**
```
Choose an option:
1. Generate a secure password
2. Test the strength of a password
Enter your choice (1, 2, or 'quit' to exit): 2

Enter a password to analyze: mypassword123
Password should include at least one uppercase, lowercase, digit, and special character.
```

---

## **How Password Strength is Evaluated**
The script calculates password **entropy** to determine its strength.  
- **Entropy** is a measure of randomness; the higher the entropy, the stronger the password.
- **Thresholds:**
  - 🔴 **< 70 bits:** Weak password (too predictable)
  - 🟡 **70 - 79 bits:** Moderate security
  - 🟢 **80+ bits:** Strong password (high entropy)

### License
This script is released under the **MIT License**, which allows modification, distribution, and use with minimal restrictions.