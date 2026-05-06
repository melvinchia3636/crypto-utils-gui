<center><h1 align="center">🔐 Crypto Utils</h1></center>

<p align="center">A desktop cryptography explorer built with PyQt5</p>

## 🤔 The Problem (Not Really)

I was enrolled in a module titled Wireless Network & Security during my Bachelor's Degree in Software Engineering, which covered only briefly various cryptographic algorithms. Being a young man with infinite curiosity and a long-lived esteem in the wonderful world of cryptography, I was not satisfied at all. 

Just then, my dear lecturer found the little GUI app I built for a demonstration of symmetric crypto algorithms during the tutorial session, when other people were still trying to get their few lines of code running. And yeah, she was absolutely cool with that, and even gave me a task to extend the app to cover more algorithms, for both symmetric and asymmetric encryption.

## ✅ The Solution

So yeah, here we go. A PyQt5 desktop application that compiles a decently comprehensive collection of cryptographic algorithms into a relatively clean interface. I've built the codebase to be quite decently declarative and modular (like I usually do lol) btw, so if in the future a new cipher method is to be added, it will be pretty simple.

The last time I was building a GUI application was already like 5 years ago, when I was still a teen playing around with TKinter (yup, very legacy, I know, but somehow I managed to master that library). Picking it back up (but this time using PyQt5) wasn't that difficult anyway; some references and documentation were more than enough.

## ✨ Features

- **Symmetric Ciphers** - DES, 3DES, AES (GCM mode), Blowfish, Twofish, RC4, plus a consolidated view that encrypts with all algorithms at once
- **Asymmetric Cryptography** - RSA (OAEP encryption + PSS signing), ECC (ECDH + ECDSA), ElGamal, and Diffie-Hellman key agreement
- **Passphrase-Based Key Derivation** - No need to manage raw hex keys; enter a passphrase and a PBKDF2-derived key is used internally, with the derived key displayed for transparency
- **15+ Fun Encodings (100% Just for fun lol)** - View ciphertext as hex, base64, emoji, braille, runes, mathematical symbols, mahjong tiles, alchemy symbols, morse code, bars, binary, octal, and more — all switchable live from the encoding selector
- **PEM Key Import/Export** - Generate, export, and import PEM-encoded keys (public and private) for all asymmetric algorithms
- **Autofill Flow** - Generated keys are automatically propagated across related tabs (e.g., key generation auto-fills into encryption/decryption and signing/verification tabs)

## 🖥 Screenshots

<div>
  <img width="49%" alt="image" src="https://github.com/user-attachments/assets/722058aa-f5ca-4fc6-9eb7-b7f6818de375" />
  <img width="49%" alt="image" src="https://github.com/user-attachments/assets/58776425-3596-44cb-b043-cda58c37fe94" />
  <img width="49%" alt="image" src="https://github.com/user-attachments/assets/eef0b859-9539-4e57-abab-ef572b0e72b1" />
  <img width="49%" alt="image" src="https://github.com/user-attachments/assets/dab91a21-058e-488f-958d-a58d03b2433a" />
  <img width="49%" alt="image" src="https://github.com/user-attachments/assets/8a22cc88-6824-4390-a900-e5efe1966476" />
  <img width="49%" alt="image" src="https://github.com/user-attachments/assets/79a3fb8e-3034-41eb-baa6-9ac6956a8662" />
</div>

## 🔬 Technologies Used

