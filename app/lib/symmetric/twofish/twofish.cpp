#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <cryptopp/twofish.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>

#include <string>

namespace py = pybind11;

py::bytes encrypt_twofish(
    py::bytes key_bytes,
    py::bytes plaintext_bytes)
{
    using namespace CryptoPP;

    std::string key = key_bytes;
    std::string plaintext = plaintext_bytes;

    std::string ciphertext;

    ECB_Mode<Twofish>::Encryption encryptor;

    encryptor.SetKey(
        reinterpret_cast<const byte *>(key.data()),
        key.size());

    StringSource ss(
        plaintext,
        true,
        new StreamTransformationFilter(
            encryptor,
            new StringSink(ciphertext)));

    return py::bytes(ciphertext);
}

py::bytes decrypt_twofish(
    py::bytes key_bytes,
    py::bytes ciphertext_bytes)
{
    using namespace CryptoPP;

    std::string key = key_bytes;
    std::string ciphertext = ciphertext_bytes;

    std::string recovered;

    ECB_Mode<Twofish>::Decryption decryptor;

    decryptor.SetKey(
        reinterpret_cast<const byte *>(key.data()),
        key.size());

    StringSource ss(
        ciphertext,
        true,
        new StreamTransformationFilter(
            decryptor,
            new StringSink(recovered)));

    return py::bytes(recovered);
}

PYBIND11_MODULE(twofishlib, m)
{
    m.def(
        "encrypt",
        &encrypt_twofish,
        "Encrypt using Twofish");

    m.def(
        "decrypt",
        &decrypt_twofish,
        "Decrypt using Twofish");
}
