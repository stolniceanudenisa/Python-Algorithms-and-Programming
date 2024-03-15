from Domain.imobil import Imobil


def test_imobil_getteri():
    imobil = Imobil("1", "Dorobanti", "1000", "vanzare")
    assert imobil.get_id_imobil() == "1"
    assert imobil.get_adresa_imobil() == "Dorobanti"
    assert imobil.get_pret_imobil() == "1000"
    assert imobil.get_tip_imobil() == "vanzare"


def test_imobil_setteri():
    imobil = Imobil("1", "Dorobanti", "1000", "vanzare")
    imobil.set_id_imobil("2")
    imobil.set_adresa_imobil("Cluj")
    imobil.set_pret_imobil("2000")
    imobil.set_tip_imobil("inchiriere")
    assert imobil.get_id_imobil() == "2"
    assert imobil.get_adresa_imobil() == "Cluj"
    assert imobil.get_pret_imobil() == "2000"
    assert imobil.get_tip_imobil() == "inchiriere"
