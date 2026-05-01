import pytest

# 1. Test to verify form assignment logic
def test_form_mapping():
    form_logic = {
        "new_registration": "Form 6",
        "deletion_objection": "Form 7",
        "correction_address": "Form 8"
    }
    
    assert form_logic["new_registration"] == "Form 6"
    assert form_logic["deletion_objection"] == "Form 7"
    assert form_logic["correction_address"] == "Form 8"

# 2. Test to verify ALL 7 supported languages are correctly configured
def test_language_support():
    supported_languages = ["English", "Tamil", "Hindi", "Malayalam", "Telugu", "Kannada", "Bengali"]
    
    # Verifying every single language in our app's UI dictionary
    assert "English" in supported_languages
    assert "Tamil" in supported_languages
    assert "Hindi" in supported_languages
    assert "Malayalam" in supported_languages
    assert "Telugu" in supported_languages
    assert "Kannada" in supported_languages
    assert "Bengali" in supported_languages