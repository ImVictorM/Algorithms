from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # test_with_negative_key
    message = "papel caneta"
    reversed_message = "atenac lepap"
    assert encrypt_message(message, -1) == reversed_message

    # test_with_even_key
    message = "papelcaneta"
    encrypted_message = "atena_clepap"
    assert encrypt_message(message, 6) == encrypted_message

    # test_with_odd_key
    message = "papelcaneta"
    encrypted_message = "lepap_atenac"
    assert encrypt_message(message, 5) == encrypted_message

    # test_if_throws_when_message_type_is_invalid
    with pytest.raises(TypeError):
        encrypt_message(14, 5)

    # test_if_throws_when_key_type_is_invalid
    with pytest.raises(TypeError):
        encrypt_message("papel caneta", "sim")
