import unittest

from medilink_contract import build_summary


class TestPatientSummaryContract(unittest.TestCase):
    def setUp(self):
        self.patient = {"patient_id": "P1001", "name": "Ana Reyes"}
        self.appointments = [{"date": "2026-10-05", "service": "Consultation"}]

    def test_summary_preserves_required_public_contract(self):
        summary = build_summary(self.patient, self.appointments)

        self.assertEqual(set(summary), {"patient", "appointments", "clinic_status"})
        self.assertEqual(summary["patient"]["patient_id"], "P1001")
        self.assertEqual(summary["appointments"], self.appointments)
        self.assertEqual(summary["clinic_status"], "ACTIVE")

    def test_custom_clinic_status_is_normalized(self):
        summary = build_summary(self.patient, self.appointments, " maintenance ")
        self.assertEqual(summary["clinic_status"], "MAINTENANCE")

    def test_missing_patient_identifier_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "patient_id"):
            build_summary({"name": "Missing identifier"}, self.appointments)

    def test_appointments_must_be_a_list(self):
        with self.assertRaisesRegex(ValueError, "appointments must be a list"):
            build_summary(self.patient, {"date": "2026-10-05"})


if __name__ == "__main__":
    unittest.main()
