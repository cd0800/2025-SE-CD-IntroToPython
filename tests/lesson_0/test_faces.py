from lesson_0.faces import convert

def test_faces():
    # Add your test cases here
    result = convert("Hello :) Goodbye :(")
    assert "Hello 🙂 Goodbye 🙁" == result
