"""
    Testing class Equipment Singleton
"""

from app.interfaces import Equipment


class TestEquipmentSingleton:

    def test_singleton(self, equipment_file):
        eqip_1 = Equipment(equipment_file)
        eqip_2 = Equipment(equipment_file)
        assert id(eqip_1) == id(eqip_2)
