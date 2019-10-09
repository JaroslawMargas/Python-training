from unittest import TestCase
from lesson_08_regular_expressions import validation_email


class TestValidation(TestCase) :

    def test_validation1(self) :
        self.assertEqual(validation_email.validation("alias@domain.pl"), True)

    def test_validation2(self) :
        self.assertEqual(validation_email.validation("alias@domain"), False)

    def test_validation3(self) :
        self.assertEqual(validation_email.validation("alias@"), False)

    def test_validation4(self) :
        self.assertEqual(validation_email.validation("alias"), False)

    def test_validation5(self) :
        self.assertEqual(validation_email.validation("@domain.pl"), False)

    def test_validation6(self) :
        self.assertEqual(validation_email.validation("domain.pl"), False)

    def test_validation7(self) :
        self.assertEqual(validation_email.validation(".pl"), False)

    def test_validation8(self) :
        self.assertEqual(validation_email.validation("alias@domain.co.uk"), True)

    def test_validation9(self) :
        self.assertEqual(validation_email.validation("alias@domain.co."), False)

    def test_validation10(self) :
        self.assertEqual(validation_email.validation("alias@domain.co.u!k"), False)

    def test_validation11(self) :
        self.assertEqual(validation_email.validation("alias@domain.c!#$%&'*+/=?^_`{|o.uk"), False)

    def test_validation12(self) :
        self.assertEqual(validation_email.validation("9alias@domain.co.uk"), False)

    def test_validation13(self) :
        self.assertEqual(validation_email.validation("alias@doma_.-in.co.uk"), False)

    def test_validation14(self) :
        self.assertEqual(validation_email.validation("ali as@domain.co.uk"), False)