![skills](https://img.shields.io/badge/-PYTHON-FF0000?style=for-the-badge&logo=python&logoColor=white&color=3776AB)
![skills](https://img.shields.io/badge/-PYQT5-FF0000?style=for-the-badge&logo=qt&logoColor=white&color=41CD52)
![skills](https://img.shields.io/badge/-PYCRYPTODOME-FF0000?style=for-the-badge&logo=python&logoColor=white&color=FFD43B)

**Core:** Python 3.12+, PyQt5, PyCryptodome  
**Cryptography:** AES, DES, 3DES, Blowfish, Twofish, RC4, RSA, ECC (ECDH/ECDSA), ElGamal, Diffie-Hellman  
**Key Derivation:** PBKDF2-HMAC-SHA256  
**Protocol:** PKCS#1 OAEP, PSS, ECIES hybrid encryption

## ⌨️ Setup

### Prerequisites

- Python 3.12+
- Crypto++ (for Twofish support)
- uv (Pls don't use default pip, it's slow af lol)

### Building the Twofish Native Module

The Twofish cipher is implemented as a C++ pybind11 module using Crypto++. The `.so` file must be built for your specific platform before running the app.

> [!NOTE]
> **Why a native module?** There is no reliable, well-maintained pure-Python Twofish implementation available. Crypto++ provides a trusted C++ implementation, and pybind11 bridges it to Python.

**macOS (Homebrew):**

```bash
brew install cryptopp pybind11
```

```bash
c++ -O3 -Wall -shared -std=c++17 \
  -undefined dynamic_lookup \
  $(python3 -m pybind11 --includes) \
  -I$(brew --prefix cryptopp)/include \
  app/cipher/symmetric/twofish/twofish.cpp \
  -o app/cipher/symmetric/twofish/twofishlib$(python3 -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))") \
  -L$(brew --prefix cryptopp)/lib \
  -lcryptopp
```

**Linux (APT):**

```bash
sudo apt install libcrypto++-dev pybind11-dev
```

```bash
c++ -O3 -Wall -shared -std=c++17 -fPIC \
  $(python3 -m pybind11 --includes) \
  app/cipher/symmetric/twofish/twofish.cpp \
  -o app/cipher/symmetric/twofish/twofishlib$(python3 -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))") \
  -lcryptopp
```

**Windows:**  
The build process for Windows is not documented here. You will need `cryptopp` and `pybind11` configured for your MSVC environment. Contributions welcome!



### Installation

```bash
cd crypto-utils-gui
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Running

```bash
source .venv/bin/activate
python3 main.py
```

## 🧪 Running Tests

This project Utils GUI includes inline verification tests embedded throughout the development process. All algorithms can be tested by running the app and performing encrypt/decrypt roundtrips on any algorithm tab.

## 🏗 Project Structure

```
app/
├── __init__.py              # Application entry point (App widget)
├── base/                    # Base classes for dynamic discovery
│   ├── cipher_frame.py      # CipherFrame data class
│   ├── content_tab.py       # ContentTab, TabbedFrame widgets
│   ├── encoder.py           # Encoder base class
│   └── form_component.py    # FormComponent base class
├── cipher/
│   ├── asymmetric/          # Asymmetric ciphers (RSA, ECC, DH, ElGamal)
│   └── symmetric/           # Symmetric ciphers (DES, AES, Blowfish, etc.)
├── encoding/
│   ├── standard/            # Standard encodings (hex, base64, etc.)
│   └── fun/                 # Fun encodings (emoji, braille, etc.)
├── forms/
│   ├── components/          # Reusable form widget builders
│   ├── utils/               # Shared utilities (row_col helper)
│   └── encoding_selector.py # Encoding selector widget
└── helpers/
    ├── algorithm_browser.py # Split-pane browser widget
    ├── discover_modules.py  # Plugin discovery utility
    └── key_derivation.py    # PBKDF2 key derivation + constants
```

## 🔌 Architecture

This project uses a **dynamic module discovery** pattern:

- **Ciphers** export a `CipherFrame` instance from their `__init__.py`
- **Encodings** export an `Encoder` subclass with `encode`/`decode` methods
- **Form components** export a `FormComponent` subclass with a `build` method
- The `discover_modules()` helper auto-discovers all plugins at startup — no manual registration needed when adding new algorithms

## ⌨️ Supported Algorithms

| Category | Algorithms |
|----------|-----------|
| **Symmetric** | DES, 3DES, AES-128-GCM, Blowfish, Twofish, RC4, Consolidated (all at once) |
| **Asymmetric** | RSA (OAEP + PSS), ECC (ECDH + ECDSA), ElGamal, Diffie-Hellman |

## 🎨 Encodings

| Group | Encodings |
|-------|-----------|
| **Standard** | Hex, Base64, Base32, Base58, Base16 |
| **Fun** | Emoji, Bars, Braille, Runes, Math Symbols, Mahjong Tiles, Alchemy Symbols, Binary, Octal, Morse Code, Base 128 |

Feel free to add more.

## 📈 Status

All core cryptographic functions have been completed. The application is fully functional with a modular, extensible architecture. New algorithms can be added easily in the future.

## 🙏 Credits

This project would not be possible without them:

- **My Brain** for staying curious at all time and diving deep through all the theoretical side of stuff, getting a decent understanding of each algo.
- **[Deepseek](https://deepseek.com)** via OpenCode - **Assisted** with implementation of cryptographic primitives and UI components
- **[Dr. Poornima Mahadevappa](https://www.linkedin.com/in/poornima-mahadevappa-bb325244/)** - My lecturer for the module for giving me the courage and motivation to explore the field of cryptography.

## 📄 License

This project is licensed under the MIT License.
