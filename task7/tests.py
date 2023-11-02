from main import charivna_kulka, configure_charivna_kulka, answers, update_procent

# Перевірка, що функція поверне одне з очікуваних значень
def test_return_value():
    assert charivna_kulka("ask ?") in ["Так", "Ні", "Можливо"]

# Перевірка, що функція повертає значення типу 'str'
def test_return_type():
    assert isinstance(charivna_kulka("ask ?"),str)

# Перевірка, що функція повертає порожнє значення, коли було задане пусте питання
def test_return_empty():
    assert charivna_kulka("") is None

# Перевірка, що функція підкручує шанс
def test_update_procent():
    assert update_procent("Ні", 50) == ["Так", "Ні", "Можливо", "Ні"]

# Перевірка, що функція додає нові відповіді до базового списку відповедей кульки
def test_new_answers():
    new_answers = ["Не знаю", "Скоріш за все, ні"]
    configure_charivna_kulka(new_answers)
    for answer in new_answers:
        assert answer in answers
